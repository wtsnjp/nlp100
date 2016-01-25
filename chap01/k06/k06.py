str1 = "paraparaparadise"
str2 = "paragraph"
words1 = str1.split()
words2 = str2.split()

def n_gram(list, type):
    bi_gram = []
    if type == 'char':
        for w in list:
            l = len(w)
            if l > 1:
                for i in range(l):
                    if i != 0:
                        bi_gram.append(w[i-1:i+1])
    if type == 'word':
        l = len(list)
        if l != 0:
            for i in range(l):
                if i != 0:
                    bi_gram.append('-'.join(list[i-1:i+1]))
    return bi_gram

X = set(n_gram(words1, 'char'))
Y = set(n_gram(words2, 'char'))

# sets
print("X =", X)
print("Y =", Y)
# sum
print("X+Y =", X.union(Y))
# product
print("X*Y =", X.intersection(Y))
# diff
print("X-Y =", X.difference(Y))
# include 'se' or not
print("X include 'se':", 'se' in X)
print("Y include 'se':", 'se' in Y)

