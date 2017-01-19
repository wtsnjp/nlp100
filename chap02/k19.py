#
# usage: python k19.py {file name} {column number}
#

import sys
import collections

def sort_by_frequency(fn, n):
    ls = []
    for l in open(fn):
        t = l.split()
        ls.append(t[n-1])
    cd = collections.Counter(ls)
    ls = []
    for k, v in cd.most_common():
        ls.append(k)
    return ls

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    for e in sort_by_frequency(fn, n):
        print(e)
