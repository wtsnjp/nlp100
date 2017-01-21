#
# usage: python k35.py {file name}
#

import sys
from k30 import load_mecab

def successive_noun(data):
    ls, tmp = [], []
    for s in data:
        for m in s:
            if m['pos'] == '名詞':
                tmp.append(m['surface'])
            else:
                if len(tmp) > 2:
                    ls.append(''.join(tmp))
                tmp = []
    return ls

if __name__ == '__main__':
    fn = sys.argv[1]
    data = load_mecab(fn)
    for v in successive_noun(data):
        print(v)
