#area de declaraciones
def dibujarPiramide(caracter, relleno):
    print((caracter*1).center(60,relleno))# esto es lo que imprimimos en pantalla
    print((caracter*3).center(60,relleno))# esto es lo que imprimimos en pantalla
    print((caracter*5).center(60,relleno))# esto es lo que imprimimos en pantalla
    print((caracter*7).center(60,relleno))# esto es lo que imprimimos en pantalla
    print((caracter*9).center(60,relleno))# esto es lo que imprimimos en pantalla
    


#programa principal
car=input("ingrese el car para la piramide: ")
crel=input("con que caracter quieres completar la linea?: ")
dibujarPiramide(car, crel)