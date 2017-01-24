#
# usage: python k53.py {file name}
#

import sys
from xml.etree import ElementTree as ET

if __name__ == '__main__':
    fn = sys.argv[1]

    root = ET.parse(fn).getroot()
    wl = root.findall('.//word')

    for w in wl:
        print(w.text)
