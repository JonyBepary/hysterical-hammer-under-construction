import argparse
import sys
import os
import docopt


def parse(args):
    parser = argparse.ArgumentParser(usage='hho [-commands] [file/dir]')
    if(args == 0):
        return parser.print_help()
    parser.add_argument('filename', help='Optimize file filename')
    parser.add_argument('-em', '--exclude-media',
                        help='Optimized full site excluding media',
                        default='False')
    parser.add_argument('-ec', '--exclude-code',
                        help='Optimized full site excluding code',
                        default='False')
    return parser.parse_args()


if __name__ == '__main__':
    cmd = sys.argv[1:]
    try:
        if(cmd[0][0] != '-'):
            if(os.path.isfile(os.path.join(os.getcwd(), cmd[0]))):
                print(cmd[0], 'file found\n')
            else:
                print(cmd[0], 'file not found\n')
        else:
            parse(cmd)
    except IndexError:
        parse(0)
