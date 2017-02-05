#
# usage: python k66.py {area}
#

import sys
import pymongo

def count_area(area):
    cn = pymongo.MongoClient().MusicBrainz.artist
    return cn.find({'area': area}).count()

if __name__ == '__main__':
    a = sys.argv[1]
    print(count_area(a))
