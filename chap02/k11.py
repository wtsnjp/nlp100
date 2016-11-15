#
# usage: python k11.py {file name}
#

import sys
import re

def tab2space(fn):
    r = ""
    for l in open(fn):
        r += re.sub(r'\t', ' ', l)
    return r

if __name__ == '__main__':
    fn = sys.argv[1]
    print(tab2space(fn), end='')

