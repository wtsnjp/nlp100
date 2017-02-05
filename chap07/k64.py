#
# usage: python k64.py {input file} {index} ...
#

import sys
import json
import pymongo

def create_db(fn):
    cn = pymongo.MongoClient().MusicBrainz.artist
    for l in open(fn):
        d = json.loads(l)
        cn.insert_one(d)

def create_index(il):
    cn = pymongo.MongoClient().MusicBrainz.artist
    for i in il:
        cn.create_index([(i, pymongo.ASCENDING)])

if __name__ == '__main__':
    fn, il = sys.argv[1], sys.argv[2:]
    create_db(fn)
    create_index(il)
