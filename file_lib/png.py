"""PNG format."""
try:
    import extern
except ModuleNotFoundError:
    from file_lib import extern

_PNG_FORMAT = 'PNG'
FORMATS = set([_PNG_FORMAT])
LOSSLESS_FORMATS = set(('PNM', 'PPM', 'BMP', 'GIF'))
CONVERTABLE_FORMATS = LOSSLESS_FORMATS | FORMATS
OUT_EXT = '.' + _PNG_FORMAT.lower()
_PINFGO_ARGS = ['pingo', '-pngpalette=100', '-s9', 'test2.png']
_OPTIPNG_ARGS = ['optipng', '-o6', '-fix', '-preserve', '-force', '-quiet']
_ADVPNG_ARGS = ['advpng', '-z', '-4', '-f']
_PNGOUT_ARGS = ['pngout', '-force', '-v']


def pingo(file, root=None):
    """Run the external program pingo on the file."""
    args = _PINFGO_ARGS + [file]
    extern.run_ext(args, root)
    return _PNG_FORMAT


def optipng(file, root=None):
    """Run the external program optipng on the file."""
    args = _OPTIPNG_ARGS + [file]
    extern.run_ext(args, root)
    return _PNG_FORMAT


def advpng(file, root=None):
    """Run the external program advpng on the file."""
    args = _ADVPNG_ARGS + [file]
    extern.run_ext(args, root)
    return _PNG_FORMAT


def pngout(file, root=None):
    """Run the external program pngout on the file."""
    args = _PNGOUT_ARGS + [file]
    extern.run_ext(args, root)
    return _PNG_FORMAT
