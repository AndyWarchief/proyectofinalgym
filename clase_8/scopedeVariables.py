def funcion1():
    """autor: Sergio Serbluk
    funcion1 esta funcion pretende demostrar el uso de variables globales 
    no recibe parametros
    no devuelve resusltados
    """
    global a
    global b
    b=a
    a=3
    print(a)
    return
#prog princ
a="si"
funcion1()
print(b)
print(help(funcion1))