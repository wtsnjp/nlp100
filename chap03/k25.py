#
# usage: python k25.py {file name} {article title} {template name}
#

import sys
import re
from k20 import load_article

def template2dict(text, template):
    ls, fg = [], False
    p1 = re.compile('\{\{' + template)
    p2 = re.compile('\}\}')
    p3 = re.compile('\|')
    p4 = re.compile('<ref(\s|>).+?(</ref>|$)')
    for l in text.splitlines():
        if fg:
            ml = [p2.match(l), p3.match(l)]
            if ml[0]:
                break
            if ml[1]:
                ls.append(p4.sub('', l.strip()))
        if p1.match(l):
            fg = True
    p = re.compile('\|(.+?)\s=\s(.+)')
    return {m.group(1):m.group(2) for m in [p.match(c) for c in ls]}

if __name__ == '__main__':
    fn, title, template = sys.argv[1:]
    article = load_article(fn, title)
    print(template2dict(article, template))
