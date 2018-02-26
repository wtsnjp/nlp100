#
# usage: python k90.py {file name}
#

import os
import sys
import logging

from gensim.models import word2vec

def run_word2vec(fn):
    mf = './enwiki.model'
    if not os.path.exists(mf):
        sentences = word2vec.Text8Corpus(fn)
        model = word2vec.Word2Vec(sentences, size=300, min_count=10, window=5)
        model.save(mf)
    else:
        model = word2vec.Word2Vec.load(mf)
    model.wv.save_word2vec_format(mf + '.txt', binary=False)

if __name__ == '__main__':
    fn = sys.argv[1]

    #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    run_word2vec(fn)
