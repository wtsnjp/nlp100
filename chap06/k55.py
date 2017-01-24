#
# usage: python k55.py {file name}
#

import sys
from xml.etree import ElementTree as ET

if __name__ == '__main__':
    fn = sys.argv[1]

    root = ET.parse(fn).getroot()
    wl = [t.findall('./*') for t in root.findall('.//token')]
    pl = [w[0].text for w in wl if w[5].text == 'PERSON']

    for p in pl:
        print(p)
