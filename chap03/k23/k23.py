import sys
import re

file_name = sys.argv[1]

with open(file_name) as f:
    for l in f:
        r = re.compile("(=+)(.*?)=+")
        m = r.match(l)
        if m:
            print(m.group(2).strip(), len(m.group(1))-1)
