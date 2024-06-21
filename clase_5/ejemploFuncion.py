#area de declaraciones
def sumar(pn,sn):
    res=int(pn) + int(sn)
    # print(f"si sumamos {pn} y {sn} obtenemos : {res}")
    return res


#inicio del pro0grama principal
pv = int(input("ingrese un prmer valor: "))
sv = int(input("ingrese un segundo valor: "))
# sumar(pv,sv)
resultado=sumar(pv,sv)
print(f"si sumamos {pv} y {sv} obtenemos: {resultado}")
