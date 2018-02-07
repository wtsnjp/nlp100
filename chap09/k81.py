#
# usage: python k81.py {data} {countries list}
#

import sys
import re

def tokenize(l, cl):
    r = re.compile(r'[\.,\!\?;:\(\)\[\]\'"]')
    tk = [r.sub('', w) for w in l.split(' ')]

    while tk.count('') > 0:
        tk.remove('')

    ts = ' '.join(tk)

    for c in cl:
        ts = ts.replace(c, c.replace(' ', '_'))

    return ts

def load_countries(fn):
    return [l.split(',')[0] for l in open(fn)][1:]

if __name__ == '__main__':
    dt, ct = sys.argv[1:]
    ot = 'enwiki-tokens.txt'

    cl = load_countries(ct)

    for l in open(dt):
        tk = tokenize(l.strip(), cl)
        
        with open(ot, 'a') as f:
            if len(tk) > 0:
                f.write(tk + '\n')
