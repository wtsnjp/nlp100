import sys
import re

file_name = sys.argv[1]

with open(file_name) as f:
    for l in f:
        l = re.sub(r'\t', ' ', l)
        print(l, end='')
