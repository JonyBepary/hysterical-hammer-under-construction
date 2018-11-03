from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file
import os




















# from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file, html_minify, js_minify, css_minify
# import re
# import sys
# # from sys import getsizeof


# def removeComments(string):
#     # remove all occurance streamed comments (/*COMMENT */) from string
#     string = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", string)

#     # remove all occurance singleline comments (//COMMENT\n ) from string
#     string = re.sub(re.compile("//.*?\n"), "", string)

#     return string


# # process_single_html_file('test.htm', overwrite=False)
# # # 'test.html'
# # process_single_js_file('test.js', overwrite=False)
# # # 'test.min.js'
# # process_single_css_file('test.css', overwrite=False)

# with open("main.js", "r") as fp:
#     text = fp.readlines()

# fp.close()

# for x in range(len(text)):
#     # print(text[x])
#     text[x] = removeComments(text[x])

# string = "".join(text)
# string = string.replace("\n", "")
# string = html_minify(string)

# with open("new_main.js", "w") as f:
#     f.write(string)
# f.close()
