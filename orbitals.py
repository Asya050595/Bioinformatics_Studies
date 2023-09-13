import numpy as np
import scipy.special
import scipy.misc
from npy2cube import npy2cube
import py3Dmol

def w(n,l,m,d):

     x,y,z = np.mgrid[-d:d:30j,-d:d:30j,-d:d:30j]

     r = lambda x,y,z: np.sqrt(x**2+y**2+z**2)
     theta = lambda x,y,z: np.arccos(z/r(x,y,z))
     phi = lambda x,y,z: np.arctan(y/x)

     a0 = 1.

     R = lambda r,n,l: (2*r/n/a0)**l * np.exp(-r/n/a0) * scipy.special.genlaguerre(n-l-1,2*l+1)(2*r/n/a0)
     WF = lambda r,theta,phi,n,l,m: R(r,n,l) * scipy.special.sph_harm(m,l,phi,theta)
     absWF = lambda r,theta,phi,n,l,m: np.absolute(WF(r,theta,phi,n,l,m))**2

     res = WF(r(x, y, z), theta(x, y, z), phi(x, y, z), n, l, m)
     return np.real(res) + np.imag(res)

# Зададим цикл по перебору квантовых чисел

for n in range(0,4):
    d = 10 * n
    step = d / 10
    for l in range(0,n):
        for m in range(0,l+1,1):
            grid= w(n, l, m, d)
            name='%s-%s-%s' % (n,l,m)
            # для сохранения нужно задать координаты старта grid и шаг по каждому направлению
            npy2cube(grid, (-d, -d, -d), (step, step, step), f'{name} + .cube')

view = py3Dmol.view()
alpha = open('1-0-0.cube','r').read()
view.addVolumetricData(alpha, "cube", {'isoval': 0.04, 'color': "red", 'opacity': 0.5})
view.zoomTo()
view.show()



