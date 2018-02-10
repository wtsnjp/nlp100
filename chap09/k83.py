#
# usage: python k84.py {context file}
#

import sys
import random

def sum_tc(fn, t, c):
    s = 0
    for l in open(fn):
        tmp = list(map(lambda s: s.strip(), l.split('\t')))
        if len(tmp) == 2:
            if tmp[0] == t and tmp[1] == c:
                s += 1
    return s

def sum_t(fn, t):
    s = 0
    for l in open(fn):
        tmp = list(map(lambda s: s.strip(), l.split('\t')))
        if len(tmp) == 2:
            if tmp[0] == t:
                s += 1
    return s

def sum_c(fn, c):
    s = 0
    for l in open(fn):
        tmp = list(map(lambda s: s.strip(), l.split('\t')))
        if len(tmp) == 2:
            if tmp[1] == c:
                s += 1
    return s

def count_context(fn):
    s = 0
    for l in open(fn):
        s += 1
    return s

if __name__ == '__main__':
    fn = sys.argv[1]

    print('f("is", "a") = {}'.format(sum_tc(fn, 'is', 'a')))
    print('f("is", *) = {}'.format(sum_t(fn, 'is')))
    print('f(*, "a") = {}'.format(sum_c(fn, 'a')))
    print('N = {}'.format(count_context(fn)))
