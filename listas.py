Usuarios=[
    [3,"Alguien",123],
    [2,"nadie",234],
    [1,"todos",523],
    [4,"alguno",134]
]
Usuarios.sort(key=lambda id:id[0])# Ordena los Numeros(devuelve la posicion[0] del array)
nombres=[Usuario[1] for Usuario in Usuarios]#Recibe el segundo dato de los array internos
print(Usuarios)
print(nombres)