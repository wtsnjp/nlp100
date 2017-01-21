#
# usage: python k32.py {file name}
#

import sys
from k30 import load_mecab
from k31 import get_morpheme_list

if __name__ == '__main__':
    fn = sys.argv[1]
    data = load_mecab(fn)
    for v in get_morpheme_list(data, 'pos', '動詞', 'base'):
        print(v)
