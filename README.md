# hysterical-hammer
hysterical-hammer is tool for optimize (html, css, js) code and (png, jpg, gif, svg) media in "Jekyll Blog", "Ghost Blog" or any "Static Site" and many more.

USED:
xxhash (for FIC)
css_html_js_minify (for css ,html ,js)
pillow
rarfile
library from piopt (for raster)

mozjpeg / libjpeg-turbo (jpeg enocoder)
jpegtran / jpegrescan / jpegoptim (enocoding tool)
gifscale/Gfycat (for GIF)
optipng / advpng / pngout (for png)

##Under Contruction



instlation of jpegoptim
git clone https://github.com/tjko/jpegoptim.git
cd jpegoptim.git
./configure CPPFLAGS=-I/opt/mozjpeg/include LDFLAGS=-L/opt/mozjpeg/lib
make
sudo make install




    svgcleaner [FLAGS] [OPTIONS] <in-file> <out-file>

     can contain values: true, false, yes, no, y, n

EXAMPLES:
    clean a file with default options:
    svgcleaner in.svg out.svg

    clean a file with custom options:
    svgcleaner --indent=2 --paths-coordinates-precision=5 --join-arcto-flags=yes in.svg out.svg

    clean a file without default options:
    svgcleaner --no-defaults --remove-comments=yes in.svg out.svg

    clean a stream using UNIX pipes:
    cat in.svg | svgcleaner -c - > out.svg



svgcleaner madara2.svg madara1.svg --remove-comments --remove-declarations --remove-nonsvg-elements --remove-unused-defs --convert-shapes --remove-title --remove-desc --remove-metadata --remove-dupl-lineargradient --remove-dupl-radialgradient --remove-dupl-fegaussianblur --ungroup-groups --ungroup-defs --remove-invalid-stops --remove-version --remove-nonsvg-attributes --remove-text-attributes --remove-unused-coordinates --remove-default-attributes --remove-xmlns-xlink-attribute --remove-needless-attributes --paths-to-relative --remove-unused-segments --convert-segments --apply-transform-to-paths --trim-paths --join-arcto-flags --remove-dupl-cmd-in-paths --use-implicit-cmds --simplify-transforms
