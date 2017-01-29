#
# usage: python k30.py {file name}
#

import sys

def load_mecab(fn):
    keys = ['surface', 'pos', 'pos1', 'pos2', 'pos3', 'infection',
            'conjugations', 'base', 'read', 'pronunciation']
    return [[dict(zip(keys, l.replace('\t', ',').split(',')))
                for l in s.split('\n') if l != '']
            for s in open(fn).read().split('EOS\n') if s != '']

if __name__ == '__main__':
    fn = sys.argv[1]
    for s in load_mecab(fn):
        print(s)
