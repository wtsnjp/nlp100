#
# usage: python k02.py
#

def alt_cat(s1, s2):
    ln = len(s1) if len(s1) < len(s2) else len(s2)
    return ''.join([s1[i] + s2[i] for i in range(ln)]) + s1[ln:] + s2[ln:]

if __name__ == '__main__':
    print(alt_cat('パトカー', 'タクシー'))
