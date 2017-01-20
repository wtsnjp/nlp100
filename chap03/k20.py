#
# usage: python k20.py {file name} {article title}
#

import sys
import gzip
import json

def load_article(fn, title):
    f = gzip.open(fn, 'rb')
    data = f.read().decode('utf-8')
    f.close()

    article_dict = {}
    for l in data.splitlines():
        line_dict = json.loads(l)
        article_dict[line_dict['title']] = line_dict

    return article_dict[title]['text']

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    print(load_article(fn, title))
