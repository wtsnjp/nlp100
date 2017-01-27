#
# usage: python k13.py {file name} ...
#

import sys

def col_get(fns):
    ad = [[l.rstrip() for l in open(fn)] for fn in fns]
    return [[d[i] for d in ad] for i in range(len(ad[0]))]

if __name__ == '__main__':
    fns = sys.argv[1:]
    for l in col_get(fns):
        print('\t'.join([str(d) for d in l]))
