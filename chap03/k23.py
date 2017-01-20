#
# usage: python k23.py {file name} {article title}
#

import sys
import re
from k20 import load_article

def get_section_structure(text):
    ls, p = [], re.compile("(=+)(.*?)=+")
    for l in text.splitlines():
        m = p.match(l)
        if m:
            ls.append([str(m.group(2)).strip(), len(m.group(1))-1])
    return ls

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    article = load_article(fn, title)
    for s in get_section_structure(article):
        print(s[0], s[1])
