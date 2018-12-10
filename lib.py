'''library used and imported in this program'''
# ----------------------------library----------------------------
import os
from itertools import chain

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    print("tqdm library not installed in this system !!! \nyou can install using 'pip install tqdm' this command\n\n")
    exit()

try:
    from css_html_js_minify import js_minify, html_minify, css_minify
except ModuleNotFoundError:
    print("css_html_js_minify library not installed in this system !!! \nyou can install using 'pip install css-html-js-minify' this command\n\n")
    exit()

# minify(text, mangle=True, mangle_toplevel=True)
try:
    from calmjs.parse.unparsers.es5 import minify_print
except ModuleNotFoundError:
    print("'slimit' library not installed in this system !!! \nyou can install using 'pip install slimit' this command\n\n")
    exit()

# Function Example
# [['SITE']['CPU_ARCHITECTURE']
# config_set(['SITE'], 'CPU_ARCHITECTURE', '32')
# config_get(['SITE'], 'CPU_ARCHITECTURE')
try:
    from library.config import config_set, config_get
except ModuleNotFoundError:
    print("'config' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

try:
    from library.hash_maker import main_file_strike, File_Probe, Check_Probe
except ModuleNotFoundError:
    print("'hash_maker' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

try:
    from file_lib.jpeg import mozjpeg, jpegoptim, jpegrescan, jpegtran
except ModuleNotFoundError:
    print("'from file_lib import jpeg' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()


try:
    from file_lib.png import pingo, optipng, advpng, pngout
except ModuleNotFoundError:
    print("'from file_lib png' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

try:
    from file_lib.gif import gifsicle, gifsicle_lossy
except ModuleNotFoundError:
    print("'from file_lib import gif' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()


try:
    from file_lib.svg import svgcleaner
except ModuleNotFoundError:
    print("'from file_lib import extern' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

# if __name__ == '__main__':
#     try:
#         from file_lib.extern import ext_root_set, ext_root_get
#     except ModuleNotFoundError:
#         print("'from file_lib import extern' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
#         exit()

# ------------------------------end------------------------------
