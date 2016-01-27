import sys
import re

file_name = sys.argv[1]

with open(file_name) as f:
    for l in f:
        r = re.compile("\[\[Category:(.*?)(\|.*\]\]|\]\])")
        if r.match(l):
            m = r.match(l)
            print(m.group(1))
