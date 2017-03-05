from nltk import stem
from collections import Counter
from bisect import bisect_left

class SentimentSentences:
    def __init__(self, sentences):
        sl = [s.split() for s in sentences]
        self.sentences = list(map(self.__sentence_dict, sl))

    @staticmethod
    def __sentence_dict(s):
        p, src = 0, ' '.join(s[1:])
        if s[0][0] == '+':
            p = 1
        return {'polar': p, 'src': src}

    def feature_extraction(self, fr=10):
        """remove stop/unique words and stemming"""
        sl = [s['src'].split() for s in self.sentences]
        stemmer = stem.PorterStemmer()
        
        c, st = Counter([w for s in sl for w in list(set(s[1:]))]), len(sl) * fr / 100
        self.stopwords = sorted([k for k, v in c.items() if v > st])
        self.uniqwords = sorted([k for k, v in c.items() if v == 1])
        
        for s in self.sentences:
            s['feature'] = [stemmer.stem(w) for w in s['src'].split()
                            if not self.is_stopword(w) and not self.is_uniqword(w)]

    def is_stopword(self, w):
        ss = self.stopwords
        i, b = bisect_left(ss, w), False
        if i != len(ss) and ss[i] == w:
            b = True
        return b

    def is_uniqword(self, w):
        us = self.uniqwords
        i, b = bisect_left(us, w), False
        if i != len(us) and us[i] == w:
            b = True
        return b
