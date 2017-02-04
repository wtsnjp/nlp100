#
# usage: python k61.py {file name} {artist name} ...
#

import sys
import json
import plyvel

def get_area(fn, nl):
    db = plyvel.DB(fn)
    al = [db.get(n.encode()).decode() for n in nl]
    db.close()
    return al

if __name__ == '__main__':
    fn, nl = sys.argv[1], sys.argv[2:]
    
    for n, a in zip(nl, get_area(fn, nl)):
        print(n, a)
