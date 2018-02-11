#
# usage: python k84.py {context file}
#

import sys
import plyvel

def count_context(fn):
    co_db = plyvel.DB('./co.ldb', create_if_missing=True)
    word_db = plyvel.DB('./word.ldb', create_if_missing=True)
    context_db = plyvel.DB('./context.ldb', create_if_missing=True)

    s = 0
    ZERO = s.to_bytes((s.bit_length() + 7) // 8, 'big')
    
    for l in open(fn):
        tmp = list(map(lambda s: s.strip(), l.split('\t')))
        if len(tmp) != 2:
            continue

        # f(t, c)
        t_key = '\t'.join(tmp).encode('utf-8')
        i = int.from_bytes(co_db.get(t_key, ZERO), 'big') + 1
        co_db.put(t_key, i.to_bytes((i.bit_length() + 7) // 8, 'big'))

        # f(t, *)
        t_key = tmp[0].encode('utf-8')
        i = int.from_bytes(word_db.get(t_key, ZERO), 'big') + 1
        word_db.put(t_key, i.to_bytes((i.bit_length() + 7) // 8, 'big'))

        # f(*, c)
        t_key = tmp[1].encode('utf-8')
        i = int.from_bytes(context_db.get(t_key, ZERO), 'big') + 1
        context_db.put(t_key, i.to_bytes((i.bit_length() + 7) // 8, 'big'))

        # N
        s += 1

    co_db.close()
    word_db.close()
    context_db.close()

    return s

def show_result(t, c):
    i = 0
    ZERO = i.to_bytes((i.bit_length() + 7) // 8, 'big')

    if c == '*':
        word_db = plyvel.DB('./word.ldb', create_if_missing=True)
        t_key = t.encode('utf-8')
        i = int.from_bytes(word_db.get(t_key, ZERO), 'big')
        print('f("{}", *) = {}'.format(t, i))
        word_db.close()
    elif t == '*':
        context_db = plyvel.DB('./context.ldb', create_if_missing=True)
        t_key = c.encode('utf-8')
        i = int.from_bytes(context_db.get(t_key, ZERO), 'big')
        print('f(*, "{}") = {}'.format(c, i))
        context_db.close()
    else:
        co_db = plyvel.DB('./co.ldb', create_if_missing=True)
        t_key = '\t'.join((t, c)).encode('utf-8')
        i = int.from_bytes(co_db.get(t_key, ZERO), 'big')
        print('f("{}", "{}") = {}'.format(t, c, i))
        co_db.close()

if __name__ == '__main__':
    fn = sys.argv[1]

    s = count_context(fn)

    show_result('of', 'a')
    show_result('of', '*')
    show_result('*', 'a')
    print('N = {}'.format(s))
