#!/bin/sh
cut -f $2 $1 | sort | uniq -c | sort -nr | cut -d' ' -f 5
