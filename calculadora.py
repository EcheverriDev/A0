
while(True):
	x=int(input("ingrese numero x: "))
	y=int(input("ingrese numero y: "))
	z=int(input("ingrese una operacion \n 1.sumar \n 2.restar \n 3.multiplicar \n 4.dividir \n"))
	match z:
		case 1:	
			print("la suma es:", x+y)
		case 2:
			print("la resta es:", x-y)
		case 3:
			print("la multiplicacion es:", x*y)
		case 4:
			print("la division es:", x/y)
	a=int(input("¿Desea continuar? \n 1.si 2.no \n"))
	if a==2:
		print("Programa finalizado")
		break		
