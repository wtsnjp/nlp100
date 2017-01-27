#
# usage: python k17.py {file name} {column number}
#

import sys

def sort_item(fn, n):
    return sorted(list({l.split()[n-1] for l in open(fn)}))

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    for e in sort_item(fn, n):
        print(e)
