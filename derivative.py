import sys
import math
import scipy.integrate
from scipy.integrate import quad



numbers = [int(arg) for arg in sys.argv[1:]]

newfile = open("output-deriv.txt", "w")
newfile.write("x        f       f'" + '\n')


for i in numbers:
    a = math.log1p(i**2)
    b = (1+i**2)/1
    newfile.write(f'{i}        {a}       {b}' + '\n')

