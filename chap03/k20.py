#
# usage: python k20.py {file name} {article title}
#

import sys
import json

def load_article(fn, title):
    for l in open(fn):
        a = json.loads(l)
        if a['title'] == title:
            return a['text']

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    print(load_article(fn, title))
