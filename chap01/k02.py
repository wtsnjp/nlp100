#
# usage: python k02.py
#

def alt_cat(s1, s2):
    s, l1, l2 = "", len(s1), len(s2)
    ls = l1 if l1<l2 else l2
    for i in range(ls):
        s += s1[i] + s2[i]
    return s + s1[ls:] + s2[ls:]

if __name__ == '__main__':
    print(alt_cat("パトカー", "タクシー"))

