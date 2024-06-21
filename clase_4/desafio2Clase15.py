codigo=input("ingrese el producto: ")
cod=codigo[0].upper()
match cod:
    case "A":
        print("Electronicos")
    case "B":
        print("Indumentaria")
    case "C":
        print("Alimentos")
    case _:
        print("codigo desconocido...")