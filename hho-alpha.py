"""test docopt.
Usage:
  test-docopt.py <NAME>...
  test-docopt.py -s | --strike
  test-docopt.py --version
  test-docopt.py -h | --help
  test-docopt.py [--check-file] [--make-xxhash] [--cat-config]
                 [--make-config] [--optional] <FILE>...
  test-docopt.py [--only-binary] [--only-text] [--unoptimize-list]
                 [--setup] [--make-config] [--directory] [--optional] [<DIR>]...

Arguments:
  NAME  it can a DIR or FILE.
  DIR   working directory.
  FILE  working file.

Options:
  --version              Show version.
  --author               Show version.
  -h, --help             Show this screen.
  -c, --check-file       Check if <FILE> is optimized.
  -m, --make-xxhash      Make <FILE> Hash and print.
  -s, --strike           Optimize all files in current dir & sub-dir
  -t, --only-text        Optimize only text based file. (eg. html, css, js)
  -b, --only-binary      Optimize only binary based file. (eg. jpg, png, svg)
  -D, --directory        Show directory.
  -L, --unoptimize-list  Show unoptimize list.
  -cc, --cat-config      Check and Show hho config file.
  -S, --setup            Setup hho config.
  -mc, --make-config     Make a config  hho config

Examples:
  python test-docopt.py pic.jpg     Optimize a file.
  python test-docopt.py _site       Optimize a directory.
  python test-docopt.py -b _site    Optimize a directory excluding text based file.

Hystrical hammmer project site: <https://github.com/JonyBepary/hysterical-hammer>
The naming inspiration can be found: <https://www.readmng.com/combat-continent/4/16>

"""

from docopt import docopt
import os
import sys
import command_processor

# arg['<DIR>']
# arg['<FILE>']
# arg['<NAME>']


def arg_procces(arg, key):
  print('start')
  if key == '--strike':
    command_processor.strike(os.getcwd())
  elif key == '--check-file':
    if arg['<FILE>']:
      command_processor.check_file(arg['<FILE>'])
    else:
      return FileNotFoundError

  elif key == '--make-xxhash':
    if arg['<FILE>']:
      command_processor.make_xxhash(arg['<FILE>'])
    else:
      return FileNotFoundError

  elif key == '--cat-config':
    if arg['<FILE>']:
      command_processor.cat_config(arg['<FILE>'])
    else:
      return FileNotFoundError

  elif key == '--make-config':
    if arg['<FILE>']:
      command_processor.make_config(arg['<FILE>'])
    else:
      pass

  elif key == '--optional':
    if arg['<FILE>']:
      command_processor.optional(arg['<FILE>'])
    else:
      pass

  elif key == '--only-binary':
    print('True!!!')
    if arg['<DIR>']:
      command_processor.only_binary(os.getcwd())
    else:
      pass

  elif key == '--only-text':
    if arg['<DIR>']:
      command_processor.only_text(os.getcwd())
    else:
      pass

  elif key == '--unoptimize-list':
    if arg['<DIR>']:
      command_processor.unoptimize_list(os.getcwd())
    else:
      pass

  elif key == '--setup':
    command_processor.setup(os.getcwd())


if __name__ == '__main__':
  print(__name__)
  arguments = docopt(__doc__, version='test docopt 2.0')
  for argument, value in arguments.items():
    if value == True:
      arg_procces(arguments, argument)
      break
    else:
      if arguments['<NAME>']:
        pass
        break

# arguments[<DIR>] | arguments[<FILE>] |

# <NAME>
# <DIR>
# <FILE>
