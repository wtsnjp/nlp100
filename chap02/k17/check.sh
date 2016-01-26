cut -f 1 $1 | LANG=C sort | uniq | tee check.txt
