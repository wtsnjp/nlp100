#
# usage: python k44.py {file name} {number}
#

import sys
import pydot
from k41 import *
from k42 import get_relation_pairs

if __name__ == '__main__':
    fn, nos = sys.argv[1], int(sys.argv[2])
    sl = load_cabocha(fn)
    pl = get_relation_pairs([sl[nos-1]])

    g = pydot.graph_from_edges(pl)
    g.write_png('result.png', prog='dot')
