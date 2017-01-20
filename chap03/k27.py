#
# usage: python k27.py {file name} {article title} {template name}
#

import sys
import re
from k20 import load_article
from k25 import template2dict
from k26 import remove_stress

def remove_inner_links(dc):
    for k, v in dc.items():
        dc[k] = re.sub(r'\[\[(.+\||)(.+?)\]\]', r'\2', v)
    return dc

if __name__ == '__main__':
    fn, title, template = sys.argv[1:]
    article = load_article(fn, title)
    dc = template2dict(article, template)
    print(remove_inner_links(remove_stress(dc)))
