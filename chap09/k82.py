#
# usage: python k82.py {token file}
#

import sys
import random

def extract_context(ifn, ofn):
    for l in open(ifn):
        wl = l.split(' ')
        if len(wl) < 2:
            continue

        for i in range(len(wl)):
            t = wl[i]
            d = random.randint(1, 5)
            
            for j in range(max(0, i-d) , min(i+d, len(wl)-1)):
                if i != j:
                    with open(ofn, 'a') as f:
                        f.write('{}\t{}'.format(t, wl[j]) + '\n')

if __name__ == '__main__':
    ifn = sys.argv[1]
    ofn = 'enwiki-contexts.txt'

    extract_context(ifn, ofn)
