#
# usage: python k09.py
#

from random import randint

def typoglycemia(src):
    swl, owl = src.split(), []
    for w in swl:
        l, w = len(w), list(w)
        while l > 3:
            x, y = [randint(1, l-2) for i in range(2)]
            if x == y: break
            w[x], w[y] = w[y], w[x]
        owl.append("".join(w))
    return " ".join(owl)

if __name__ == '__main__':
    src = """\
    I couldn't believe that I could actually understand what I was reading :
    the phenomenal power of the human mind .
    """

    print(typoglycemia(src))

