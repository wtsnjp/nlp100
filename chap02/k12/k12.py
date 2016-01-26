import sys

col_num = int(sys.argv[1])
file_name = sys.argv[2]

with open(file_name) as f:
    for l in f:
        a = l.split()
        print(a[col_num-1])
