try:
    from collections import OrderedDict as _default_dict
except ImportError:
    _default_dict = dict
try:
    import json5
    json5_found = True
except ImportError:
    json5_found = False
try:
    import redis
    redis_found = True
except ImportError:
    redis_found = False

DOCUMENTATION = '''
module: redis_cnf
short_description: modify  redis conf file
description:
 - modify  redis conf file
version_added: "0.1"
options:
  action:
    description:
      - action
    required: false
    default: update
    choices: [ "update", "get", "delete"]
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

class RedisConf(object):
    def __init__(self, path):
        self._dict = _default_dict()
        self.path = path
        if not os.path.isfile(path):
            raise Exception("%s does not exist or not a file")
        self.read()

    def read(self):
        with open(self.path, "r") as fp:
            while True:
                line = fp.readline()
                if not line:
                    break
                if line.strip() == '' or line[0] in '#;':
                    continue
                line = line.strip()
                kv = line.split(" ", 1)
                if len(kv) == 1:
                    self._dict[kv[0]] = ""
                else:
                    self._dict[kv[0]] = kv[1]

    def write(self):
        with open(self.path, "wa") as fp:
            for k, v in self._dict.items():
                fp.write(k + " " + v + "\n")

    def has_option(self, option):
        return option in self._dict.keys()

    def get_dict(self):
        return self._dict

    def get(self, option):
        if not self.has_option(option):
            raise Exception("No this option %s." % option)
        return self._dict[option]

    def remove_option(self, option):
        if not self.has_option(option):
            raise Exception("No this option %s." % option)
        del self._dict[option]

    def options(self):
        return self._dict.keys()

    def set(self, option, value):
        self._dict[option] = value

    def __str__(self):
        return str(self._dict)

def main():
    module = AnsibleModule(
        argument_spec=dict(
            action=dict(default="update",choice=["update","delete","get"]),
            option=dict(default=None),
            value=dict(default=None),
            paras=dict(default=None),
            path=dict(default="/etc/redis.conf",type='path'),
            mem=dict(default=False, type='bool')
        ),
        supports_check_mode=True
    )

    action = module.params["action"]
    option = module.params["option"]
    value = module.params["value"]
    paras = module.params["paras"]
    path = module.params["path"]
    mem = module.params["mem"]

    if not json5_found:
        module.fail_json(msg="the python json5 module is required")
    if not redis_found:
        module.fail_json(msg="the python redis module is required")

    message = ""
    if not os.path.exists(path):
        if action in ["get","delete"]:
            module.fail_json(msg="%s do not exist" %path, changed=False, failed=True)
        else:
            message += "%s do not exist, create it\n" % path
    changed = False
    try:
        cnf = RedisConf(path)
        if action == "get":
            if option:
                value = cnf.get(option)
                message += "%s=%s" %(option,str(value))
                changed = True
            else:
                kvs = cnf.get_dict()
                for k, v in kvs.items():
                    message += "%s=%s\n" % (k, str(v))
                changed = True
        elif action == "update":
            if not option or not value:
                module.fail_json(msg="option, value is needed.",changed=False, failed=True)
            if not cnf.has_option(option):
                changed = True
                message += "add %s %s\n" % (option, value)
            else:
                pre_value = cnf.get(option)
                if pre_value != value:
                    changed = True
                    message += "update value of option %s from %s to %s\n" % (option, pre_value, value)
            if changed:
                if mem:
                    try:
                        client = redis.StrictRedis(host="localhost", port=6379)
                        client.config_set(option, value)
                    except Exception as e:
                        module.fail_json(msg=e.message,changed=False, failed=True)
                cnf.set(option,value)
        elif action == "delete":
            if cnf.has_option(option):
                changed = True
                cnf.remove_option(option)
                message += "delete option %s" % option
        elif action == "updateAll":
            if not paras:
                module.fail_json(msg="paras is needed.",changed=False, failed=True)
            paras = json5.loads(paras)
            if not isinstance(paras, dict):
                module.fail_json(msg="paras isn't a dict",changed=False, failed=True)
            if mem:
                try:
                    client = redis.StrictRedis(host="localhost", port=6379)
                except Exception as e:
                    module.fail_json(msg=e.message,changed=False, failed=True)
            for option, value in paras.items():
                if cnf.has_option(option):
                    old_value = cnf.get(option)
                    if old_value != value:
                        message += "update value of option %s from %s to %s\n" % (option, old_value, value)
                        if mem:
                            try:
                                client.config_set(option, value)
                            except Exception as e:
                                module.fail_json(msg=e.message)
                        cnf.set(option, value)
                        changed = True
                else:
                    message += "add %s=%s\n" % (option, value)
                    if mem:
                        try:
                            client.config_set(option, value)
                        except Exception as e:
                            module.fail_json(msg=e.message)
                    cnf.set(option, value)
                    changed = True
        elif action == "deleteAll":
            if not paras:
                module.fail_json(msg="paras is needed.", changed=False, failed=True)
            paras = json5.loads(paras)
            if not isinstance(paras, list):
                module.fail_json(msg="paras isn't a list",changed=False, failed=True)
            for option in paras:
                if cnf.has_option(option):
                    cnf.remove_option(option)
                    message += "delete option %s\n" % (option)
                    changed = True
        if changed:
            cnf.write()
        module.exit_json(changed=changed, stdout=message,failed=False)
    except Exception as e:
        module.fail_json(msg=e.message,changed=False, failed=True)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()