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
        self.vec = CountVectorizer()

    @staticmethod
    def __sentence_dict(s):
        p, src = 0, ' '.join(s[1:])
        if s[0][0] == '+':
            p = 1
        return p, src

    def feature_extraction(self, fr=99.9, uniq=False):
        """remove stop/unique words and stemming"""
        sl = [s.split() for s in self.src]
        stemmer = stem.PorterStemmer()

        cn = Counter([w for s in sl for w in list(set(s[1:]))])
        st = len(sl) * fr / 100
        self.stopwords = sorted([k for k, v in cn.items() if v > st])
        if uniq:
            self.uniqwords = sorted([k for k, v in cn.items() if v == 1])

        self.feature = [' '.join([stemmer.stem(w) for w in s
                                  if self.__is_useful(w)])
                        for s in sl]

    def __is_useful(self, w):
        ss = self.stopwords
        i, b = bisect_left(ss, w), True
        if i != len(ss) and ss[i] == w:
            b = False
        if hasattr(self, 'uniqwords'):
            us = self.uniqwords
            i = bisect_left(us, w)
            if i != len(us) and us[i] == w:
                b = False
        return b

    def train(self, eta=0.6):
        lr = LogisticRegression(C=eta)
        X = self.vec.fit_transform(self.feature)
        self.model = lr.fit(X, self.polar)

    def predict(self, text):
        vec = self.vec.transform([text])
        pr = self.model.predict_proba(vec)[0]
        if pr[0] > pr[1]:
            return '-1', pr[0]
        else:
            return '+1', pr[1]

