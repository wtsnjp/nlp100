#
# usage: python k72.py {file name}
#

import sys
from sentiment import SentimentSentences

if __name__ == '__main__':
    fn = sys.argv[1]
    
    data = SentimentSentences([l for l in open(fn)])
    data.feature_extraction()

    for s in data.sentences:
        print(s)
