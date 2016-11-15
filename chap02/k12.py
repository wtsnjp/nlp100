#
# usage: python k12.py {file name} {column number}
#

import sys

def cut_col(fn, cn):
    r = []
    for l in open(fn):
        r.append(l.split()[cn-1])
    return r

if __name__ == '__main__':
    fn, cn = sys.argv[1], int(sys.argv[2])
    for d in cut_col(fn, cn):
        print(d)
