#
# usage: python k37.py {file name}
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

    kl, vl, dl = [], [], range(1, NUM+1)
    cnt = 0
    for k, v in ls:
        kl.append(k)
        vl.append(v)
        cnt += 1
        if cnt == NUM:
            break

    plt.bar(dl, vl, align='center')
    plt.xticks(dl, kl)
    plt.show()
