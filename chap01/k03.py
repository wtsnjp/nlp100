#
# usage: python k03.py
#

# get lengths of words
def get_low(s):
    return [len(w) for w in [''.join([c for c in w if c.isalnum()]) for w in s.split()]]

if __name__ == '__main__':
    s = '''\
    Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics.
    '''
    print(get_low(s))
