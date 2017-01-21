#
# usage: python k31.py {file name}
#

import sys
from k30 import load_mecab

def get_morpheme_list(data, key, value, out):
    l = []
    for s in data:
        for m in s:
            if m[key] == value:
                l.append(m[out])
    return l

if __name__ == '__main__':
    fn = sys.argv[1]
    data = load_mecab(fn)
    for v in get_morpheme_list(data, 'pos', '動詞', 'surface'):
        print(v)
