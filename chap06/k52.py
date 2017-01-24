#
# usage: python k52.py {file name}
#

import sys
from nltk import stem
from k50 import get_sentence_list
from k51 import get_word_list

def stemming(wl):
    stemmer = stem.PorterStemmer()
    return [[w, stemmer.stem(w)] for w in wl]

if __name__ == '__main__':
    fn = sys.argv[1]

    sl = get_sentence_list(open(fn).read())
    wl = [w.lower() for swl in get_word_list(sl) for w in swl]
    for w in stemming(wl):
        print(w[0], w[1], sep='\t')
