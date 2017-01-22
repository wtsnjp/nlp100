#
# usage: python k46.py {file name}
#

import sys
from k41 import *

def get_case_frame_info(sl):
    pl = []
    for s in sl:
        for c in s:
            for m in c.morphs:
                if m.pos != '動詞':
                    continue
                verb, pps, pchs, chs = m.base, [], [], []
                for i in c.srcs:
                    ch, ppf = [], False
                    for m_i in s[i].morphs:
                        if m_i.pos != '記号':
                            ch.append(m_i.surface)
                        if m_i.pos == '助詞':
                            pps.append(m_i.base)
                            ppf = True
                    if ppf:
                        pchs.append([''.join(ch), pps[-1]])
                if pps != []:
                    pps = sorted(list(set(pps)))
                    for p in pps:
                        chs.extend([c[0] for c in pchs if c[1] == p])
                    pl.append([verb, pps, chs])
    return pl

if __name__ == '__main__':
    fn = sys.argv[1]
    sl = load_cabocha(fn)
    pl = get_case_frame_info(sl)

    for p in pl:
        print(p[0], ' '.join(p[1]), ' '.join(p[2]), sep='\t')
