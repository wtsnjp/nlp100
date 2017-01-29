#
# usage: python k39.py {file name}
#

import sys
import collections
from matplotlib import pyplot as plt
from k30 import load_mecab
from k36 import frequency_ranking

if __name__ == '__main__':
    NUM = 10
    fn = sys.argv[1]
    data = load_mecab(fn)
    ls = frequency_ranking(data)

    plt.plot([v[1]/len(ls) for v in ls])
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('順位')
    plt.ylabel('出現頻度')
    plt.show()
