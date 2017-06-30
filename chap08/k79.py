#
# usage: python k79.py {file name}
#

import sys
import matplotlib.pyplot as plt
from sentiment import SentimentSentences
from k78 import cross_validation

if __name__ == '__main__':
    fn = sys.argv[1]

    ls, tl = [l for l in open(fn)], list(range(0, 100, 10))
    prl, rrl = [[] for i in range(2)]

    for t in tl:
        cr, pr, rr = cross_validation(5, ls, th=t)
        prl.append(pr)
        rrl.append(rr)
    
    plt.plot(tl, prl, label='precision', color='red')
    plt.plot(tl, rrl, label='recall', color='blue')
    
    plt.xlabel('threshold')
    plt.ylabel('rate')
    plt.xlim(0, 100)
    plt.ylim(0, 1)
    plt.title('Logistic Regression')
    plt.legend(loc=3)
    
    plt.show()
