import sys
import collections

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
            s.append({'surface': v[0], 'base': v[7], 'pos': v[1], 'pos1': v[2]})

tango = []

for s in sentences:
    for v in s:
        tango.append(v['base'])

count_dict = collections.Counter(tango)
for k,v in count_dict.most_common():
    print("%d %s" % (v,k))
