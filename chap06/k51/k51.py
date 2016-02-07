import sys
import re

file_name = sys.argv[1]

with open(file_name) as f:
    for l in f:
        sen = l.split(" ")
        for w in sen:
            w = re.sub(r"[^a-zA-Z]", "", w)
            print(w)
        print()
