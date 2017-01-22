#
# usage: python k47.py {file name}
#

import sys
from k41 import *

def get_funktionsverben_patterns(sl):
    pl = []
    for s in sl:
        for c in s:
            for m in c.morphs:
                if m.pos != '動詞':
                    continue
                verb, pred = m.base, ''
                pps, pchs, chs = [], [], []
                for i in c.srcs:
                    ch, ppf = [], False
                    for m_i in s[i].morphs:
                        if m_i.pos != '記号':
                            ch.append(m_i.surface)
                        if m_i.pos == '助詞':
                            if m_i.base == 'を' and pre.pos1 == 'サ変接続':
                                pred = pre.surface + m_i.surface + verb
                            else:
                                pps.append(m_i.base)
                                ppf = True
                        pre = m_i
                    if ppf:
                        pchs.append([''.join(ch), pps[-1]])
                if pred != '' and pps != []:
                    pps = sorted(list(set(pps)))
                    for p in pps:
                        chs.extend([c[0] for c in pchs if c[1] == p])
                    pl.append([pred, pps, chs])
    return pl

if __name__ == '__main__':
    fn = sys.argv[1]
    sl = load_cabocha(fn)
    pl = get_funktionsverben_patterns(sl)

    for p in pl:
        print(p[0], ' '.join(p[1]), ' '.join(p[2]), sep='\t')
