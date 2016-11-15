#
# usage: python k13.py {file name} ...
#

import sys

def col_get(fns):
    ad, r = [], []
    for fn in fns:
        cd = []
        for l in open(fn):
            cd.append(l.rstrip())
        ad.append(cd)
    for i in range(len(ad[0])):
        cd = []
        for d in ad:
            cd.append(d[i])
        r.append(cd)
    return r

if __name__ == '__main__':
    fns = sys.argv[1:]
    for l in col_get(fns):
        print('\t'.join([str(d) for d in l]))
