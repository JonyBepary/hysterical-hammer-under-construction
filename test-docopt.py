"""test docopt.
Usage:
  test-docopt.py <NAME>...
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
  -h, --help             Show this screen.
  -c, --check-file       Check if <FILE> is optimized.
  -m, --make-xxhash      Make <FILE> Hash and print.
  -t, --only-text        Optimize only text based file. (eg. html, css, js)
  -b, --only-binary      Optimize only binary based file. (eg. jpg, png, svg)
  -D, --directory        Show directory.
  -L, --unoptimize-list  Show unoptimize list.
  -cc, --cat-config      Check and Show hho config file.
  -s, --setup            Setup hho config.
  -mc, --make-config     Make a config  hho config

Examples:
  python test-docopt.py pic.jpg     Optimize a file.
  python test-docopt.py _site       Optimize a directory.
  python test-docopt.py -b _site    Optimize a directory excluding text based file.

Hystrical hammmer project site: <https://github.com/JonyBepary/hysterical-hammer>
The naming inspiration can be found: <https://www.readmng.com/combat-continent/4/16>

"""

from docopt import docopt
import sys

if __name__ == '__main__':
  print(__name__)
  arguments = docopt(__doc__, version='test docopt 2.0')
  print('Start:\n')
  print(arguments)
