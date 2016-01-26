import sys

file_name = sys.argv[1]

with open(file_name) as f:
    cnt = 0
    for l in f:
        cnt += 1
    print(cnt)
