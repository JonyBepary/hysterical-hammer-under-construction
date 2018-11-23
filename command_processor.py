''' is process each and every command given by hho
'''
import core
import os


def strike(FILE=None):
    if __name__ == '__main__':
        FILE = core.tartget_dir_func(os.getcwd())
    return core.controller('all', FILE)
    print('striking\n')


strike(os.getcwd())


def setup(FILE=None):
    print('setup\n')


def directory(args, FILE=None):
    print('directory\n')


def optional(FILE=None):
    print('optional\n')


def check_file(FILE=None):
    print('check_file\n')



def make_xxhash(FILE=None):
    print('make_xxhash\n')


def cat_config(FILE=None):
    print('cat_config\n')


def make_config(FILE=None):
    print('make_config\n')


def only_binary(FILE=None):
    return core.controller('b', FILE)
    print('only_binary\n')


def only_text(FILE=None):
    return core.controller('t', FILE)
    print('only_text\n')


def unoptimize_list(FILE=None):
    print('unoptimize_list\n')



def make_config(FILE=None):
    print('make_config\n')
