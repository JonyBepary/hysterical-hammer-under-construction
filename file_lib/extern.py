"""Run external programs."""
# import absolute_import
# import division
# import print_function

import subprocess
import os
import configparser

cwd = os.getcwd()
cwd = os.path.join(cwd, 'file_lib')
# print(cwd)


def ext_root_set(core_root_wd):
    cwd1 = os.path.join(cwd, '_config_extern.ini')
    # print('extern root_wd: ', core_root_wd, 'getcwd: ', cwd)
    config = configparser.ConfigParser()
    config.read(os.path.join(cwd, '_config_extern.ini'))
    config.set('EXTERN', 'root_wd', core_root_wd)
    with open(cwd1, 'w') as fp:
        config.write(fp)
    return True


def ext_root_get():
    config = configparser.ConfigParser()
    config.read(os.path.join(cwd, '_config_extern.ini'))
    con_str = config['EXTERN']['root_wd']
    return con_str


class ExtArgs(object):
    """Arguments for external programs."""

    def __init__(self, old_filename, new_filename):
        """Set arguments."""
        self.old_filename = old_filename
        self.new_filename = new_filename


def does_external_program_run(prog, verbose):
    """Test to see if the external programs can be run."""
    try:
        with open('/dev/null') as null:
            subprocess.call([prog, '-h'], stdout=null, stderr=null)
        result = True
    except OSError:
        if verbose > 1:
            print("couldn't run {}".format(prog))
        result = False

    return result


def run_ext(args, root=None):
    """Run EXTERNAL program."""
    root_wd = ext_root_get()
    # print('run_ext cwd: ', root_wd)
    if root != None:
        os.chdir(root)
    # print(args)
    if False:
        os.chdir(root_wd)
        return 0
    try:
        subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as exc:
        print(exc)
    os.chdir(root_wd)
