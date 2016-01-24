str = """\
Now I need a drink, alcoholic of course,
after the heavy lectures involving quantum mechanics.
"""
words = str.replace('.', '').replace(',', '').split()

list = []

for w in words:
    list.append(len(w))

print(list)
