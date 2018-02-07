#!/bin/sh
wget -q "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2"
bunzip2 enwiki-20150112-400-r10-105752.txt.bz2
wget -q "https://pkgstore.datahub.io/core/country-list/data_csv/data/d7c9d7cfb42cb69f4422dec222dbbaa8/data_csv.csv"
mv data_csv.csv countries.csv
