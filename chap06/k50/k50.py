import sys
import re

file_name = sys.argv[1]

sen_list = []
with open(file_name) as f:
    for l in f:
        if not l == "\n":
            sen_list.append(l)

text = ''.join(sen_list)
text = re.sub(r"\n+", " ", text)

sen_list = re.sub(r"(\.|;|\?|\!)\s([A-Z])", r"\1@@@\2", text).split("@@@")
for s in sen_list:
    print(s)
