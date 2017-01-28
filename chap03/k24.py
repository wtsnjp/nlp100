#
# usage: python k24.py {file name} {article title}
#

import sys
import re
from k20 import load_article

def get_media_files(text):
    p = re.compile("ファイル:(.+?)\|")
    return [str(m.group(1)).strip().replace(' ', '_')
            for m in [p.search(l) for l in text.splitlines()] if m]

if __name__ == '__main__':
    fn, title = sys.argv[1:]
    article = load_article(fn, title)
    for f in get_media_files(article):
        print(f)
