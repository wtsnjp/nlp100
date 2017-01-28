#
# usage: python k26.py {file name} {article title} {template name}
#

import sys
import re
from k20 import load_article
from k25 import template2dict

def remove_stress(dc):
    r = re.compile("'+")
    return {k:r.sub('', v) for k,v in dc.items()}

if __name__ == '__main__':
    fn, title, template = sys.argv[1:]
    article = load_article(fn, title)
    dc = template2dict(article, template)
    print(remove_stress(dc))
