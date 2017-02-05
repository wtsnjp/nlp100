#
# usage: python k64.py {input file} {index} ...
#

import sys
import json
import pymongo

def create_index(fn, il):
    db = pymongo.MongoClient().MusicBrainz
    cn = db.artist
    for l in open(fn):
        d = json.loads(l)
        cn.insert_one(d)
    cn.create_index([(i, pymongo.ASCENDING) for i in il])

if __name__ == '__main__':
    fn, il = sys.argv[1], sys.argv[2:]
    create_index(fn, il)
