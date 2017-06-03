#
# usage: python k78.py {file name}
#

import sys
from sentiment import SentimentSentences

def split_array(ls, gn):
    ln = len(ls)
    for i in range(gn):
        yield ls[i * ln // gn:(i+1) * ln // gn]

if __name__ == '__main__':
    fn, gn = sys.argv[1], 5

    lss = list(split_array([l for l in open(fn)], gn))
    crs, prs, rrs = [[] for i in range(3)]

    for i in range(gn):
        ns = [i for i in range(gn)]
        ns.remove(i)
        trl = [c for l in [lss[j] for j in ns] for c in l]

        data = SentimentSentences(trl)
        data.feature_extraction()
        data.train()
        
        c, pc, rp, pp = [0 for i in range(4)]
        for l in [(s[0], data.predict(' '.join(s[1:]))[0])
                  for s in [l.split() for l in lss[i]]]:
            if l[0] == l[1]:
                c += 1
                if l[0] == '+1':
                    pc += 1
            if l[0] == '+1':
                rp += 1
            if l[1] == '+1':
                pp += 1
        
        crs.append(c/len(lss[i]))
        prs.append(pc/pp)
        rrs.append(pc/rp)

    cr = sum(crs) / len(crs)
    pr = sum(prs) / len(prs)
    rr = sum(rrs) / len(rrs)

    print('correct rate:', cr)
    print('precision rate:', pr)
    print('recall rate:', rr)
    print('F1 score:', (2 * pr * rr) / (pr + rr))

