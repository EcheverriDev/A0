def vocal(c):
	"""
	Dada una letra decide si es vocal o no

	Args:
	c (chr):Letra a comparar
	Returns:
	True si es vocal o False si es consonante
	"""
	vocals=["a","e","i","o","u"]
	return c in vocals

print(vocal(2))