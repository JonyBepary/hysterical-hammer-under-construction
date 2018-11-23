"""JPEG format."""
from __future__ import absolute_import, division, print_function

import copy
try:
    from settings import Settings
except ModuleNotFoundError:
    from file_lib.settings import Settings

try:
    import extern
except ModuleNotFoundError:
    from file_lib import extern
    pass

_JPEG_FORMAT = 'JPEG'
FORMATS = set([_JPEG_FORMAT])
OUT_EXT = '.jpg'

_MOZJPEG_ARGS = ['jpegtran', '-optimize']
_JPEGOPTIM_ARGS = ['jpegoptim']
_JPEGTRAN_ARGS = ['jpegtran', '-optimize']
_JPEGRESCAN_ARGS = ['jpegrescan']


test = False

filename = 'jhone.jpg'
new_filename = 'jhone.jpg'



def mozjpeg(ext_args, root=None):
    """Create argument list for mozjpeg."""
    args = copy.copy(_MOZJPEG_ARGS)
    if Settings.destroy_metadata:
        args += ["-copy", "none"]
    else:
        args += ["-copy", "all"]
    if Settings.jpegtran_prog:
        args += ["-progressive"]

    args += ['-outfile']
    args += [ext_args.new_filename, ext_args.old_filename]
    if test:
        print("mozjpeg: ", args)
        return 0

    extern.run_ext(args, root)
    return _JPEG_FORMAT


def jpegoptim(filename, quality=None, root=None):
    # jpegoptim - s - f - o - -all - progressive . / test.png
    """Create argument list for jpegtran."""
    args = copy.copy(_JPEGOPTIM_ARGS)
    if Settings.destroy_metadata:
        args += ["-s"]
    if Settings.force:
        args += ["-f"]
    if Settings.verbose:
        args += ["-v"]
    if quality:
        args += ["-m {}".format(quality)]
    if Settings.jpegtran_prog:
        args += ["--all-progressive"]

    args += [filename]
    if test:
        print("jpegoptim: ", args)
        return 0

    extern.run_ext(args, root)
    return _JPEG_FORMAT


def jpegtran(ext_args, root=None):
    """Create argument list for jpegtran."""
    args = copy.copy(_JPEGTRAN_ARGS)
    if Settings.destroy_metadata:
        args += ["-copy", "none"]
    else:
        args += ["-copy", "all"]
    if Settings.jpegtran_prog:
        args += ["-progressive"]
    args += ['-outfile']
    args += [ext_args.new_filename, ext_args.old_filename]
    if test:
        print("jpegtran: ", args)
        return 0

    extern.run_ext(args, root)
    return _JPEG_FORMAT


_JPEGRESCAN_ARGS = ['jpegrescan']


def jpegrescan(ext_args, root=None):
    """Run the EXTERNAL program jpegrescan."""
    args = copy.copy(_JPEGRESCAN_ARGS)
    if Settings.jpegrescan_multithread:
        args += ['-t']
    if Settings.destroy_metadata:
        args += ['-s']
    args += [ext_args.old_filename, ext_args.new_filename]
    if test:
        print("jpegrescan: ", args)
        return 0

    extern.run_ext(args, root)
    return _JPEG_FORMAT
