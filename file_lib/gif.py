"""Gif Optimizer."""
from __future__ import absolute_import, division, print_function

try:
    import extern
except ModuleNotFoundError:
    from file_lib import extern

SEQUENCED_TEMPLATE = '{} SEQUENCED'
_GIF_FORMAT = 'GIF'
FORMATS = set([SEQUENCED_TEMPLATE.format(_GIF_FORMAT), _GIF_FORMAT])
OUT_EXT = '.' + _GIF_FORMAT.lower()

_GIFSICLE_ARGS = ['gifsicle', '--optimize=3']




def gifsicle(file, root=None):
    """Run the EXTERNAL program gifsicle."""
    args = _GIFSICLE_ARGS + [file]
    args = args + ['-o']
    args = args + [file]
    extern.run_ext(args, root)
    return _GIF_FORMAT


def gifsicle_lossy(file, root=None):
    """Run the EXTERNAL program gifsicle."""
    args = _GIFSICLE_ARGS + ['--lossy=80']
    args = args + [file]
    args = args + ['-o']
    args = args + [file]
    extern.run_ext(args, root)
    return _GIF_FORMAT


# gifsicle_lossy('jony.gif')
PROGRAMS = (gifsicle)
BEST_ONLY = True
