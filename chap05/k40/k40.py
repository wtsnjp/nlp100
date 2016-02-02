import sys

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

file_name = sys.argv[1]
sentences = []

with open(file_name) as f:
    s = []
    for l in f:
        if l == "EOS\n":
            if s != []:
                sentences.append(s)
                s = []
        elif l[0] != "*":
            l = l.replace('\t', ',')
            v = l.split(',')
            m = Morph(v[0], v[7], v[1], v[2])
            s.append(m)
            # s.append({'surface': v[0], 'base': v[7], 'pos': v[1], 'pos1': v[2]})

print(sentences[2])
