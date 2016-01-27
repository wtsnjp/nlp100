import sys
import gzip
import json

file_name = sys.argv[1]

f = gzip.open(file_name, 'rb')
data = f.read().decode('utf-8')
f.close()

article_dict = {}
for l in data.splitlines():
    line_dict = json.loads(l)
    article_dict[line_dict['title']] = line_dict

print(article_dict[u'イギリス']['text'])
