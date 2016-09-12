#!/usr/bin/env python
# coding: utf-8

'''
Font Bakery Package:
~~~~~~~~~~~~~~~~~~~

If upstream source folder passes Font Bakery, create 'ofl/apache' package
for Google Fonts.

Current upstream repos have the following structure:

├── AUTHORS.txt
├── CONTRIBUTORS.txt
├── DESCRIPTION.en_us.html
├── OFL.txt 
├── README.md 
├── fonts
│   ├── MavenPro-Black.ttf
│   ├── MavenPro-Bold.ttf
│   ├── MavenPro-Medium.ttf
│   └── MavenPro-Regular.ttf
└── sources 
    ├── MavenPro.glyphs 
    └── build
        └── instances.yml

Which will be converted to:

├── MavenPro-Black.ttf
├── MavenPro-Bold.ttf
├── MavenPro-Medium.ttf
├── MavenPro-Regular.ttf
├── DESCRIPTION.en_us.html
├── FONTLOG.txt
├── METADATA.pb
└── OFL.txt

METADATA.pb will be generated as well.

'''

import os
import sys
import shutil
import argparse
import importlib
import glob
import add_font
from google.protobuf import text_format
fb_check = importlib.import_module("fontbakery-check-ttf")


def getFile(path, f):
    try:
        return os.path.join(path, f)
    except IOError:
        print('ERROR: File %s does not exist' % f)
        return


def main(path):

    font_files = glob.glob(os.path.join(path, 'fonts/*.ttf'))
    if not font_files:
        font_files = glob.glob(os.path.join(path, 'fonts', 'ttf/*.ttf'))
    else:
        print('No font sources found, should be at fonts/*.ttf or fonts/ttf/*.ttf')
        return

    description_file = getFile(path, 'DESCRIPTION.en_us.html')
    meta_file = getFile(path, 'METADATA.pb')
    ofl_file = getFile(path, 'OFL.txt')

    # Create package from font name
    pkg_name = os.path.basename(os.path.normpath(font_files[0]))
    # Lobster-Regular.ttf -> lobster
    pkg_name = pkg_name.split('-')[0].lower()
    if not os.path.exists(os.path.join(path, pkg_name)):
        os.makedirs(os.path.join(path, pkg_name))

    ship_repo = os.path.join(path, pkg_name)

    # Copy font files into our ship repo
    for font in font_files:
        shutil.copy(font, ship_repo)

    # copy txt_file into our ship repo
    shutil.copy(description_file, ship_repo)
    shutil.copy(ofl_file, ship_repo)

    # Generate METADATA.pb
    metadata = add_font._MakeMetadata(ship_repo)
    text_proto = text_format.MessageToString(metadata)
    add_font._WriteTextFile(os.path.join(ship_repo, 'METADATA.pb'), text_proto)

    # Check with Fontbakery
    pass
    print ('done')



    # # Load gitignore file, if it doesn't exist, create one
    # try:
    #     gitignore_file = open(os.path.join(path, '.gitignore'))
    # except IOError:
    #     print('No .gitignore file! creating a new one now')
    #     gitignore_file = open('.gitignore', 'w')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Package upstream repo")
    parser.add_argument('source', metavar='s', type=str,
                        help='Add source folder')
    args = parser.parse_args()
    main(args.source)
