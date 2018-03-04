#
# usage: python k86.py {model file}
#

import sys

def word_vec(fn, w):
    for l in open(fn):
        tmp = l.split(' ')
        if tmp[0] == w:
            return [float(i) for i in tmp[1:]]
    return None

if __name__ == '__main__':
    fn = sys.argv[1]

    w = 'United_States'
    vec = word_vec(fn, w)
    if vec is None:
        print('! No result for "{}"'.format(w))
    else:
        print(vec)
