#
# usage: python k28.py {file name} {article title} {template name}
#

import sys
import re
from k20 import load_article
from k25 import template2dict

def remove_markups(dc):
    for k, v in dc.items():
        v = re.sub(r"'+", '', v)
        v = re.sub(r'\[\[(.+\||)(.+?)\]\]', r'\2', v)
        v = re.sub(r'\{\{(.+\||)(.+?)\}\}', r'\2', v)
        v = re.sub(r'<\s*?/*?\s*?br\s*?/*?\s*>', '', v)
        dc[k] = v
    return dc

if __name__ == '__main__':
    fn, title, template = sys.argv[1:]
    article = load_article(fn, title)
    dc = template2dict(article, template)
    print(remove_markups(dc))
