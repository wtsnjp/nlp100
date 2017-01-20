#
# usage: python k22.py {file name} {article title}
#

import sys
import re
from k20 import load_article

def get_category_names(text):
    ls, p = [], re.compile("\[\[Category:(.*?)(\|.*\]\]|\]\])")
    for l in text.splitlines():
        m = p.match(l)
        if m != None:
            ls.append(m.group(1))
    return ls

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    article = load_article(fn, title)
    for l in get_category_names(article):
        print(l)
