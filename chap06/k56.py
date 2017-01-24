#
# usage: python k56.py {file name}
#

import sys
from xml.etree import ElementTree as ET

def substitute_mentions(sl, cl):
    for c in cl:
        rm = c[0][2]
        for m in c[1:]:
            l, r, tm = sl[m[0]][:m[1]], sl[m[0]][m[1]:], m[2]
            r = ' '.join(r).replace(tm, rm + ' (' + tm + ')').split(' ')
            sl[m[0]] = l + r
    return sl

if __name__ == '__main__':
    fn = sys.argv[1]

    root = ET.parse(fn).getroot()
    sl = [[t.find('word').text for t in s.findall('tokens/*')]
            for s in root.find('./document/sentences')]
    cl = [[[int(m.find('sentence').text)-1,
            int(m.find('start').text)-1, m.find('text').text] 
                for m in e.findall('mention')]
                for e in root.findall('document/coreference/*')]

    for s in substitute_mentions(sl, cl):
        print(' '.join(s))
