#
# usage: python k62.py {file name} {area}
#

import sys
import json
import plyvel

def count_artists(fn, area):
    db, cnt = plyvel.DB(fn), 0
    for n, a in db:
        if a.decode() == area:
            cnt += 1
    db.close()
    return cnt

if __name__ == '__main__':
    fn, area = sys.argv[1], sys.argv[2]
    
    print(count_artists(fn, area))
