#!/bin/sh
wget -q "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz"
tar zxf rt-polaritydata.tar.gz
nkf -w rt-polaritydata/rt-polarity.pos > rt-polarity.pos
nkf -w rt-polaritydata/rt-polarity.neg > rt-polarity.neg
python k70.py rt-polarity.pos rt-polarity.neg sentiment.txt > /dev/null
rm -rf rt-polarity*
