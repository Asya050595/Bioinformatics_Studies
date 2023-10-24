#Не мой код
#Механика — раздел физики, изучающий механическое движение. Суть задания состоит в
#определении констант ковалентных взаимодействий для молекулярной механики на основе
#квантово-химических расчётов.
#Задание не удалось выполнить в Google Colab из-за проблем совместимости пакета psi4 и
#окружения conda. Практикум выполнен в Jupiter Notebook (PyCharm).
#Как скачать psi4 в PyCharm:
#1. Сделать новый Project в conda environment.
#2. Запустить в терминале: «conda install psi4 python=3.11 -c conda-forge/label/libint_dev -c conda-forge»
#Обрати внимание, версия python 3.11 -- есть варианты для разных версий питона.
#Ориентировка по сайту https://psicode.org/installs/v16/ (внимательно к версиям Python!)

import psi4
import numpy as np
import jupyter
psi4.core.set_output_file('output.dat')
def run_psi4(inp):
m = psi4.geometry(inp)
psi4.set_options({"maxiter": 200, "fail_on_maxiter" : True})
x = psi4.energy('scf/cc-pvtz', molecule = m )
return x
inp = '''
C
C 1 1.52986
H 1 1.08439 2 111.200
H 1 1.08439 2 111.200 3 120
H 1 1.08439 2 111.200 3 -120
H 2 1.08439 1 111.200 3 180
H 2 1.08439 1 111.200 6 120
H 2 1.08439 1 111.200 6 -120
'''
import py3Dmol
view = py3Dmol.view()
my_image = view.addModel(psi4.geometry(inp).save_string_xyz_file(),'xyz')
view.show()
from IPython.display import Image
my_image.Image(filename='someimage.jpg')

# Результат — визуализация оптимизированной структуры этана.

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
# fake x array , replace with real one
x_o=np.arange(1,2,0.1)
# fake y array, replace with energies
y_o=-70+2*(x_o -1.58)**2
#function is f(x)=k(b-x)^2 + a
fitfunc = lambda p, x: p[0]*pow(p[1]-x,2) + p[2] # Target function
errfunc = lambda p, x, y: fitfunc(p, x) - y # Error function
p0 = [1,1, -79] # Initial guess for the parameters
p1, success = optimize.leastsq(errfunc, p0[:], args=(x_o, y_o))
print("Optimized params:", p1)
#Plot it
plt.plot(x_o, y_o, "ro", x_o,fitfunc(p1,x_o),"r-",c='blue',alpha=0.5)
plt.xlim(1,2)
plt.show()

# Результат -- зависимость энергии молекулы от длины одной связи.

fitfunc = lambda p, x: p[2]* ( (1 - np.exp(-p[1]*(x-p[0])))**2 ) # Morze potential f(x) = c * ( 1 - exp(-a(x-b)) )^2
errfunc = lambda p, x, y: fitfunc(p, x) - y
p0 = [-1.5, 1, -79] # Initial guess for the parameters
p1, success = optimize.leastsq(errfunc, p0[:], args=(x_o, y_o))
print("Optimized params:", p1)

# Результат -- зависимость энергии молекулы от длины связи C-C, вычисляемой по
формуле Morze potential f(x).

#Plot it
plt.plot(x_o, y_o, "b-", label='real', alpha=0.5)
plt.plot(x_o, fitfunc(p1,x_o), "r-", alpha=0.5, label='fit')
plt.xlabel('Длина связи C-C')
plt.ylabel('Энергия')
plt.legend()
plt.show()












