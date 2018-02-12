#
# usage: python k84.py {N}
#

import sys
import plyvel
import struct
from math import log

def create_matrix(n):
    co_db = plyvel.DB('./co.ldb', create_if_missing=True)
    word_db = plyvel.DB('./word.ldb', create_if_missing=True)
    context_db = plyvel.DB('./context.ldb', create_if_missing=True)
    matrix_db = plyvel.DB('./matrix.ldb', create_if_missing=True)

    for k, v in co_db:
        tmp = k.decode('utf-8').strip().split('\t')
        if len(tmp) != 2:
            continue

        x = 0

        f_tc = int.from_bytes(v, 'big')
        if f_tc >= 10:
            f_t = int.from_bytes(word_db.get(tmp[0].encode('utf-8')), 'big')
            f_c = int.from_bytes(context_db.get(tmp[1].encode('utf-8')), 'big')
            x = max(log(2, n * f_tc / (f_t * f_c)), 0)

        if x != 0:
            matrix_db.put(k, struct.pack('>d', x))

    co_db.close()
    word_db.close()
    context_db.close()
    matrix_db.close()

def get_matrix(t, c):
    matrix_db = plyvel.DB('./matrix.ldb', create_if_missing=True)
    t_key = '\t'.join((t, c)).encode('utf-8')
    v = float(struct.unpack('>d', matrix_db.get(t_key))[0])
    matrix_db.close()

    print('X("{}", "{}") = {}'.format(t, c, v))

if __name__ == '__main__':
    N = int(sys.argv[1])

    create_matrix(N)
    get_matrix('of', 'a')
