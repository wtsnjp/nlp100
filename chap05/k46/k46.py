import sys

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

for s in sentences:
    for c in s:
        for m in c.morphs:
            if m.pos == "動詞":
                verb = m.base
                pps, chs = [], []
                for i in c.srcs:
                    ch = []
                    pps_exist = False
                    for m_i in s[i].morphs:
                        if m_i.pos != "記号":
                            ch.append(m_i.surface)
                        if m_i.pos == "助詞":
                            pps.append(m_i.base)
                            pps_exist = True
                    if pps_exist:
                        chs.append("".join(ch))
                if pps != []:
                    print(verb, " ".join(pps), " ".join(chs), sep="\t")
                break
