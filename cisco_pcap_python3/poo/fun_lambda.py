def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

#Se sustituye con lambda
def poli(x):
	return 2 * x**2 - 4 * x + 2

imprimirfuncion([x for x in range(-2, 3)], poli)
imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
