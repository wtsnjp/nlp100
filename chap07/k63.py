#
# usage: python k63.py {json file} {ldb file} {artist name}
#

import sys
import os.path
import json
import plyvel
from ast import literal_eval

def create_kvs(fn1, fn2):
    db = plyvel.DB(fn2, create_if_missing=True)
    for l in open(fn1):
        d = json.loads(l)
        if 'name' in d and 'tags' in d:
            db.put(d['name'].encode(), json.dumps(d['tags']).encode())
    db.close()

def get_tags(fn, n):
    return literal_eval(plyvel.DB(fn).get(n.encode()).decode())

if __name__ == '__main__':
    fn1, fn2, n = sys.argv[1:]

    if not os.path.exists(fn2):
        create_kvs(fn1, fn2)

    for t in get_tags(fn2, n):
        print(t['value'], t['count'])
