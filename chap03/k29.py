#
# usage: python k29.py {file name} {article title} {template name}
#

import sys
import re
import requests
from k20 import load_article
from k25 import template2dict
from k28 import remove_markups

def get_flag_url(dc):
    url_base = 'https://commons.wikimedia.org/w/api.php?'
    url_prefix = 'action=query&titles=File:'
    url_file = dc['国旗画像'].replace(' ', '_')
    url_suffix = '&prop=imageinfo&iiprop=url&format=json'
    url = url_base + url_prefix + url_file + url_suffix

    data = requests.get(url)
    return re.search(r'"url":"(.+?)"', data.text).group(1)

if __name__ == '__main__':
    fn, title, template = sys.argv[1:]
    article = load_article(fn, title)
    dc = remove_markups(template2dict(article, template))
    print(get_flag_url(dc))
