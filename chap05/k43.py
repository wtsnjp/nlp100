#
# usage: python k43.py {file name}
#

import sys
from k41 import *

def get_sv_relation_pairs(sl):
    pl = []
    for s in sl:
        for c in s:
            if c.dst != -1 and c.dst < len(s):
                a, b = '', ''
                nf, vf = False, False
                for v in c.morphs:
                    if v.pos != '記号':
                        a += v.surface
                    if v.pos == '名詞':
                        nf = True
                for v in s[c.dst].morphs:
                    if v.pos != '記号':
                        b += v.surface
                    if v.pos == '動詞':
                        vf = True
                if a != '' and b != '' and nf and vf:
                    pl.append([a, b])
    return pl

if __name__ == '__main__':
    fn = sys.argv[1]
    sl = load_cabocha(fn)

    for p in get_sv_relation_pairs(sl):
        print(p[0], p[1], sep='\t')
