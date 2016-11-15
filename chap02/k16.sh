#!/bin/zsh
split -l $2 $1 tmp && echo '' >> tmp* && cat tmp*
