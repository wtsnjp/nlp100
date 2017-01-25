#
# usage: python k57.py {file name} {number}
#

import sys
import pydot
from xml.etree import ElementTree as ET

def isnode(text):
    return text != 'ROOT' and text.isalnum()

if __name__ == '__main__':
    fn, nod = sys.argv[1], int(sys.argv[2])

    root = ET.parse(fn).getroot()
    cdl = [d for d in root.findall('document/sentences/*/dependencies')
            if d.get('type') == 'collapsed-dependencies']
    el = [n.split(' ') for n in
            {' '.join([p[1].text, p[0].text])
                for p in cdl[nod-1].findall('*')
                for n in p.findall('*')
                if isnode(p[0].text) and isnode(p[1].text)}]

    g = pydot.graph_from_edges(el, directed=True)
    g.write_png('result.png', prog='dot')
