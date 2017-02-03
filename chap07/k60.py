#
# usage: python k60.py {input file} {output file}
#

import sys
import gzip
import json
import plyvel

def create_kvs(fn1, fn2):
    db = plyvel.DB(fn2, create_if_missing=True)
    data = gzip.open(fn1, 'rb').read().decode('utf-8')
    for l in data.splitlines():
        d = json.loads(l)
        if 'name' in d and 'area' in d:
            db.put(d['name'].encode(), d['area'].encode())
    db.close()

if __name__ == '__main__':
    fn1, fn2 = sys.argv[1:]
    create_kvs(fn1, fn2)
