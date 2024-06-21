dia=int(input("ingrese el num del dia de la semana"))
match dia:
    case 1:
        print("domingo")
    case 2:
        print("lunes")
    case 3 | 4 | 5 | 6:
        print("estamos a media semana")
    case 7:
        print("sabado")
    case _:
        print("error")