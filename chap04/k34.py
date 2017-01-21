#
# usage: python k34.py {file name}
#

import sys
from k30 import load_mecab

def noun_no_noun(data):
    ls = []
    for s in data:
        if len(s) < 3:
            continue
        for i in range(2, len(s)-1):
            if s[i-1]['surface'] != 'の':
                continue
            if s[i-2]['pos'] == s[i]['pos'] and s[i]['pos'] == '名詞':
                ls.append(s[i-2]['surface'] + 'の' + s[i]['surface'])
    return ls

if __name__ == '__main__':
    fn = sys.argv[1]
    data = load_mecab(fn)
    for v in noun_no_noun(data):
        print(v)
