import sys

file_name = sys.argv[1]
ken_set = set()

with open(file_name) as f:
    for l in f:
        a = l.split()
        ken_set.add(a[0])

ken_list = sorted(list(ken_set))

for e in ken_list:
    print(e)
