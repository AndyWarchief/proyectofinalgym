import os
import datetime
razonSocial=input("ingrese la razon social del cliente: ")
domicilio=input("ingrese el domicilio: ")
articulo=input("ingrese el articulo: ")
cantidad=int(input("ingrese la cantidad: "))
precioUnitario=float(input("ingrese el precio unitario: "))
importe=cantidad * precioUnitario
descuento=float(input("ingrese el descuento en $: "))
iva=(importe*21)/100
totalAPagar=(importe+iva)-descuento
os.system("cls")
print("datos del cliente: ".upper())
print("razon social: ".title() + razonSocial)
print("domicilio: ".capitalize() + domicilio)
print()
print("detalles de la compra: ".upper())
print("Cantidad" + "\tDescripcion".ljust(25," ")+ "\tP.U".ljust(10," ") + "\tSub-Total" )
print(str(cantidad).ljust(8," ") + "\t" + str(articulo).ljust(25," ") + "\t" + str(precioUnitario).ljust(25," ") + "\t" + str(importe).ljust(25," "))
print()
print("calculos adicionales: ".upper())
print("iva (21%)".upper(), end=" ")
print("$: ", iva)
print("descuento aplicado".title(), end=" ")
print("-$: ", descuento)
print(f"Total $: {totalAPagar}")