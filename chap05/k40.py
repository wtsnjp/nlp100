#
# usage: python k40.py {file name} {number}
#

import sys

class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base    = dc['base']
        self.pos     = dc['pos']
        self.pos1    = dc['pos1']

def load_cabocha_file(fn):
    sl, s = [], []
    keys = ['surface', 'pos', 'pos1', 'pos2', 'pos3', 'infection',
            'conjugations', 'base', 'read', 'pronunciation']

    with open(fn) as f:
        for l in f:
            if l == "EOS\n":
                if s != []:
                    sl.append(s)
                    s = []
            elif l[0] != '*':
                l = l.replace('\t', ',')
                values = l.split(',')
                if len(values) == 10:
                    s.append(dict(zip(keys, values)))
    return sl

if __name__ == '__main__':
    fn, nos = sys.argv[1], int(sys.argv[2])

    ls, tmp = [], []
    for s in load_cabocha_file(fn):
        for m in s:
            tmp.append(Morph(m))
        ls.append(tmp)
        tmp = []
    
    for m in ls[nos-1]:
        print(vars(m))
