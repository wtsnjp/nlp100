#
# usage: python k04.py
#

ses = 'H B C N O F P S K V Y I U'.split()
des = '''\
He Li Be Ne Na Mg Al Si Cl Ar Ca Sc Ti Cr Mn Fe Co Ni Cu Zn
Ga Ge As Se Br Kr Rb Sr Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb
Te Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf
Ta Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa Np Pu
Am Cm Bk Cf Es Fm Md No Lr
'''.split()

def elements(s):
    wl, wd = [''.join([c for c in w if c.isalnum()]) for w in s.split()], {}
    for i in range(len(wl)):
        if wl[i][:2] in des:
            wd[wl[i]] = wl[i][:2]
        elif wl[i][0] in ses:
            wd[wl[i]] = wl[i][0]
    return wd

if __name__ == '__main__':
    s = '''\
    Hi He Lied Because Boron Could Not Oxidize Fluorine.
    New Nations Might Also Sign Peace Security Clause. Arthur King Can.
    '''

    print(elements(s))
