#
# usage: python k48.py {file name} {number}
#

import sys
from k41 import *

def noun_root_path(s):
    pl, nf = [], False
    for c in s:
        if '名詞' in [m.pos for m in c.morphs]:
            nf, p = True, []
        while nf:
            p.append(''.join([m.surface for m in c.morphs if m.pos != '記号']))
            if c.dst != -1:
                c = s[c.dst]
            else:
                pl.append(p)
                nf = False
    return pl

if __name__ == '__main__':
    fn, nos = sys.argv[1], int(sys.argv[2])
    sl = load_cabocha(fn)
    pl = noun_root_path(sl[nos-1])

    for p in pl:
        print(' -> '.join(p))
