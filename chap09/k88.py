#
# usage: python k87.py {model file}
#

import sys
import numpy as np

def sim10(fn, w):
    # initialize
    rd = []
    def cos_sim(v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    # get word vec
    for l in open(fn):
        tmp = l.split(' ')
        if tmp[0] == w:
            v = np.array([float(i) for i in tmp[1:]])
            break

    # calculate cos_sim
    for l in open(fn):
        tmp = l.split(' ')
        tw = tmp[0]
        if tw != w and len(tmp) == 301:
            tv = np.array([float(i) for i in tmp[1:]])
            cs = cos_sim(v, tv)
            if len(rd) <= 10:
                rd.append((tv, cs))
            elif rd[0][1] < cs:
                rd[0] = (tw, cs)
            rd.sort(key=lambda x: x[1])

    return reversed(rd)

if __name__ == '__main__':
    fn = sys.argv[1]

    for t in sim10(fn, 'England'):
        print('{}\t{}'.format(t[0], t[1]))
