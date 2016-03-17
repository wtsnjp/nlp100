import sys
from nltk import stem

file_name = sys.argv[1]
stemmer = stem.PorterStemmer()

with open(file_name) as f:
    for l in f:
        l = l.lower().strip()
        l_stem = stemmer.stem(l)
        if l != "":
            print(l, l_stem, sep="\t")
