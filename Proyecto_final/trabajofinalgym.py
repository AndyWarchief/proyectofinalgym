from colorama import init, Fore, Style

# Inicializar colorama
init()

# Diccionario para almacenar los datos de los socios del gimnasio
socios = {}

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("\n*** Menú de Opciones ***")
    print("1. " + Fore.GREEN + "Agregar socio" + Style.RESET_ALL)
    print("2. " + Fore.YELLOW + "Listar socios" + Style.RESET_ALL)
    print("3. " + Fore.CYAN + "Buscar socio por nombre" + Style.RESET_ALL)
    print("4. " + Fore.RED + "Eliminar socio por número de socio" + Style.RESET_ALL)
    print("5. " + Fore.MAGENTA + "Salir" + Style.RESET_ALL)
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    return opcion

# Función para agregar un nuevo socio al diccionario
def agregar_socio():
    num_socio = input("Ingrese el número de socio: ")
    nombre = input("Ingrese el nombre del socio: ")
    edad = input("Ingrese la edad del socio: ")
    plan = input("Ingrese el plan del socio (por ejemplo, básico, premium, etc.): ")
    socios[num_socio] = {'nombre': nombre, 'edad': edad, 'plan': plan}
    print(Fore.GREEN + "¡Socio agregado correctamente!" + Style.RESET_ALL)

# Función para listar todos los socios en el diccionario
def listar_socios():
    print("\n" + Fore.YELLOW + "Listado de Socios:" + Style.RESET_ALL)
    for num_socio, info in socios.items():
        print(f"Número de Socio: {num_socio}, Nombre: {info['nombre']}, Edad: {info['edad']}, Plan: {info['plan']}")

# Función para buscar un socio por nombre
def buscar_socio():
    nombre_buscar = input("Ingrese el nombre del socio que desea buscar: ")
    encontrado = False
    for num_socio, info in socios.items():
        if nombre_buscar.lower() in info['nombre'].lower():
            print(Fore.CYAN + f"Socio encontrado:" + Style.RESET_ALL)
            print(f"Número de Socio: {num_socio}, Nombre: {info['nombre']}, Edad: {info['edad']}, Plan: {info['plan']}")
            encontrado = True
    if not encontrado:
        print(Fore.RED + f"No se encontraron socios con el nombre '{nombre_buscar}'." + Style.RESET_ALL)

# Función para eliminar un socio por número de socio
def eliminar_socio():
    num_socio_eliminar = input("Ingrese el número de socio del socio que desea eliminar: ")
    if num_socio_eliminar in socios:
        del socios[num_socio_eliminar]
        print(Fore.RED + f"Socio con número de socio '{num_socio_eliminar}' eliminado correctamente." + Style.RESET_ALL)
    else:
        print(Fore.RED + f"No se encontró socio con número de socio '{num_socio_eliminar}'." + Style.RESET_ALL)

# Función principal que maneja la lógica del programa
def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            agregar_socio()
        elif opcion == '2':
            listar_socios()
        elif opcion == '3':
            buscar_socio()
        elif opcion == '4':
            eliminar_socio()
        elif opcion == '5':
            print(Fore.MAGENTA + "¡Hasta luego!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor ingrese un número del 1 al 5." + Style.RESET_ALL)

# Iniciar el programa
if __name__ == "__main__":
    main()
