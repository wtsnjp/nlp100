import sys
import collections
from matplotlib import pyplot as plt

NUM = 10

file_name = sys.argv[1]

sentences = []

with open(file_name) as f:
    s = []
    for l in f:
        if l == "EOS\n":
            if s != []:
                sentences.append(s)
                s = []
        else:
            l = l.replace('\t', ',')
            v = l.split(',')
            if len(v) == 10:
                s.append({'surface': v[0], 'base': v[7], 'pos': v[1], 'pos1': v[2]})

tango = []

for s in sentences:
    for v in s:
        tango.append(v['base'])

cnt = 0
k_list = []
v_list = []
d_list = range(1, NUM+1)

count_dict = collections.Counter(tango)
for k,v in count_dict.most_common():
    k_list.append(k)
    v_list.append(v)
    cnt += 1
    if cnt == NUM:
        break

plt.bar(d_list, v_list, align="center")
plt.xticks(d_list, k_list)
plt.savefig("result.png")
