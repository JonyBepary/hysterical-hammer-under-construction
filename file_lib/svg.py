"""SVG format."""
import copy
try:
    import extern
except ModuleNotFoundError:
    from file_lib import extern
    pass

_SVG_FORMAT = 'SVG'
FORMATS = set([_SVG_FORMAT])
_SVGCLEANER_ARGS = ['svgcleaner']

test = False

# filename = 'jhone.jpg'
# new_filename = 'jhone.jpg'



def svgcleaner(filename, root=None):
    """Create argument list for mozSVG."""
    args = copy.copy(_SVGCLEANER_ARGS)
    args += [filename, filename]
    if test:
        # print("SVGCLEANER ARGS: ", args)
        return 0
    if root == None:
        extern.run_ext(args)
    else:
        extern.run_ext(args, root)
    return _SVG_FORMAT
