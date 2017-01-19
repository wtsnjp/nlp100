#
# usage: python k03.py
#

# get lengths of words
def get_low(s):
    t = str.maketrans(".,", "  ")
    ws, l = s.translate(t).split(), []
    for w in ws:
        l.append(len(w))
    return l

if __name__ == '__main__':
    s = """\
    Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics.
    """
    print(get_low(s))
