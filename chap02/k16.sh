#!/bin/sh
n=`cat $1 | gwc -l`
ln=`expr $n / $2`
split -l $ln $1 tmp
files="tmp*"

c=0
for f in $files; do
  c=`expr $c + 1`
  cat $f
  if [ $c -lt $2 ]; then
    echo
  fi
done

rm tmp*
