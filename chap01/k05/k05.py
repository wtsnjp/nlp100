str = "I am an NLPer"
words = str.split()

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

print(n_gram(words, 'char'))
print(n_gram(words, 'word'))

