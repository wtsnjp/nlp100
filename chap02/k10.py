#
# usage: python k10.py {file name}
#

import sys

def count_lines(fn):
    c = 0
    for l in open(fn):
        c += 1
    return c

if __name__ == '__main__':
    fn = sys.argv[1]
    print(count_lines(fn))
