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

'''

import os
import sys
import argparse
import importlib
import glob
fb_check = importlib.import_module("fontbakery-check-ttf")


def main(path):
    fonts = glob.glob(os.path.join(path, 'fonts/*.ttf'))
    if not fonts:
        fonts = glob.glob(os.path.join(path, 'fonts', 'ttf/*.ttf'))
    print(fonts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Package upstream repo")
    parser.add_argument('source', metavar='s', type=str,
                         help='Add source folder')
    args = parser.parse_args()
    main(args.source)
