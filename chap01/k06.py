#
# usage: python k06.py
#

from k05 import str2cl, n_gram

if __name__ == '__main__':
    s1 = 'paraparaparadise'
    s2 = 'paragraph'

    X = set(map(''.join, n_gram(2, str2cl(s1))))
    Y = set(map(''.join, n_gram(2, str2cl(s2))))
    
    # sets
    print('X =', X)
    print('Y =', Y)

    # sum, product, diff
    print('X + Y =', X.union(Y))
    print('X * Y =', X.intersection(Y))
    print('X - Y =', X.difference(Y))

    # include 'se' or not
    print('X include \'se\':', 'se' in X)
    print('Y include \'se\':', 'se' in Y)
