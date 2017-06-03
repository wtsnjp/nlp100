#
# usage: python k75.py {file name}
#

import sys
from sentiment import SentimentSentences

if __name__ == '__main__':
    fn = sys.argv[1]
    
    data = SentimentSentences([l for l in open(fn)])
    data.feature_extraction()

    data.train()

    idx = data.model.coef_[0].argsort()

    print('high-weight:')
    for i in idx[:10]:
        print('\t', data.vec.get_feature_names()[i], sep='')

    print('low-weight:')
    for i in idx[-10:]:
        print('\t', data.vec.get_feature_names()[i], sep='')

