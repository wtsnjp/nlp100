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
            s.append({'surface': v[0], 'base': v[7], 'pos': v[1], 'pos1': v[2]})

for s in sentences:
    l = len(s)
    if l > 1:
        noun = []
        for v in s:
            if v['pos'] == '名詞':
                noun.append(v['surface'])
            else:
                if len(noun) > 2:
                    print(''.join(noun))
                noun = []
