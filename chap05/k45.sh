#!/bin/sh
grep "^$1\t" | sort | uniq -c | sort -rnk1
