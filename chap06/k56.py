#
# usage: python k56.py {file name}
#

import sys
from xml.etree import ElementTree as ET

def substitute_mentions(sl, cl):
    return [sl[m[0]][:m[1]] + c[0][2] + ['('] + m[2] + [')'] + sl[m[0]][m[1]+len(m[2]):]
            for c in cl for m in c[1:]]

if __name__ == '__main__':
    fn = sys.argv[1]

    root = ET.parse(fn).getroot()
    sl = [[t.find('word').text for t in s.findall('tokens/*')]
            for s in root.find('document/sentences')]
    cl = [[[int(m.find('sentence').text)-1,
            int(m.find('start').text)-1, m.find('text').text.split(' ')] 
                for m in e.findall('mention')]
                for e in root.findall('document/coreference/*')]

    for s in substitute_mentions(sl, cl):
        print(' '.join(s))
