try:
    from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file
except ModuleNotFoundError:
    print("css_html_js_minify library not installed in this system !!! \nyou can install using 'pip install css-html-js-minify' this command\n\n")
    exit()

try:
    from library.hash_maker import main_file_strike, File_Probe
except ModuleNotFoundError:
    print("'hash_maker' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
    exit()

import os

overwrite_var = True



def js_min(file, root):
    # print(os.path.join(root, file))
    path = os.path.join(root, file)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print(path, "\n")
    b_size = os.path.getsize(path)
    process_single_js_file(path, overwrite=overwrite_var)
    # print("\n")
    a_size = os.path.getsize(path)
    # print("before: {0} => after: {1}".format(b_size, a_size))
    # print("\n")


def html_min(file, root):
    # print(os.path.join(root, file))
    path = os.path.join(root, file)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print(path, "\n")
    b_size = os.path.getsize(path)
    process_single_html_file(path, overwrite=overwrite_var)
    # print("\n")
    a_size = os.path.getsize(path)
    # print("before: {0} => after: {1}".format(b_size, a_size))
    # print("\n")


def css_min(file, root):
    # print(os.path.join(root, file))
    path = os.path.join(root, file)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print(path, "\n")
    b_size = os.path.getsize(path)
    process_single_css_file(path, overwrite=overwrite_var)
    # print("\n")
    a_size = os.path.getsize(path)
    # print("before: {0} => after: {1}".format(b_size, a_size))
    print("\n")


def raster_min(file, root):
    pass


def vector_min(file, root):
    pass


def autoprefix_min(file, root):
    pass


root_wd = os.getcwd()
tartget_dir = os.path.join(os.getcwd(), "assets")
print("tartget_dir:", tartget_dir)
i = 0
k = 0
j = 0
for root, dirs, files in os.walk(tartget_dir):
    for file in files:
        j = j + 1
        path = os.path.join(root, file)
        status = File_Probe(path)
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
