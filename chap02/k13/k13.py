import sys

col_file1 = sys.argv[1]
col_file2 = sys.argv[2]

with open(col_file1) as f:
    a = []
    for l in f:
        a.append(l.rstrip())

with open(col_file2) as f:
    cnt = 0
    for l in f:
        print(a[cnt], l, sep="\t", end="")
        cnt += 1
