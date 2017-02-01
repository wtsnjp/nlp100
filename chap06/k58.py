#
# usage: python k58.py {file name} {number}
#

import sys
from xml.etree import ElementTree as ET

def get_tuple(nll, dll):
    return [[p, [n[1] for n in nl if n[0] == p][0],
                [d[1] for d in dl if d[0] == p][0]]
            for nl, dl in zip(nll, dll)
            for p in list({n[0] for n in nl} & {d[0] for d in dl})]
            
if __name__ == '__main__':
    fn = sys.argv[1]

    root = ET.parse(fn).getroot()
    cdl = [d for d in root.findall('document/sentences/*/dependencies')
            if d.get('type') == 'collapsed-dependencies']
    nll = [[[n.find('governor').text, n.find('dependent').text]
            for n in e.findall('*[@type="nsubj"]')]
            for e in cdl]
    dll = [[[d.find('governor').text, d.find('dependent').text]
            for d in e.findall('*[@type="dobj"]')]
            for e in cdl]

    for t in get_tuple(nll, dll):
        print('\t'.join(t))
