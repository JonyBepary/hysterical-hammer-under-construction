import os
from file_lib import extern
from file_lib import jpeg

filename = 'jhone.jpg'
new_filename = 'jhone.jpg'

filename_on, ext_on = os.path.splitext(filename)
print(filename_on, ext_on)

ext_args = extern.ExtArgs(filename, new_filename)

# _MOZJPEG_ARGS = ['jpegtran', '-optimize']
# def mozjpeg(ext_args):
# mozjpeg:  ['jpegtran', '-optimize', '-copy', 'none', '-progressive', '-outfile', 'jhone.jpg', 'jhone.jpg']

jpeg.mozjpeg(ext_args)


# def jpegoptim(ext_args, quality=None):
#jpegoptim:  ['jpegoptim', '-s', '-f', '-v', '-m 90', '--all-progressive', 'jhone.jpg']
jpeg.jpegoptim(ext_args, 90)



# _JPEGTRAN_ARGS = [jpegtran', '-optimize']
# def jpegtran(ext_args):
# jpegtran:  ['jpegtran', '-optimize', '-copy', 'none', '-progressive', '-outfile', 'jhone.jpg', 'jhone.jpg']


jpeg.jpegtran(ext_args)



# _JPEGRESCAN_ARGS = ['jpegrescan']
# def jpegrescan(ext_args):
# ['jpegrescan', '-s', 'jhone.jpg', 'jhone.jpg']


jpeg.jpegrescan(ext_args)
