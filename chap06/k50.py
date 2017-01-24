#
# usage: python k50.py {file name}
#

import sys
import re

def get_sentence_list(src):
    r1, r2 = re.compile('([.;:?!])\s([A-Z])'), re.compile(r'(\s*\n+)+\s*')
    tmp = [''] + [s.strip() for s in r1.split(r2.sub(' ', src))] + ['']
    return [''.join(tmp[3*i:3*(i+1)]) for i in range(len(tmp)//3)]

if __name__ == '__main__':
    fn = sys.argv[1]

    for s in get_sentence_list(open(fn).read()):
        print(s)
