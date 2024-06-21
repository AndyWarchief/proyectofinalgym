def clasificadorTriangulos(a,b,c):
    if a==b and a==c:
        return "equilatero"
    elif a!=b and a!=c and b!=c:
        return"escaleno"
    else:
        return"isosceles"
la=int(input("ingrese la long del lado a: "))
lb=int(input("ingrese la long del lado b: "))
lc=int(input("ingrese la long del lado c: "))
print(f"el triangulo es {clasificadorTriangulos(la,lb,lc)}")