import sys
import pydot

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst    = dst
        self.srcs   = []

file_name = sys.argv[1]
sentences, phrases = [], []

with open(file_name) as f:
    s, p = [], []
    for l in f:
        if l == "EOS\n":
            if p != []:
                c = Chunk(p, dst)
                phrases.append(c)
                p = []
            if phrases != []:
                sentences.append(phrases)
                phrases = []
        elif l[0] == "*":
            if p != []:
                c = Chunk(p, dst)
                phrases.append(c)
                p = []
            l_list = l.split(" ")
            dst = int(l_list[2][:-1])
        else:
            l = l.replace('\t', ',')
            v = l.split(',')
            if len(v) == 10:
                m = Morph(v[0], v[7], v[1], v[2])
                p.append(m)

for s in sentences:
    n = 0
    for c in s:
        if c.dst != -1 and c.dst < len(s):
            s[c.dst].srcs.append(n)
        n += 1

pharases = []
dsts = []
for c in sentences[7]:
    p = ""
    for m in c.morphs:
        p += m.surface
    phrases.append(p)
    dsts.append(c.dst)

edges = []
i = 0
for p in phrases:
    pf = phrases[dsts[i]]
    if p != pf:
        edges.append([p, pf])
    i += 1

g = pydot.graph_from_edges(edges)
g.write_png('result.png', prog='dot')




