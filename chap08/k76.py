#
# usage: python k76.py {file name}
#

import sys
from sentiment import SentimentSentences

if __name__ == '__main__':
    fn = sys.argv[1]
    
    ls = [l for l in open(fn)]

    data = SentimentSentences(ls)
    data.feature_extraction()
    data.train()

    for s in [l.split() for l in ls]:
        t = data.predict(' '.join(s[1:]))
        print(s[0], t[0], t[1], sep='\t')

