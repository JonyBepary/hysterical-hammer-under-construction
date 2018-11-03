from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file, html_minify, js_minify, css_minify
import os
overwrite_var = True

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".js"):
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

        if file.endswith(".html"):
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

        if file.endswith(".css"):
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
