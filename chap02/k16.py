#
# usage: python k16.py {file name} {split number}
#

import sys
from k10 import count_lines

def n_split(fn, n):
    sl = open(fn).read().split('\n')
    ln = len(sl) // n
    return [sl[i*ln:(i+1)*ln] if i<n-1 else sl[i*ln:] for i in range(n)]

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    d = n_split(fn, n)
    for i in range(n):
        if i != 0: print('\n')
        print('\n'.join(d[i]), end='')
