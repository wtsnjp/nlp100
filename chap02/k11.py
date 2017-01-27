#
# usage: python k11.py {file name}
#

import sys

def tab2space(fn):
    return ''.join([l.replace('\t', ' ') for l in open(fn)])

if __name__ == '__main__':
    fn = sys.argv[1]
    print(tab2space(fn), end='')
