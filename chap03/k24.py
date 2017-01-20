#
# usage: python k24.py {file name} {article title}
#

import sys
import re
from k20 import load_article

def get_media_files(text):
    ls, p = [], re.compile("ファイル:(.+?)\|")
    for l in text.splitlines():
        m = p.search(l)
        if m:
            ls.append(str(m.group(1)).strip().replace(' ', '_'))
    return ls

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    article = load_article(fn, title)
    for f in get_media_files(article):
        print(f)
