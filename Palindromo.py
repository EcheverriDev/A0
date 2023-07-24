"""
def palin(palabra:str):
	large=len(palabra)
	revers=[]
	for i in range(large):
		no.append(palabra[-i-1])
	
	
	return list(palabra)==revers
	
print(palin("mam"))
------------------------------------------------------------------------
def palin(palabra):
	x=list(palabra)
	y=list(palabra)
	x.reverse()
	while x.count(" ")>0:
		y.remove(" ")
		x.remove(" ")
                
	return y==x

print(palin("amo la paloma"))
-------------------------------------------------------------------
def palind(pali):

	def delete(palabra:str):
		sin=list(palabra)
		while sin.count(" ")>0:
			sin.remove(" ")
		return sin	

	def rev(arr):
		reves=[]
		for i in range(len(arr)):
			reves.append(arr[-i-1])
		return reves
	
	return rev(delete(pali))==delete(pali)

print(palind("amo la paloma"))

-------------------------------------------------------
def no_space(text):
    sin_espacios=""
    for char in text:
        if char != " ":
            sin_espacios+=char
    return sin_espacios
def es_palindromo(text):
    acron=no_space(text)
    reversa=""
    for char in acron:
        reversa=char+reversa
    print(reversa)

print(es_palindromo("amo la paloma"))
	
"""