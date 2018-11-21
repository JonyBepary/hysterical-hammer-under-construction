# ----------------------------library----------------------------
import os
from itertools import chain
try:
    from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file
except ModuleNotFoundError:
    print("css_html_js_minify library not installed in this system !!! \nyou can install using 'pip install css-html-js-minify' this command\n\n")
    exit()

# Function Example
# ['JEKYLL']['CPU_ARCHITECTURE']
# config_set('JEKYLL', 'CPU_ARCHITECTURE', '32')
# config_get('JEKYLL', 'CPU_ARCHITECTURE')
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


# ------------------------------end------------------------------



overwrite_var = config_get('JEKYLL', 'overwrite')
if overwrite_var == KeyError:
    raise KeyError
# print("overwrite: ", overwrite_var)


def js_min(file, root):
    path = os.path.join(root, file)
    b_size = os.path.getsize(path)
    process_single_js_file(path, overwrite=overwrite_var)
    status = File_Probe(path)
    a_size = os.path.getsize(path)


def html_min(file, root):
    path = os.path.join(root, file)
    b_size = os.path.getsize(path)
    process_single_html_file(path, overwrite=overwrite_var)
    status = File_Probe(path)
    a_size = os.path.getsize(path)



def css_min(file, root):
    path = os.path.join(root, file)
    b_size = os.path.getsize(path)
    process_single_css_file(path, overwrite=overwrite_var)
    status = File_Probe(path)
    a_size = os.path.getsize(path)
    print("\n")


def raster_min(file, root):
    pass


def vector_min(file, root):
    pass


def autoprefix_min(file, root):
    pass


i = 0
k = 0
j = 0

root_wd = os.getcwd()
sub_dir = config_get("JEKYLL", "target_location")
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

# for root, dirs, files in os.walk(tartget_dir):
for root, dirs, files in chain.from_iterable(os.walk(directory) for directory in tartget_dir):
    for file in files:
        j = j + 1
        path = os.path.join(root, file)
        status = Check_Probe(path)
        if status == "FILE_NOT_MODIFIED":
            i = i + 1
        else:
            if file.endswith(".js"):
                js_min(file, root)
                k = k + 1
            elif file.endswith(".css"):
                css_min(file, root)
                k = k + 1
            elif file.endswith(".html") or file.endswith(".htm"):
                html_min(file, root)
                k = k + 1
print("total: {}, modified: {}, not modified{}".format(j, k, i))



















# def function():
#     # for root, dirs, files in os.walk(tartget_dir):
#     for root, dirs, files in chain.from_iterable(os.walk(directory) for directory in tartget_dir):
#         for file in files:
#             j = j + 1
#             path = os.path.join(root, file)
#             status = File_Probe(path)
#             if status == "FILE_NOT_MODIFIED":
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
