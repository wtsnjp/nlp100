#
# usage: python k15.py {file name} {line number}
#

import sys

def tail(fn, n):
    r = []
    for l in open(fn):
        r.append(l)
    return ''.join(r[-n:])

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    print(tail(fn, n), end='')
