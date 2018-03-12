#
# usage: python k87.py {model file}
#

import sys
import numpy as np

def word_cos_sim(fn, w1, w2):
    v1, v2 = None, None
    for l in open(fn):
        tmp = l.split(' ')
        if tmp[0] == w1:
            v1 = np.array([float(i) for i in tmp[1:]])
        elif tmp[0] == w2:
            v2 = np.array([float(i) for i in tmp[1:]])
    if v1 is None or v2 is None:
        #return None
        print('failed')
        print('v1 = ' + str(v1))
        print('v2 = ' + str(v2))
    else:
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

if __name__ == '__main__':
    fn = sys.argv[1]

    w1, w2 = 'United_States', 'US'
    #w1, w2 = 'baseball', 'football'
    #w1, w2 = 'true', 'false'
    #w1, w2 = 'natural', 'seed'
    sim = word_cos_sim(fn, w1, w2)
    if sim is None:
        print('failed')
    else:
        print('cos("{}", "{}") = {}'.format(w1, w2, sim))
