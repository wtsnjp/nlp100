import random

str = """\
I couldn't believe that I could actually understand what I was reading :
the phenomenal power of the human mind .
"""
words = str.split()

for i in range(len(words)):
    w = list(words[i])
    l = len(w)
    if l > 3:
        while True:
            x, y = random.randint(1, l-2), random.randint(1, l-2)
            if x == y:
                break
            w[x], w[y] = w[y], w[x]
    words[i] = ''.join(w)

print(' '.join(words))
