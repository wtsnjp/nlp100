import sys

lines = int(sys.argv[1])
file_name = sys.argv[2]

with open(file_name) as f:
    cnt = 0
    for l in f:
        if cnt == lines:
            break
        print(l, end='')
        cnt += 1
