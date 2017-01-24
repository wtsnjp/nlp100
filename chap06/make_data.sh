#!/bin/sh
wget -q "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt"
wget -q "http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip"
unzip -q stanford-corenlp-full-2016-10-31.zip
java -cp "./stanford-corenlp-full-2016-10-31/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt > /dev/null 2>&1
rm -rf stanford-corenlp-full-2016-10-31*
