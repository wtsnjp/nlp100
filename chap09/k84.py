#
# usage: python k84.py {N}
#

import sys
import plyvel
from math import log

def wc_matrix(n, ofn):
    co_db = plyvel.DB('./co.ldb', create_if_missing=True)
    word_db = plyvel.DB('./word.ldb', create_if_missing=True)
    context_db = plyvel.DB('./context.ldb', create_if_missing=True)

    x = 0
    ZERO = x.to_bytes((x.bit_length() + 7) // 8, 'big')

    for k, v in co_db:
        tmp = k.decode('utf-8').strip().split('\t')
        if len(tmp) != 2:
            continue

        x = 0

        f_tc = int.from_bytes(v, 'big')
        if f_tc >= 10:
            f_t = int.from_bytes(word_db.get(tmp[0].encode('utf-8'), ZERO), 'big')
            f_c = int.from_bytes(context_db.get(tmp[1].encode('utf-8'), ZERO), 'big')
            x = max(log(2, n * f_tc / (f_t * f_c)), 0)

        if x != 0:
            with open(ofn, 'a') as f:
                f.write('{}\t{}\t{}\n'.format(tmp[0], tmp[1], x))

    co_db.close()
    word_db.close()
    context_db.close()

if __name__ == '__main__':
    N = int(sys.argv[1])
    ofn = 'wc-matrix.txt'

    wc_matrix(N, ofn)
