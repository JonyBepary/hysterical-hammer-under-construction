"""Run external process manager.
Function:
    ExtArgs()       Arguments for external programs.
    run_ext()       Run EXTERNAL program.
"""
import subprocess
import os
import configparser
from library import config

if __name__ == '__main__':
    cwd = os.getcwd()
    cwd = os.path.join(cwd, 'file_lib')
    # print(cwd)


class ExtArgs(object):
    """Arguments for external programs."""

    def __init__(self, old_filename, new_filename):
        """Set arguments."""
        self.old_filename = old_filename
        self.new_filename = new_filename



def run_ext(args, root=None):
    """Run EXTERNAL program."""
    # root_wd = root
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
    # os.chdir(root)
