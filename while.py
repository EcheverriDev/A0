import math

n=int(input("ingrese un numero para la raiz: "))
trys=0

while n<0:
    print("Numero invalido")
    trys=trys+1
    
    if trys>4:
        print("programa finalizado")
        break
    n=int(input("ingrese un numero para la raiz: "))

print(f" la raiz es: {math.sqrt(n)}")