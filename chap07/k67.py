#
# usage: python k67.py {alias}
#

import sys
import pymongo

def find_aliases(alias):
    cn = pymongo.MongoClient().MusicBrainz.artist
    return [a for a in cn.find({'aliases.name': alias})]

if __name__ == '__main__':
    n = sys.argv[1]
    for a in find_aliases(n):
        print(a)
