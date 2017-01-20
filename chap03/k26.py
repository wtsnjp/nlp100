#
# usage: python k26.py {file name} {article title} {template name}
#

import sys
import re
from k20 import load_article
from k25 import template2dict

def remove_stress(dc):
    for k, v in dc.items():
        dc[k] = re.sub(r"'+", '', v)
    return dc

if __name__ == '__main__':
    fn, title, template = sys.argv[1:]
    article = load_article(fn, title)
    dc = template2dict(article, template)
    print(remove_stress(dc))
