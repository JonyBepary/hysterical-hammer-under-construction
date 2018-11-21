from css_html_js_minify import html_minify
import os
path = os.path.join(os.getcwd(), 'assets/htm/index.html')

with open(path, 'r') as fp:
    text = fp.read()
    fp.close()
try:
    text = html_minify(text)
except Exception as e:
    print("A Exception '{}' occured\n".format(e))

with open(path, 'w') as fp:
    fp.write(text)
    fp.close()

print('start: \n', text)
print('\n\n\nend: \n', text)
