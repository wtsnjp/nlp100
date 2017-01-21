#
# usage: python k38.py {file name}
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

    cl, ln = [], len(ls)
    for v in ls:
        cl.append(v[1]/ln)

    plt.hist(cl, 50, range=(0.0, 0.01))
    plt.xlabel('出現頻度')
    plt.ylabel('種類数')
    plt.show()
