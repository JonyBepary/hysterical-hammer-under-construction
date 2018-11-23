try:
    import extern
except ModuleNotFoundError:
    from picopt import extern
    pass



class Settings(object):
    """Global settings class."""
    force = True
    quality = 90
    advpng = False
    archive_name = None
    bigger = False
    comics = False
    destroy_metadata = True
    follow_symlinks = True
    formats = set()
    gifsicle = True
    jpegrescan = False
    jpegrescan_multithread = False
    jpegtran = True
    jpegtran_prog = True
    list_only = False
    mozjpeg = False
    optimize_after = None
    optipng = True
    paths = set()
    pngout = True
    record_timestamp = False
    recurse = False
    test = False
    to_png_formats = set()
    verbose = 1
