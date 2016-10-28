#
# usage: python k05.py
#

def str2wlist(src):
    wl = []
    for s in src.rstrip(".").split("."):
        wl.append(s.split())
    return wl

def str2clist(src):
    cl = []
    t = str.maketrans(".", " ")
    for w in src.translate(t).split():
        cl.append(list(w))
    return cl

def n_gram(n, gl):
    ngl = []
    for g in gl:
        l = len(g)
        if l >= n:
            for i in range(l-n+1):
                ngl.append(g[i:i+n])
    return ngl

if __name__ == '__main__':
    s1 = "I am an NLPer"
    s2 = "I want to be a TeXnician. I love TeX."

    print(n_gram(2, str2wlist(s1)))
    print(n_gram(2, str2clist(s1)))

