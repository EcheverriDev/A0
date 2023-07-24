def calculator():
    n1=0
    n2=0
    
    while True:
        try:
            n1=int(input("ingrese parametro 1: "))
            break
        except ValueError:
            print("ingrese un numero")
    
    while True:
        try:
            n2=int(input("ingrese parametro 2: "))
            break
        except ValueError:
            print("ingrese un numero")
    
    while True:
        operacion=input("Ingrese una operacion: ")

        if operacion=="sumar":
            return n1+n2
            break
        elif operacion=="restar":
            return n1-n2
            break
        elif operacion=="multiplicar":
            return n1*n2
            break
        elif operacion=="dividir":
            try:
                return n1/n2
                break
            except ZeroDivisionError:
                print("no se puede dividir entre 0")
        else:
            print("operacion invalida")

print(calculator())


