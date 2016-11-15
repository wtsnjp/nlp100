#
# usage: python k16.py {file name} {split number}
#

import sys
from k10 import count_lines

def split(fn, n):
    r, b, c, ln = [], '', 0, count_lines(fn)
    for l in open(fn):
        b += l
        if c == ln-1 or c%n == n-1:
            r.append(b)
            b = ''
        c += 1
    return r

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    d = split(fn, n)
    print('\n'.join(d))
