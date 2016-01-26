lines=`wc -l $2 | grep -o '[0-9].'`
split -l `expr $lines / $1` $2 check-
