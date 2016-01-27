import sys
import collections

file_name = sys.argv[1]
ken_list = []

with open(file_name) as f:
    for l in f:
        a = l.split()
        ken_list.append(a[0])

count_dict = collections.Counter(ken_list)
for k,v in count_dict.most_common():
    print("   %d %s" % (v,k))
