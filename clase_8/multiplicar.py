def tabla_de_multiplicar(numero):   
    if 0 < numero and numero <= 10:
        contador = 1
        while contador <= 10:
            resultado = numero * contador
            print(f"{numero} x {contador} = {resultado}")
            contador += 1
    else:
        print("El número debe estar entre 0 y 10.")
    return
def tablaMultiplicarFor(numero):
    coleccion="hola a todos"
    # for i in [1,2,3,4,5,6,7,8,9,10]:
    # for i in range(1,10):
    for e in coleccion:
        print(e)
        return

num=int(input("ingrese un num may a 0 y men 11"))    
# tabla_de_multiplicar(num)
tablaMultiplicarFor(num)
