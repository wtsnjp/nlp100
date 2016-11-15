#
# usage: python k17.py {file name} {column number}
#

import sys

def sort_item(fn, n):
    s = set()
    for l in open(fn):
        t = l.split()
        s.add(t[n-1])
    return sorted(list(s))

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    for e in sort_item(fn, n):
        print(e)
