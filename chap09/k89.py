#
# usage: python k89.py {model file}
#

import sys
import numpy as np

def var_sim10(fn, w1, w2, w3):
    # initialize
    rd = []
    def cos_sim(v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    # get word vecs
    for l in open(fn):
        tmp = l.split(' ')
        if tmp[0] == w1:
            v1 = np.array([float(i) for i in tmp[1:]])
        elif tmp[0] == w2:
            v2 = np.array([float(i) for i in tmp[1:]])
        elif tmp[0] == w3:
            v3 = np.array([float(i) for i in tmp[1:]])

    # calculate analogy
    v = v1 - v2 + v3

    # calculate cos_sim
    for l in open(fn):
        tmp = l.split(' ')
        tw = tmp[0]
        if not tw in (w1, w2, w3) and len(tmp) == 301:
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

    for t in var_sim10(fn, 'Spain', 'Madrid', 'Athens'):
        print('{}\t{}'.format(t[0], t[1]))
