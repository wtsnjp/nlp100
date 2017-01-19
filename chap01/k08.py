#
# usage: python k08.py
#

def cipher(src):
    ecd = ""
    for w in src:
        c = ord(w)
        if 96 < c < 123:
            c = 219 - c
        ecd += chr(c)
    return ecd

if __name__ == '__main__':
    ecd = cipher("Hello world!")
    dcd = cipher(ecd)
    print(ecd, dcd)
