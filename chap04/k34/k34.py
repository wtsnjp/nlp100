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
    l = len(s)
    if l > 2:
        for i in range(2, l-1):
            if s[i-2]['pos'] == '名詞' and s[i-1]['surface'] == 'の' and s[i]['pos'] == '名詞':
                print(s[i-2]['surface'], s[i-1]['surface'], s[i]['surface'], sep='')
