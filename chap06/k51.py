#
# usage: python k51.py {file name}
#

import sys
import re
from k50 import get_sentence_list

def get_word_list(sl):
    r = re.compile('[^a-zA-Z0-9]')
    return [[r.sub('', w) for w in s.split(' ')] for s in sl]

if __name__ == '__main__':
    fn = sys.argv[1]

    sl = get_sentence_list(open(fn).read())
    for s in get_word_list(sl):
        for w in s:
            print(w)
        print()
