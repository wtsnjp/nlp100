#
# usage: python k65.py {artist}
#

import sys
import pymongo

def find_artist(name):
    cn = pymongo.MongoClient().MusicBrainz.artist
    return [a for a in cn.find({'name': name})]

if __name__ == '__main__':
    n = sys.argv[1]
    for a in find_artist(n):
        print(a)
