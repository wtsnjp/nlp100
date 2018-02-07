#
# usage: python k80.py {file name}
#

import sys
import re

def tokenize(l):
    r = re.compile(r'[\.,\!\?;:\(\)\[\]\'"]')
    tk = [r.sub('', w) for w in l.split(' ')]

    while tk.count('') > 0:
        tk.remove('')

    return tk

if __name__ == '__main__':
    fn = sys.argv[1]
    ot = 'enwiki-tokens.txt'

    for l in open(fn):
        tk = tokenize(l.strip())
        
        with open(ot, 'a') as f:
            if len(tk) > 0:
                f.write(' '.join(tk) + '\n')
