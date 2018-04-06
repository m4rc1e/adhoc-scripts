# -*- coding: utf-8 -*-
"""
Change Heavy styles to Black to conform with GF API
"""
import os
from fontTools.ttLib import TTFont
import shutil

def get_files(path, file_type='ttf'):
    files = []
    for f in os.listdir(path):
        if f.endswith(file_type):
            file_path = os.path.join(path, f)
            files.append(file_path)
    return files


def main():
    fonts_paths = get_files('/Users/marc/Downloads/Google_Korean-3/fix')

    for path in fonts_paths:
        font = TTFont(path)

        for record in font['name'].names:
            if 'Heavy' in record.toUnicode():
                text = record.toUnicode()
                text = text.replace('Heavy', 'Black')
                text = text.replace('Black Black', 'Black')
                record.string = text
                font.save(path + '.fix')
                os.remove(path)
                os.rename(path + '.fix', path)
            # if 'UltaLight' in record.toUnicode():
            #     print record.toUnicode()

if __name__ == '__main__':
    main()
