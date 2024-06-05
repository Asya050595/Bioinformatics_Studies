import sys
import math
from math import sin, cos

n = int(sys.argv[2])
a = math.radians(n)
b = math.sin(a)
c = math.cos(a)
pum_sin = '{:.4f}'.format(b)
pum_cos = '{:.4f}'.format(c)
text_sin = 'fun({}) = '.format(n)
text_cos = 'fun({}) = '.format(n)
text_error = 'I can’t compute {}({})!'.format(sys.argv[1], n)

if sys.argv[1] == 'sin':
	print(text_sin, pum_sin)
elif sys.argv[1] == 'cos':
	print(text_cos, pum_cos)
else:
	print(text_error)


