#
# usage: python k59.py {file name} {number}
#

import sys
import re
from xml.etree import ElementTree as ET

def get_np(pl):
    def np_list(s):
        l, r1, r2 = [], re.compile('\(NP(.+)'), re.compile('\(\S*\s*|\)')
        m = r1.search(s)
        while m:
            t, d = '', 0
            for c in list(m.group()):
                if c == '(':
                    d += 1
                elif c == ')':
                    d -= 1
                t += c
                if d == 0:
                    break
            l.append(r2.sub('', t))
            m = r1.search(m.group(1))
        return l
    return [np_list(p) for p in pl]

if __name__ == '__main__':
    fn = sys.argv[1]

    root = ET.parse(fn).getroot()
    pl = [p.text for p in root.findall('.//parse')]

    for npl in get_np(pl):
        for np in npl:
            print(np)
