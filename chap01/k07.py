#
# usage: python k07.py
#

def template(x, y, z):
    return '%s時の%sは%s' % (x, y, z)

if __name__ == '__main__':
    print(template(12, '気温', 22.4))
