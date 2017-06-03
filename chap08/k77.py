#
# usage: python k77.py {file name}
#

import sys
from sentiment import SentimentSentences

if __name__ == '__main__':
    fn = sys.argv[1]
    
    ls = [l for l in open(fn)]

    data = SentimentSentences(ls)
    data.feature_extraction()
    data.train()

    c, pc, rp, pp = [0 for i in range(4)]
    for l in [(s[0], data.predict(' '.join(s[1:]))[0])
              for s in [l.split() for l in ls]]:
        if l[0] == l[1]:
            c += 1
            if l[0] == '+1':
                pc += 1
        if l[0] == '+1':
            rp += 1
        if l[1] == '+1':
            pp += 1

    cr, pr, rr = c/len(ls), pc/pp, pc/rp
    print('correct rate:', cr)
    print('precision rate:', pr)
    print('recall rate:', rr)
    print('F1 score:', (2 * pr * rr) / (pr + rr))


