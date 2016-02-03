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

count_dict = collections.Counter(tango)
count_list = []

for k,v in count_dict.most_common():
    count_list.append(v/len(count_dict))

plt.hist(count_list, 50, range=(0.0, 0.01))
plt.xlabel("出現頻度")
plt.ylabel("種類数")
plt.savefig("result.png")
