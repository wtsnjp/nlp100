#
# usage: python k45.py {file name}
#

import sys
from k41 import *

def get_case_pttern(sl):
    pl = []
    for s in sl:
        for c in s:
            for m in c.morphs:
                if m.pos != '動詞':
                    continue
                verb, pps = m.base, []
                for i in c.srcs:
                    for m_i in s[i].morphs:
                        if m_i.pos == '助詞':
                            pps.append(m_i.base)
                if pps != []:
                    pps = sorted(list(set(pps)))
                    pl.append([verb, pps])
    return pl

if __name__ == '__main__':
    fn = sys.argv[1]
    sl = load_cabocha(fn)
    pl = get_case_pttern(sl)

    for p in pl:
        print(p[0], ' '.join(p[1]), sep='\t')
