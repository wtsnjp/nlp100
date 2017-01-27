#
# usage: python k08.py
#

def cipher(src):
    return ''.join([chr(219-ord(c)) if 96 < ord(c) < 123 else c for c in src])

if __name__ == '__main__':
    ecd = cipher('Hello world!')
    dcd = cipher(ecd)
    print(ecd, dcd)
