"""of hysterical hammer
function:
controller(), tartget_dir_func()
js_min(), html_min(),
css_min(), jpeg_min(),
png_min(), gif_min(),
svg_min(), autoprefix_min(),
"""

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

if __name__ == '__main__':
    root_wd = os.getcwd()
    # ext_root_set(root_wd)


file_config = os.path.join(os.getcwd(), '_config.ini')
# print(file_config)
# if os.path.isfile(file_config) != True:
#     overwrite = True
# else:
#     overwrite_var = config_get('SITE', 'overwrite', file_config)
#     if overwrite_var == KeyError:
#         raise KeyError
# print(overwrite_var)
# exit()
# print("overwrite: ", overwrite_var)


def tartget_dir_func(wd):
    print(type(wd))
    sub_dir = config_get("SITE", "target_location", wd)
    # print(sub_dir, ":", type(sub_dir))
    tartget_dir = list()
    # if "," in sub_dir:
    if False:
        pass
        sub_dir = sub_dir.split(', ')
        # print("True: ", type(sub_dir))
        for i, t_dir in enumerate(sub_dir):
            tartget_dir.insert(i, os.path.join(wd, t_dir))
        # print("tartget_dir:", tartget_dir)
        return tartgt_dir
    else:
        tartget_dir.insert(0, os.path.join(wd, sub_dir))
        print("from core tartget_dir:", tartget_dir)
        return tartget_dir


def ext_manange_text(status, file, path, root=None):
    if file.endswith(".js"):
        js_min(file, root)
        return File_Probe(path)
    elif file.endswith(".css"):
        css_min(file, root)
        return File_Probe(path)
    elif file.endswith(".html") or file.endswith(".htm"):
        html_min(file, root)
        return File_Probe(path)
    else:
        return ModuleNotFoundError


def ext_manange_binary(status, file, path, root=None):
    if file.endswith('.jpg') or file.endswith('.jpeg'):
        jpeg_min(file, root)
        return File_Probe(path)
    elif file.endswith('.png') or file.endswith('.pnm'):
        png_min(file, root)
        return File_Probe(path)
    elif file.endswith('.gif'):
        gif_min(file, root)
        return File_Probe(path)
    elif file.endswith(".svg"):
        # print("svg file: ", file)
        svg_min(file, root)
        return File_Probe(path)
    else:
        return ModuleNotFoundError


def ext_manange(cmd, status, file, path, root=None):
    # print('cmd: ', cmd)

    if status == "FILE_NOT_MODIFIED":
        return "FILE_NOT_MODIFIED"
    else:
        if cmd == 'all' or cmd == None:
            # print('success!!!')
            reb = ext_manange_binary(status, file, path, root)
            if reb == ModuleNotFoundError:
                ret = ext_manange_text(status, file, path, root)
                if ret == ModuleNotFoundError:
                    # add unsupported file to bd
                    # return File_Probe(path)
                    pass
                    return ret
                else:
                    return ret
                return reb
            else:
                return reb

        elif cmd == 'b':
            return ext_manange_binary(status, file, path, root)
        elif cmd == 't':
            return ext_manange_text(status, file, path, root)
        # print("total: {}, modified: {}, not modified{}".format(j, k, i))



def js_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)
    # print('path: ', path)
    b_size = os.path.getsize(path)
    with open(path, 'r') as fp:
        text = fp.read()
        fp.close()
    try:
        text = minify_print(file)
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
    # print("\n")


def jpeg_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)
    jpeg_program = config_get('IMAGE', 'jpg_program')
    # print(jpeg_program)
    if jpeg_program == 'jpegoptim':
        jpeg_quality = config_get('IMAGE', 'jpgoptim_quality')
        # print("jpeg_program: ", jpeg_program, "jpgoptim_quality: ", jpeg_quality)
        jpegoptim(file, jpeg_quality)
    elif jpeg_program == 'jpegtran':
        # print("jpeg_program: ", jpeg_program, "jpgoptim_quality: ", jpeg_quality)
        jpegtran(file, jpeg_quality)
    elif jpeg_program == 'jpegrescan':
        # print("jpeg_program: ", jpeg_program, "jpgoptim_quality: ", jpeg_quality)
        jpegrescan(file, jpeg_quality)
    elif jpeg_program == 'jpegoptim':
        # print("jpeg_program: ", jpeg_program, "jpgoptim_quality: ", jpeg_quality)
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
        # print("png_program: ", png_program)
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
    # print(gif_program)
    if gif_program == 'gifsicle_lossy':
        # print("gif_program: ", gif_program)
        gifsicle_lossy(file, root)
    elif gif_program == 'gifsicle':
        # print("gif_program: ", gif_program)
        gifsicle(file, root)
    return 0



def svg_min(file, root=None):
    if root != None:
        path = os.path.join(root, file)
    else:
        path = os.path.join(os.getcwd(), file)

    svg_program = config_get('IMAGE', 'svg_progran')
    # print(svg_program)
    if svg_program == 'svgcleaner':
        # print("svg_program: ", svg_program)
        svgcleaner(file, root)
    return 0


def autoprefix_min(file, root=None):
    pass




'''---maybe this too---'''


def controller(main_dir=None, cmd=None):
    print('main_dir: ', main_dir, 'type: ', type(main_dir))
    if __name__ == '__main__':
        if main_dir == None:
            t_dir = tartget_dir_func(os.getcwd())
        else:
            t_dir = tartget_dir_func(main_dir)
        # '/home/jony/blog/HardCandy-Jekyll-master'
    else:
        if main_dir == None:
            t_dir = tartget_dir_func(os.getcwd())
        else:
            t_dir = tartget_dir_func(main_dir)
    print(t_dir, ':', t_dir)

    i = 0
    return 0
    for root, dirs, files in chain.from_iterable(os.walk(directory) for directory in t_dir):
        if i == 20:
            break
        for file in files:
            print('root: ', root, 'file: ', file)
            i = i + 1
            path = os.path.join(root, file)
            print('path: ', path)
            status = Check_Probe(path)
            ext_manange(cmd, status, file, path, root)



# print('start')
# raster_min('JHON.png', root_wd)
# controller()



if __name__ == '__main__':
    controller(os.getcwd())
