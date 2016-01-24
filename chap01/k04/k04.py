str = """\
Hi He Lied Because Boron Could Not Oxidize Fluorine.
New Nations Might Also Sign Peace Security Clause. Arthur King Can.
"""
words = str.replace('.', '').replace(',', '').split()

dict = {}
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
cnt = 1

for w in words:
    if cnt in num_list:
        dict[w] = w[0]
    else:
        dict[w] = w[0:2]
    cnt += 1

print(dict)
