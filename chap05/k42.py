#
# usage: python k42.py {file name}
#

import sys
from k41 import *

def get_relation_pairs(sl):
    pl = []
    for s in sl:
        for c in s:
            if c.dst != -1 and c.dst < len(s):
                a, b = '', ''
                for v in c.morphs:
                    if v.pos != '記号':
                        a += v.surface
                for v in s[c.dst].morphs:
                    if v.pos != '記号':
                        b += v.surface
                if a != '' and b != '':
                    pl.append([a, b])
    return pl

if __name__ == '__main__':
    fn = sys.argv[1]
    sl = load_cabocha(fn)

    for p in get_relation_pairs(sl):
        print(p[0], p[1], sep='\t')
