"""
Copy a name table from a font to another font
"""
import os
import shutil
from os.path import basename
from glob import glob
from fontTools.ttLib import TTFont


def main():

    fonts_from = {basename(f): f for f in glob('/Users/marc/Downloads/Nanum_Brush_Script-2/*.ttf')}
    fonts_to = {basename(f): f for f in glob('/Users/marc/Documents/googlefonts/fonts/ofl/nanumbrushscript/*.ttf')}

    for font in fonts_to:
        ttfont_to = TTFont(fonts_to[font])
        ttfont_from = TTFont(fonts_from[font])

        ttfont_to['name'] = ttfont_from['name']

        new_filename = fonts_to[font] + '.fix'
        ttfont_to.save(new_filename)
        os.remove(fonts_to[font])
        shutil.move(new_filename, fonts_to[font])
        print 'saved {}'.format(fonts_to[font])


if __name__ == '__main__':
    main()