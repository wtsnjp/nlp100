import sys
import re

file_name = sys.argv[1]

with open(file_name) as f:
    for l in f:
        r = re.compile("ファイル:(.+?)\|")
        m = r.search(l)
        if m:
            print(m.group(1).strip().replace(' ', '_'))
