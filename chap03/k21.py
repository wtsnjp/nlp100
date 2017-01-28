#
# usage: python k21.py {file name} {article title}
#

import sys
import re
from k20 import load_article

def get_category_lines(text):
    p = re.compile("\[\[Category:")
    return [l for l in text.splitlines() if p.match(l)]

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    article = load_article(fn, title)
    for l in get_category_lines(article):
        print(l)
