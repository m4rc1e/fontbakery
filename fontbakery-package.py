'''
Font Bakery Package:
~~~~~~~~~~~~~~~~~~~

If upstream source passes Font Bakery, create 'ofl/apache' package for Google
Fonts.

'''

import os
import sys
import argparse
import importlib
fb_check = importlib.import_module("fontbakery-check-ttf")


def main():
    parser = argparse.ArgumentParser(description="Package upstream repo")
    parser.add_argument('source', metavar='s', type=str,
                         help='Add source folder')
    args = parser.parse_args()
    print(args.source)


if __name__ == "__main__":
    main()
