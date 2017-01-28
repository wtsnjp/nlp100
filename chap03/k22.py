#
# usage: python k22.py {file name} {article title}
#

import sys
import re
from k20 import load_article

def get_category_names(text):
    p = re.compile("\[\[Category:(.*?)(\|.*\]\]|\]\])")
    return [m.group(1) for m in [p.match(l) for l in text.splitlines()] if m != None]

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    article = load_article(fn, title)
    for l in get_category_names(article):
        print(l)
