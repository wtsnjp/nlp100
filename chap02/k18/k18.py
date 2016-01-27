import sys
from operator import itemgetter

file_name = sys.argv[1]
lines = []

with open(file_name) as f:
    for l in f:
        lines.append(l.split())

lines.sort(key=itemgetter(2), reverse=True)

for l in lines:
    print("\t".join(l))
