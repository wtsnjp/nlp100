#
# usage: python k70.py {pos file} {neg file} {output file}
#

import sys
import os
import random

def count_pn(sl):
    pc, nc = 0, 0
    for s in sl:
        if s[0] == '+':
            pc += 1
        elif s[0] == '-':
            nc += 1
    return (pc, nc)

if __name__ == '__main__':
    pf, nf, fn = sys.argv[1:]

    if os.path.isfile(fn):
        sl = [l for l in open(fn)]
    else:
        sl = ['+1 ' + l for l in open(pf)] + ['-1 ' + l for l in open(nf)]
        random.shuffle(sl)
        open(fn, 'w').writelines(sl)
    
    c = count_pn(sl)
    print(c[0], c[1])
