#
# usage: python k20.py {file name} {article title}
#

import sys
import gzip
import json

def load_article(fn, title):
    data = gzip.open(fn, 'rb').read().decode('utf-8')
    for a in [json.loads(l) for l in data.splitlines()]:
        if a['title'] == title:
            return a['text']

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    print(load_article(fn, title))
