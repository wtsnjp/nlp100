#
# usage: python k15.py {file name} {line number}
#

import sys

def tail(fn, n):
    return ''.join([l for l in open(fn)][-n:])

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    print(tail(fn, n), end='')
