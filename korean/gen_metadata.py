"""
Batch generate METADATA.pb file in korean repos
"""
import subprocess


families = [
    'ofl/blackandwhitepicture',
    'ofl/cutefont',
    'ofl/daehanmingukdokdo',
    'ofl/dohyeon',
    'ofl/dohyeon/bmdohyeon',
    'ofl/gaegu',
    'ofl/gaegu',
    'ofl/gaegu',
    'ofl/gamjaflower',
    'ofl/gothica1',
    'ofl/hanna',
    'ofl/hanna',
    'ofl/himelody',
    'ofl/jua',
    'ofl/jua/bmjua',
    'ofl/kiranghaerang',
    'ofl/kiranghaerang/bmkiranghaerang',
    'ofl/nanumbrushscript',
    'ofl/nanumgothic',
    'ofl/nanumgothic',
    'ofl/nanumgothic',
    'ofl/nanummyeongjo',
    'ofl/nanummyeongjo',
    'ofl/nanummyeongjo',
    'ofl/poorstory',
    'ofl/singleday',
    'ofl/songmyung',
    'ofl/stylish',
    'ofl/sunflower',
    'ofl/sunflower',
    'ofl/sunflower',
    'ofl/yeonsung',
]

FONTS_DIR = '/Users/marc/Documents/googlefonts/fonts'
ADD_FONT_DIR = '/Users/marc/Documents/googlefonts/tools'

import os

os.chdir(ADD_FONT_DIR)

py_script = os.path.join(ADD_FONT_DIR, 'bin', 'gftools-add-font.py')

for family in families:
    family_dir = os.path.join(FONTS_DIR, family)
    subprocess.call(['python', py_script, '--update', family_dir])