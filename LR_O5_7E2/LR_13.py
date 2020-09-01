import math as m

def func(x):
	return m.e**2+m.sqrt(1+m.e**(2*x))-2

def add(a, b):
	eps = 1e-4
	array = []
	while m.fabs(a - b) > eps:
		c = (a + b) / 2.0
		fa = func(a)
		fb = func(b)
		if (fa < 0 and fb < 0) or (fa > 0 and fb > 0):
			b = c
		else:
			a = c
	return c

print(add(-1,0))