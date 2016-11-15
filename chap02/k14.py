#
# usage: python k14.py {file name} {line number}
#

import sys

def head(fn, n):
    c, r = 0, ''
    for l in open(fn):
        if c == n: break
        r += l
        c += 1
    return r

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    print(head(fn, n), end='')
