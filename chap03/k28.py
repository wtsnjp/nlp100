#
# usage: python k28.py {file name} {article title} {template name}
#

import sys
import re
from k20 import load_article
from k25 import template2dict

def remove_markups(dc):
    r1 = re.compile("'+")
    r2 = re.compile('\[\[(.+\||)(.+?)\]\]')
    r3 = re.compile('\{\{(.+\||)(.+?)\}\}')
    r4 = re.compile('<\s*?/*?\s*?br\s*?/*?\s*>')
    def sub_chain(s):
        s = r1.sub('', s)
        s = r2.sub(r'\2', s)
        s = r3.sub(r'\2', s)
        s = r4.sub('', s)
        return s
    return {k:sub_chain(v) for k,v in dc.items()}

if __name__ == '__main__':
    fn, title, template = sys.argv[1:]
    article = load_article(fn, title)
    dc = template2dict(article, template)
    print(remove_markups(dc))
