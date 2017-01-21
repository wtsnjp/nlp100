#
# usage: python k36.py {file name}
#

import sys
import collections
from k30 import load_mecab

def frequency_ranking(data):
    ls, tmp = [], []
    for s in data:
        for m in s:
            tmp.append(m['base'])
    cd = collections.Counter(tmp)
    for k, v in cd.most_common():
        ls.append([k, v])
    return ls

if __name__ == '__main__':
    fn = sys.argv[1]
    data = load_mecab(fn)
    for v in frequency_ranking(data):
        print(v[0], v[1])
