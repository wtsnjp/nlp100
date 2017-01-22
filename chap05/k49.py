#
# usage: python k49.py {file name} {number}
#

import sys
from k41 import *

def noun_noun_path(s):
    pl, nl = [], [c for c in s if '名詞' in [m.pos for m in c.morphs]]
    for i in range(len(nl)-1):
        st1 = [''.join([m.surface if m.pos != '名詞' else 'X' for m in nl[i].morphs])]
        for e in nl[i+1:]:
            dst, p = nl[i].dst, []
            st2 = [''.join([m.surface if m.pos != '名詞' else 'Y' for m in e.morphs])]
            while dst != -1 and dst != s.index(e):
                p.append(s[dst])
                dst = s[dst].dst
            if len(p) < 1 or p[-1].dst != -1:
                mid = [''.join([m.surface for m in c.morphs if m.pos != '記号']) for c in p]
                pl.append(st1 + mid + ['Y'])
            else:
                mid, dst = [], e.dst
                while not s[dst] in p:
                    mid.append(''.join([m.surface for m in s[dst].morphs]))
                    dst = s[dst].dst
                ed = [''.join([m.surface for m in s[dst].morphs if m.pos != '記号'])]
                pl.append([st1, st2 + mid, ed])
    return pl

if __name__ == '__main__':
    fn, nos = sys.argv[1], int(sys.argv[2])
    sl = load_cabocha(fn)
    pl = noun_noun_path(sl[nos-1])
    
    for p in pl:
        if isinstance(p[0], str):
            print(' -> '.join(p))
        else:
            print(p[0][0], ' -> '.join(p[1]), p[2][0], sep=' | ')
