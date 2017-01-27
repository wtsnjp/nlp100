#
# usage: python k18.py {file name} {column number}
#

import sys
from operator import itemgetter

def sort_by_item(fn, n):
    ls = [l.split() for l in open(fn)]
    ls.sort(key=itemgetter(n-1), reverse=True)
    return ls

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    for l in sort_by_item(fn, n):
        print('\t'.join(l))
