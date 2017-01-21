#
# usage: python k30.py {file name}
#

import sys

def load_mecab(fn):
    sl, s = [], []
    keys = ['surface', 'pos', 'pos1', 'pos2', 'pos3', 'infection',
            'conjugations', 'base', 'read', 'pronunciation']

    with open(fn) as f:
        for l in f:
            if l == "EOS\n":
                if s != []:
                    sl.append(s)
                    s = []
            else:
                l = l.replace('\t', ',')
                values = l.split(',')
                if len(values) == 10:
                    s.append(dict(zip(keys, values)))
    return sl

if __name__ == '__main__':
    fn = sys.argv[1]
    for s in load_mecab(fn):
        print(s)
