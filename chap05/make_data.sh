#!/bin/sh
wget -q "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt"
cabocha -f1 neko.txt > neko.txt.cabocha
rm neko.txt
