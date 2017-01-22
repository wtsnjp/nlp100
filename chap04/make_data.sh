#!/bin/sh
wget -q "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt"
mecab neko.txt > neko.txt.mecab
rm neko.txt
