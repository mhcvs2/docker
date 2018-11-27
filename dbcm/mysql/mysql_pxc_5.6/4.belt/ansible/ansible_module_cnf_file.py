from ansible.module_utils.config.mysql_cnf import Mycnf
try:
    import json5
    json5_found = True
except ImportError:
    json5_found = False
try:
    import MySQLdb
    mysqldb_found = True
except ImportError:
    mysqldb_found = False

DOCUMENTATION = '''
module: cnf_file
short_description: modify .cnf file
description:
 - modify .cnf file
version_added: "0.1"
options:
  action:
    description:
      - action
    required: false
    default: update
    choices: [ "update", "get", "delete", "updateAll", "deleteAll"]
  section:
    description:
      - section
    required: false
    default: None
  option:
    description:
      - option
    required: false
    default: None
  value:
    description:
      - value
    required: false
    default: None
  path:
    description:
      - path
    type: path
    required: false
    default: /etc/my.cnf
'''

def getDbUser(cursor):
    query = 'use mysql;'
    cursor.execute(query)
    query='SELECT Db,User FROM db;'
    cursor.execute(query)
    res = cursor.fetchall()
    r = {}
    for db, user in res:
        if not user:
            continue
        if db not in r:
            r[db] = [user]
        else:
            r[db].append(user)
    return json5.dumps(r)

def typedvalue(value):
    """
    Convert value to number whenever possible, return same value
    otherwise.

    >>> typedvalue('3')
    3
    >>> typedvalue('3.0')
    3.0
    >>> typedvalue('foobar')
    'foobar'

    """
    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value

def getvariable(cursor, mysqlvar):
        cursor.execute("SHOW VARIABLES WHERE Variable_name = %s", (mysqlvar,))
        mysqlvar_val = cursor.fetchall()
        if len(mysqlvar_val) is 1:
            return mysqlvar_val[0][1]
        else:
            return None

def setvariable(cursor, mysqlvar, value):
    mysqlvar_val = getvariable(cursor, mysqlvar)
    if mysqlvar_val is None:
        return "Variable not available \"%s\"\n" % mysqlvar
    if value is not None:
        # Type values before using them
        value_wanted = typedvalue(value)
        value_actual = typedvalue(mysqlvar_val)
        query = "SET GLOBAL %s = " % mysql_quote_identifier(mysqlvar, 'vars')
        try:
            cursor.execute(query + "%s", (value_wanted,))
            cursor.fetchall()
            result = True
        except Exception:
            e = get_exception()
            result = str(e)
        if result is True:
            return "Variable change succeeded in memory\n"
        else:
            return result
    return ""

def main():
    module = AnsibleModule(
        argument_spec=dict(
            action=dict(default="update",choice=["update","delete","get", "updateAll", "deleteAll"]),
            section=dict(default="mysqld"),
            option=dict(default=None),
            value=dict(default=None),
            paras=dict(default=None),
            path=dict(default="/etc/my.cnf",type='path'),
            mem=dict(default=False, type='bool'),
            login_user=dict(default="root"),
            login_password=dict(default=None, no_log=True),
            login_unix_socket=dict(default=None),
            login_host=dict(default="localhost"),
            login_port=dict(default=3306, type='int'),
        ),
        supports_check_mode=True
    )

    action = module.params["action"]
    section = module.params["section"]
    option = module.params["option"]
    value = module.params["value"]
    paras = module.params["paras"]
    path = module.params["path"]
    mem = module.params["mem"]
    user = module.params["login_user"]
    password = module.params["login_password"]

    if not mysqldb_found:
        module.fail_json(msg="the python mysqldb module is required")
    if not json5_found:
        module.fail_json(msg="the python json5 module is required")

    message = ""
    if not os.path.exists(path):
        if action in ["get","delete"]:
            module.fail_json(msg="%s do not exist" %path, changed=False, failed=True)
        else:
            message += "%s do not exist, create it\n" % path
    changed = False
    if action == "getdbuser":
        try:
            cursor = mysql_connect(module, login_user=user, login_password=password)
        except Exception as e:
            module.fail_json(msg=e.message, changed=False, failed=True)
        dbusers = getDbUser(cursor)
        module.exit_json(changed=True, stdout=dbusers, failed=False)
    try:
        cnf = Mycnf(path)
        if action == "get":
            if section and option:
                value = cnf.get(section,option)
                message += "%s=%s" %(option,str(value))
                changed = True
            elif section:
                message += "[%s]\n" %(section)
                for option in cnf.options(section):
                    value = cnf.get(section, option)
                    message += "%s=%s\n" % (option, str(value))
                changed = True
            elif option:
                module.fail_json(msg="section is needed.", changed=False, failed=True)
            else:
                with open(path, "r") as f:
                    message = f.read()
                    changed = True
        elif action == "update":
            if not section or not option or not value:
                module.fail_json(msg="section, option, value is needed.", changed=False, failed=True)
            if not cnf.has_section(section):
                message += "add section %s\n" %section
                cnf.add_section(section)
                message += "add %s=%s\n" %(option,value)
                changed = True
            elif cnf.has_option(section,option):
                old_value =cnf.get(section,option)
                if old_value == value:
                   changed = False
                else:
                    message += "update value of option %s from %s to %s\n" %(option,old_value,value)
                    changed = True
            else:
                message += "add %s=%s\n" %(option,value)
                changed = True
            if changed:
                if mem:
                    try:
                        cursor = mysql_connect(module, login_user=user, login_password=password)
                        message += setvariable(cursor, option, value)
                    except Exception as e:
                        module.fail_json(msg=e.message,changed=False, failed=True)
                cnf.set(section, option, value)
        elif action == "delete":
            if section:
                if cnf.has_section(section):
                    if option:
                        if cnf.has_option(section,option):
                            cnf.remove_option(section,option)
                            message += "delete option %s in section %s\n" %(option,section)
                            changed = True
                    else:
                        cnf.remove_section(section)
                        message += "delete section %s" %section
                        changed = True
        elif action == "updateAll":
            if not section:
                section = "mysqld"
            if not paras:
                module.fail_json(msg="paras is needed.", changed=False, failed=True)
            paras = json5.loads(paras)
            if not isinstance(paras, dict):
                module.fail_json(msg="paras isn't a dict", changed=False, failed=True)
            if mem:
                try:
                    cursor = mysql_connect(module, login_user=user, login_password=password)
                except Exception as e:
                    module.fail_json(msg=e.message, changed=False, failed=True)
            if not cnf.has_section(section):
                message += "add section %s\n" %section
                cnf.add_section(section)
                changed = True
            for option, value in paras.items():
                if cnf.has_option(section, option):
                    old_value = cnf.get(section, option)
                    if old_value != value:
                        message += "update value of option %s from %s to %s\n" % (option, old_value, value)
                        if mem:
                            try:
                                message += setvariable(cursor, option, value)
                            except Exception as e:
                                module.fail_json(msg=e.message, changed=False, failed=True)
                        cnf.set(section, option, value)
                        changed = True
                else:
                    message += "add %s=%s\n" % (option, value)
                    if mem:
                        try:
                            message += setvariable(cursor, option, value)
                        except Exception as e:
                            module.fail_json(msg=e.message, changed=False, failed=True)
                    cnf.set(section, option, value)
                    changed = True
        elif action == "deleteAll":
            if not section:
                section = "mysqld"
            if not paras:
                module.fail_json(msg="paras is needed.", changed=False, failed=True)
            paras = json5.loads(paras)
            if not isinstance(paras, list):
                module.fail_json(msg="paras isn't a list", changed=False, failed=True)
            for option in paras:
                if cnf.has_option(section, option):
                    cnf.remove_option(section, option)
                    message += "delete option %s in section %s\n" % (option, section)
                    changed = True

        if changed:
            cnf.update()
        module.exit_json(changed=changed, stdout=message, failed=False)
    except Exception as e:
        module.fail_json(msg=e.message, changed=False, failed=True)

from ansible.module_utils.basic import *
from ansible.module_utils.database import *
from ansible.module_utils.mysql import *

if __name__ == '__main__':
    main()