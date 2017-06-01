#
# usage: python k74.py {file name}
#

import sys
from sentiment import SentimentSentences

if __name__ == '__main__':
    fn = sys.argv[1]
    
    data = SentimentSentences([l for l in open(fn)])
    data.feature_extraction()

    data.train()

    print(data.predict("a very charming and funny movie ."))
