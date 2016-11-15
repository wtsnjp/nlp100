#!/bin/sh
cut -f $2 $1 | LANG=C sort | uniq
