import sys

lines = int(sys.argv[1])
file_name = sys.argv[2]
data = []

with open(file_name) as f:
    for l in f:
        data.append(l.strip())

for l in data[-lines:]:
    print(l)

