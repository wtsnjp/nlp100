#
# usage: python k05.py
#

def str2wl(src):
    return [s.split() for s in src.rstrip('.').split('.')]

def str2cl(src):
    return [list(w) for w in [''.join([c for c in w if c.isalnum()]) for w in src.split()]]

def n_gram(n, gl):
    return [g[i:i+n] for g in gl for i in range(len(g)-n+1) if len(g) >= n]

if __name__ == '__main__':
    s1 = 'I am an NLPer'
    s2 = 'I want to be a TeXnician. I love TeX.'

    print(n_gram(2, str2wl(s1)))
    print(n_gram(2, str2cl(s1)))
