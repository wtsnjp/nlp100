import sys
import re

file_name = sys.argv[1]
kiso = False
kiso_list = []
kiso_dict = {}

with open(file_name) as f:
    r1 = re.compile("\{\{基礎情報")
    r2 = re.compile("\}\}")
    r3 = re.compile("\|")
    r4 = re.compile("<ref(\s|>).+?(</ref>|$)")
    for l in f:
        if kiso:
            m1 = r2.match(l)
            m2 = r3.match(l)
            if m1:
                break
            if m2:
                l = re.sub(r"'+", '', l)
                l = re.sub(r'\[\[(.+\||)(.+?)\]\]', r'\2', l)
                l = re.sub(r'\{\{(.+\||)(.+?)\}\}', r'\2', l)
                l = re.sub(r'<\s*?/*?\s*?br\s*?/*?\s*>', '', l)
                kiso_list.append(r4.sub('', l.strip()))
        m = r1.match(l)
        if m:
            kiso = True

r = re.compile("\|(.+?)\s=\s(.+)")
for c in kiso_list:
    m = r.match(c)
    kiso_dict[m.group(1)] = m.group(2)

del kiso_dict['注記']

for k in kiso_dict:
    print(k, kiso_dict[k], sep=": ")
