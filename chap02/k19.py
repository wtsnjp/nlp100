#
# usage: python k19.py {file name} {column number}
#

import sys
import collections

def sort_by_frequency(fn, n):
    cd = collections.Counter([l.split()[n-1] for l in open(fn)])
    return [k for k, v in cd.most_common()]

if __name__ == '__main__':
    fn, n = sys.argv[1], int(sys.argv[2])
    for e in sort_by_frequency(fn, n):
        print(e)
