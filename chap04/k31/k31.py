import sys

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

for s in sentences:
    for m in s:
        if m['pos'] == '動詞':
            print(m['surface'])
