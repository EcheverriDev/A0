def maximo(a,b,c):
	"""
	recibe 3 numeros y devuelve el mayor de ellos

	Args:
	a (int)=primer numero a comparar
	b (int)=segundo numero a comparar
	c (int)=tercer numero a comparar
	
	returns:
	int: el mayor de los 3 numeros
	"""
	if a==b or b==c:
		if b>c or b>a:
			return b
		elif c>b:
			return c
		else:
			return a
	elif a!=b and b!=c:
		if a>b:
			if a>c:
				return a
			else:
				return c
		else:
			if b>c:
				return b
			else:
				return c 
	else:
		raise Exception("solo recibe numeros")

print(maximo(90,90,80))
