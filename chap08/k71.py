#
# usage: python k71.py {file name}
#

import sys
from collections import Counter

def stopwords(sl, fr):
    cn = Counter([w for s in sl for w in list(set(s))])
    st = len(sl) * fr / 100
    return [k for k, v in cn.items() if v > st]

def is_stopword(w, ss):
    return w in ss

if __name__ == '__main__':
    fn = sys.argv[1]
    
    sl = [l.split()[1:] for l in open(fn)]
    ss = stopwords(sl, 10)

    for w in ['is', 'a', 'the', 'happy', 'sad', 'cry']:
        print(w, is_stopword(w, ss))
