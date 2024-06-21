# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("\n*** Menú de Opciones ***")
    print("1. Agregar dato")
    print("2. Listar datos")
    print("3. Buscar dato")
    print("4. Eliminar dato")
    print("5. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    return opcion

# Función para agregar un nuevo dato al diccionario
def agregar_dato(datos):
    codigo = input("Ingrese el código del dato: ")
    descripcion = input("Ingrese la descripción del dato: ")
    # Podrías añadir más campos según tus necesidades
    datos[codigo] = {'descripcion': descripcion}
    print("¡Dato agregado correctamente!")

# Función para listar todos los datos en el diccionario
def listar_datos(datos):
    print("\nListado de Datos:")
    for codigo, info in datos.items():
        print(f"Código: {codigo}, Descripción: {info['descripcion']}")

# Función para buscar un dato por código o descripción
def buscar_dato(datos):
    criterio = input("Ingrese el código o descripción a buscar: ")
    encontrado = False
    for codigo, info in datos.items():
        if criterio in codigo or criterio in info['descripcion']:
            print(f"Datos encontrados para '{criterio}':")
            print(f"Código: {codigo}, Descripción: {info['descripcion']}")
            encontrado = True
    if not encontrado:
        print(f"No se encontraron datos para '{criterio}'.")

# Función para eliminar un dato por código o descripción
def eliminar_dato(datos):
    criterio = input("Ingrese el código o descripción del dato a eliminar: ")
    eliminado = False
    for codigo, info in list(datos.items()):  # Usamos list() para iterar sobre una copia
        if criterio in codigo or criterio in info['descripcion']:
            del datos[codigo]
            print(f"Dato con código '{codigo}' eliminado correctamente.")
            eliminado = True
    if not eliminado:
        print(f"No se encontraron datos para '{criterio}'.")

# Función principal que maneja la lógica del programa
def main():
    datos = {}  # Aquí almacenaremos nuestros datos (podrías usar una lista de diccionarios también)
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            agregar_dato(datos)
        elif opcion == '2':
            listar_datos(datos)
        elif opcion == '3':
            buscar_dato(datos)
        elif opcion == '4':
            eliminar_dato(datos)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 5.")

# Iniciar el programa
if __name__ == "__main__":
    main()
