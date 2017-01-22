#!/bin/sh
cut -f $1 | sort | uniq -c | sort -rnk1
