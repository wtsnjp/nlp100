#
# Class SentimentSentences: sentences for polarity analysis
#

from nltk import stem
from collections import Counter
from bisect import bisect_left
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

class SentimentSentences:
    def __init__(self, sentences):
        sl = list(map(self.__sentence_dict,
                      [s.split() for s in sentences]))
        self.polar = [s[0] for s in sl]
        self.src = [s[1] for s in sl]

    @staticmethod
    def __sentence_dict(s):
        p, src = 0, ' '.join(s[1:])
        if s[0][0] == '+':
            p = 1
        return p, src

    def feature_extraction(self, fr=10):
        """remove stop/unique words and stemming"""
        sl = [s.split() for s in self.src]
        stemmer = stem.PorterStemmer()

        cn = Counter([w for s in sl for w in list(set(s[1:]))])
        st = len(sl) * fr / 100
        self.stopwords = sorted([k for k, v in cn.items() if v > st])
        self.uniqwords = sorted([k for k, v in cn.items() if v == 1])

        self.feature = [' '.join([stemmer.stem(w) for w in s
                                  if not (self.is_stopword(w)
                                          or self.is_uniqword(w))])
                        for s in sl]

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

    def train(self, param=1000.0):
        lr, cv = LogisticRegression(C=param), CountVectorizer()
        self.vector = cv.fit_transform(self.feature)
        self.model = lr.fit(self.vector, self.polar)

    def predict(self, text):
        vec = self.vector[self.src.index(text),:]
        pr = self.model.predict_proba(vec)[0]
        if pr[0] > pr[1]:
            return "-1", pr[0]
        else:
            return "+1", pr[1]

