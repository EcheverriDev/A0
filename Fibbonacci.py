def fib(z:int):
	"""
	Recibe un entero y devuelve la secuencia de fibbonacci hasta esa iteracion
	Args:
	z(int):numero de iteraciones a realizar
	Returns:
	x[int]:secuencia de fibbonacci
	"""
	x=[0,1]
	for i in range(z):
			x.append(x[-1]+x[-2])
	return x
print(fib(1000))	