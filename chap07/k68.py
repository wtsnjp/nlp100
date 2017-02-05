#
# usage: python k68.py {tag}
#

import sys
import pymongo

def top10(tag):
    cn = pymongo.MongoClient().MusicBrainz.artist
    al = [[d['name'], d['rating']['count']]
            for d in cn.find({'tags.value': tag}) if 'rating' in d]
    return sorted(al, key=lambda x:x[1], reverse=True)[:10]

if __name__ == '__main__':
    t = sys.argv[1]
    for a in top10(t):
        print(a[0], a[1])
