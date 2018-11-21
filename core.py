# ----------------------------library----------------------------
import os
from itertools import chain
try:
    from css_html_js_minify import js_minify, html_minify, css_minify
except ModuleNotFoundError:
    print("css_html_js_minify library not installed in this system !!! \nyou can install using 'pip install css-html-js-minify' this command\n\n")
    exit()

# minify(text, mangle=True, mangle_toplevel=True)
try:
    from slimit import minify
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
    from picopt.jpeg import mozjpeg, jpegoptim, jpegrescan, jpegtran
except ModuleNotFoundError:
    print("'from picopt import jpeg' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()


try:
    from picopt.png import pingo, optipng, advpng, pngout
except ModuleNotFoundError:
    print("'from picopt png' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

try:
    from picopt.gif import gifsicle, gifsicle_lossy
except ModuleNotFoundError:
    print("'from picopt import gif' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

try:
    from picopt.extern import ext_root_set, ext_root_get
except ModuleNotFoundError:
    print("'from picopt import extern' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

try:
    from picopt.svg import svgcleaner
except ModuleNotFoundError:
    print("'from picopt import extern' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

# ------------------------------end------------------------------


root_wd = os.getcwd()
ext_root_set(root_wd)


file_config = os.path.join(os.getcwd(), '_config.ini')
# print(file_config)
if os.path.isfile(file_config) != True:
    pass
else:
    overwrite_var = config_get('SITE', 'overwrite', file_config)
    # print(overwrite_var)
# exit()
if overwrite_var == KeyError:
    raise KeyError
# print("overwrite: ", overwrite_var)


def js_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)
    print('path: ', path)
    b_size = os.path.getsize(path)
    with open(path, 'r') as fp:
        text = fp.read()
        fp.close()
    try:
        text = minify(text, mangle=True, mangle_toplevel=True)
    except Exception as e:
        print("A Exception '{}' So try running in 'css_html_js_minify' \n".format(e))
        text = js_minify(text)

    with open(path, 'w') as fp:
        fp.write(text)
        fp.close()
    a_size = os.path.getsize(path)


def html_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)
    b_size = os.path.getsize(path)
    with open(path, 'r') as fp:
        text = fp.read()
        fp.close()
    try:
        text = html_minify(text)
    except Exception as e:
        print("A Exception '{}' occured\n".format(e))
        pass
    with open(path, 'w') as fp:
        fp.write(text)
        fp.close()

    a_size = os.path.getsize(path)


def css_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)
    b_size = os.path.getsize(path)

    with open(path, 'r') as fp:
        text = fp.read()
        fp.close()
    try:
        text = css_minify(text)
    except Exception as e:
        print("A Exception '{}' occured\n".format(e))
        pass
    with open(path, 'w') as fp:
        fp.write(text)
        fp.close()
    a_size = os.path.getsize(path)
    print("\n")


def jpeg_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)
    jpeg_program = config_get('IMAGE', 'jpg_program')
    # print(jpeg_program)
    if jpeg_program == 'jpegoptim':
        jpeg_quality = config_get('IMAGE', 'jpgoptim_quality')
        print("jpeg_program: ", jpeg_program, "jpgoptim_quality: ", jpeg_quality)
        jpegoptim(file, jpeg_quality)
    elif jpeg_program == 'jpegtran':
        print("jpeg_program: ", jpeg_program, "jpgoptim_quality: ", jpeg_quality)
        jpegtran(file, jpeg_quality)
    elif jpeg_program == 'jpegrescan':
        print("jpeg_program: ", jpeg_program, "jpgoptim_quality: ", jpeg_quality)
        jpegrescan(file, jpeg_quality)
    elif jpeg_program == 'jpegoptim':
        print("jpeg_program: ", jpeg_program, "jpgoptim_quality: ", jpeg_quality)
        jpegoptim(file, jpeg_quality, root)
    return 0


def png_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)
    png_program = config_get('IMAGE', 'png_program')
    # print(png_program)
    if png_program == 'pingo':
        print("png_program: ", png_program)
        pingo(file, root)
    elif png_program == 'pngout':
        # print("png_program: ", png_program)
        pngout(file, root)
    elif png_program == 'optipng':
        # print("png_program: ", png_program)
        optipng(file, root)
    elif png_program == 'advpng':
        # print("png_program: ", png_program)
        advpng(file, root)
    return 0


def gif_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)

    gif_program = config_get('IMAGE', 'gif_program')
    print(gif_program)
    if gif_program == 'gifsicle_lossy':
        print("gif_program: ", gif_program)
        gifsicle_lossy(file, root)
    elif gif_program == 'gifsicle':
        print("gif_program: ", gif_program)
        gifsicle(file, root)
    return 0



def svg_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)

    svg_program = config_get('IMAGE', 'svg_progran')
    print(svg_program)
    if svg_program == 'svgcleaner':
        print("svg_program: ", svg_program)
        svgcleaner(file, root)
    return 0


def autoprefix_min(file, root=None):
    pass


'''--- maybe i'll move this to main.py ---'''
sub_dir = config_get("SITE", "target_location")
tartget_dir = list()
if "," in sub_dir:
    sub_dir = sub_dir.split(', ')
    # print("True: ", type(sub_dir))
    for i, t_dir in enumerate(sub_dir):
        tartget_dir.insert(i, os.path.join(os.getcwd(), t_dir))
    print("tartget_dir:", tartget_dir)
else:
    tartget_dir.insert(0, os.path.join(os.getcwd(), sub_dir))
    print("tartget_dir:", tartget_dir)

    '''---end---'''


'''---maybe this too---'''


def controller():
    i = 0
    k = 0
    j = 0
    for root, dirs, files in chain.from_iterable(os.walk(directory) for directory in tartget_dir):
        for file in files:
            # print('root: ', root, 'file: ', file)
            j = j + 1
            path = os.path.join(root, file)
            status = Check_Probe(path)
            if status == "FILE_NOT_MODIFIED":
                i = i + 1
            else:
                if file.endswith(".js"):
                    js_min(file, root)
                    k = k + 1
                    File_Probe(path)
                elif file.endswith(".css"):
                    css_min(file, root)
                    k = k + 1
                    File_Probe(path)
                elif file.endswith(".html") or file.endswith(".htm"):
                    html_min(file, root)
                    k = k + 1
                    File_Probe(path)
                elif file.endswith('.jpg') or file.endswith('.jpeg'):
                    jpeg_min(file, root)
                    k = k + 1
                    File_Probe(path)
                elif file.endswith('.png') or file.endswith('.pnm'):
                    png_min(file, root)
                    k = k + 1
                    File_Probe(path)
                elif file.endswith('.gif'):
                    gif_min(file, root)
                    k = k + 1
                    File_Probe(path)
                elif file.endswith(".svg"):
                    # print("svg file: ", file)
                    svg_min(file, root)
                    k = k + 1
                    File_Probe(path)
    print("total: {}, modified: {}, not modified{}".format(j, k, i))


print('start')
# raster_min('JHON.png', root_wd)
# controller()


controller()










# def function():
#     # for root, dirs, files in os.walk(tartget_dir):
#     for root, dirs, files in chain.from_iterable(os.walk(directory) for directory in tartget_dir):
#         for file in files:
#             j = j + 1
#             path = os.path.join(root, file)
#             if 0 == "FILE_NOT_MODIFIED":
#                 i = i + 1
#             else:
#                 if file.endswith(".js"):
#                     js_min(file, root)
#                     k = k + 1
#                 elif file.endswith(".css"):
#                     css_min(file, root)
#                     k = k + 1
#                 elif file.endswith(".html") or file.endswith(".htm"):
#                     html_min(file, root)
#                     k = k + 1
#     print("total: {}, modified: {}, not modified{}".format(j, k, i))
