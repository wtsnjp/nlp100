#
# usage: python k36.py {file name}
#

import sys
import collections
from k30 import load_mecab

def frequency_ranking(data):
    cd = collections.Counter([m['base'] for s in data for m in s])
    return [[k, v] for k,v in cd.most_common()]

if __name__ == '__main__':
    fn = sys.argv[1]
    data = load_mecab(fn)
    for v in frequency_ranking(data):
        print(v[0], v[1])
