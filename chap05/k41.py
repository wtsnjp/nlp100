#
# usage: python k41.py {file name} {number}
#

import sys

class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base    = dc['base']
        self.pos     = dc['pos']
        self.pos1    = dc['pos1']

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst    = dst
        self.srcs   = []

def load_cabocha(fn):
    sl, pl, s, p = [], [], [], []
    keys = ['surface', 'pos', 'pos1', 'pos2', 'pos3', 'infection',
            'conjugations', 'base', 'read', 'pronunciation']

    with open(fn) as f:
        for l in f:
            if l == 'EOS\n':
                if p != []:
                    c = Chunk(p, dst)
                    pl.append(c)
                    p = []
                if pl != []:
                    sl.append(pl)
                    pl = []
            elif l[0] == '*':
                if p != []:
                    c = Chunk(p, dst)
                    pl.append(c)
                    p = []
                ll = l.split(' ')
                dst = int(ll[2][:-1])
            else:
                l = l.replace('\t', ',')
                values = l.split(',')
                if len(values) == 10:
                    p.append(Morph(dict(zip(keys, values))))

    for s in sl:
        n = 0
        for c in s:
            if c.dst != -1 and c.dst < len(s):
                s[c.dst].srcs.append(n)
            n += 1

    return sl

if __name__ == '__main__':
    fn, nos = sys.argv[1], int(sys.argv[2])
    sl = load_cabocha(fn)

    for c in sl[nos-1]:
        ml = c.morphs
        for m in ml:
            if m.pos != '記号':
                print(m.surface, end='')
        print('', c.dst)
