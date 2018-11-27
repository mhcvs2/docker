#!/usr/bin/python
# -*- coding: utf-8 -*-
#put this to ansible remote_tmp
import os
import os.path
import sys
import __main__
import zipfile
import tempfile
import base64
scriptdir = None
try:
    scriptdir = os.path.dirname(os.path.abspath(__main__.__file__))
except (AttributeError, OSError):
    # Some platforms don't set __file__ when reading from stdin
    # OSX raises OSError if using abspath() in a directory we don't have
    # permission to read.
    pass
if scriptdir is not None:
    sys.path = [p for p in sys.path if p != scriptdir]

import subprocess
import shutil

if sys.version_info < (3,):
    bytes = str
    PY3 = False
else:
    unicode = str
    PY3 = True
try:
    # Python-2.6+
    from io import BytesIO as IOStream
except ImportError:
    # Python < 2.6
    from StringIO import StringIO as IOStream

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        print('\n{"msg": "Error: ansible requires the stdlib json or simplejson module, neither was found!", "failed": true}')
        sys.exit(1)
    except SyntaxError:
        print('\n{"msg": "SyntaxError: probably due to installed simplejson being for a different python version", "failed": true}')
        sys.exit(1)

def invoke_module(module, modlib_path, json_params):
    pythonpath = os.environ.get('PYTHONPATH')
    if pythonpath:
        os.environ['PYTHONPATH'] = ':'.join((modlib_path, pythonpath))
    else:
        os.environ['PYTHONPATH'] = modlib_path

    p = subprocess.Popen(['/usr/bin/python', module, json_params], env=os.environ, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    (stdout, stderr) = p.communicate()

    if not isinstance(stderr, (bytes, unicode)):
        stderr = stderr.read()
    if not isinstance(stdout, (bytes, unicode)):
        stdout = stdout.read()
    if PY3:
        sys.stderr.buffer.write(stderr)
        sys.stdout.buffer.write(stdout)
    else:
        sys.stderr.write(stderr)
        sys.stdout.write(stdout)
    return p.returncode

if __name__ == '__main__':

    if(len(sys.argv)<2):
        print "lack para"
        sys.exit(1)
    if(os.path.isfile(sys.argv[1])):
        #/tmp/ansible/ansible-tmp-1508035392.94-193205129467521/command.py
        command_path = sys.argv[1]
        command_dir = os.path.dirname(command_path)
        cmd = "python %s explode >/dev/null" %command_path
        subprocess.check_call(cmd, shell=True)
        debug_dir = os.path.join(command_dir, "debug_dir")
        if not os.path.exists(debug_dir):
            print "extart module failed"
            sys.exit(1)
        cmd = "cp -rn %s/* %s" %(debug_dir, scriptdir)
        subprocess.check_call(cmd, shell=True)
        shutil.rmtree(command_dir)
        sys.exit(0)

    temp_path = tempfile.mkdtemp(prefix='ansible_')
    zipped_mod = os.path.join(temp_path, 'ansible_modlib.zip')
    modlib = open(zipped_mod, 'wb')
    modlib.write(base64.b64decode(sys.argv[1]))
    modlib.close()

    z = zipfile.ZipFile(zipped_mod, mode='r')
    args = z.read('ansible_args')
    params = json.loads(args.decode('utf-8'))

    module_name = params["ANSIBLE_MODULE_ARGS"]["_ansible_module_name"]
    module_file_name = 'ansible_module_'+module_name+".py"
    args_file_name = 'ansible_module_'+module_name+"_args"

    module = os.path.join(scriptdir, module_file_name)
    args_file = os.path.join(temp_path, args_file_name)
    with open(args_file, 'w') as f:
        f.write(args)
    exitcode = invoke_module(module, scriptdir, args_file)
    shutil.rmtree(temp_path)
    sys.exit(exitcode)
