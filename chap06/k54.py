#
# usage: python k54.py {file name}
#

import sys
from xml.etree import ElementTree as ET

if __name__ == '__main__':
    fn = sys.argv[1]

    root = ET.parse(fn).getroot()
    wl = [t.findall('*') for t in root.findall('.//token')]
    wlpl = [[w[0].text, w[1].text, w[4].text] for w in wl]

    for wlp in wlpl:
        print(wlp[0], wlp[1], wlp[2], sep='\t')
