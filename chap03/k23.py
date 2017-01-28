#
# usage: python k23.py {file name} {article title}
#

import sys
import re
from k20 import load_article

def get_section_structure(text):
    p = re.compile("(=+)(.*?)=+")
    return [[str(m.group(2)).strip(), len(m.group(1))-1]
            for m in [p.match(l) for l in text.splitlines()] if m]

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    article = load_article(fn, title)
    for s in get_section_structure(article):
        print(s[0], s[1])
