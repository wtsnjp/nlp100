#!/bin/sh
wget -q "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz"
tar zxvf rt-polaritydata.tar.gz
python k70.py rt-polaritydata/rt-polarity.pos rt-polaritydata/rt-polarity.neg sentiment.txt
rm -rf rt-polarity*
