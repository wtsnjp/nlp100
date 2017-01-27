#
# usage: python k10.py {file name}
#

import sys

def count_lines(fn):
    return len([l for l in open(fn)])

if __name__ == '__main__':
    fn = sys.argv[1]
    print(count_lines(fn))
