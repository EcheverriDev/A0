def calculadora(x,op,y):
    if op=="+":
        return x+y
    elif op=="-":
        return x-y
    elif op=="*":
        return x*y
    elif op=="/":
        return x/y
    elif op=="**":
        return x**y
    elif op=="%":
        return x%y
    else:
        return Exception

ans=0
while True:

    if ans==0:
        x=int(input("./ingrese un numero: "))
        op=input("./ingrese una operacion: ")
        y=int(input("./ingrese otro numero: "))
        
        ans=calculadora(x,op,y)
        print("./ total:", ans)
    else:
        op=input("./ingrese una operacion: ")
        y=int(input("./ingrese otro numero: "))
        
        ans=calculadora(ans,op,y)
        print("./ total:", ans)
    

    