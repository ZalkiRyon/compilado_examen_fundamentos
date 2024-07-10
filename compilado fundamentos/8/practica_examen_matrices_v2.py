import numpy as np

# Definición de variables globales
asientos = np.arange(1, 43).reshape(7, 6)  # Matriz de asientos
estado_asientos = asientos.astype(object)  # Inicialmente todos los asientos tienen su número, usando matriz de objetos
pasajeros = {}  # Diccionario para almacenar datos de los pasajeros

# Función para mostrar asientos disponibles
def mostrar_asientos():
    print("_________________________________________________________________")
    for i in range(asientos.shape[0]):
        if i == 5:
            print("|_________________________              ________________________|")
            print("|_________________________              ________________________|\n")
        for j in range(asientos.shape[1]):
            if j == 0:
                print("|", end="\t")
            if j == 3:
                print("\t", end="")
            asiento = estado_asientos[i, j]
            print(f"{'X' if asiento == 'X' else asiento}", end="\t")
            if j == asientos.shape[1] - 1:
                print("|", end="")
        print("\n", end="")
    print("_________________________________________________________________")

# Función para comprar asiento
def comprar_asiento():
    mostrar_asientos()
    nombre = input("Ingrese su nombre: ")
    rut = input("Ingrese su RUT: ")
    telefono = input("Ingrese su teléfono: ")
    banco = input("Ingrese su banco: ")

    while True:
        try:
            num_asiento = int(input("Seleccione el número de asiento que desea comprar: "))
            if num_asiento < 1 or num_asiento > 42:
                print("Número de asiento inválido. Intente nuevamente.")
                continue

            fila, columna = divmod(num_asiento - 1, 6)
            if estado_asientos[fila, columna] == 'X':
                print("Asiento ocupado. Seleccione otro asiento.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    if num_asiento >= 31:
        precio = 240000
    else:
        precio = 78900

    if banco.lower() == "bancoduoc":
        precio *= 0.85

    print(f"El valor del asiento seleccionado es: ${precio:.2f}")
    confirmar = input("¿Desea confirmar la compra? (si/no): ")
    if confirmar.lower() == 'si':
        estado_asientos[fila, columna] = 'X'
        pasajeros[num_asiento] = {
            'nombre': nombre,
            'rut': rut,
            'telefono': telefono,
            'banco': banco,
            'precio': precio
        }
        print("Compra realizada con éxito.")
    else:
        print("Compra cancelada.")

# Función para anular vuelo
def anular_vuelo():
    mostrar_asientos()
    try:
        num_asiento = int(input("Ingrese el número de asiento que desea anular: "))
        fila, columna = divmod(num_asiento - 1, 6)
        if estado_asientos[fila, columna] != 'X':
            print("El asiento ya está disponible.")
        else:
            estado_asientos[fila, columna] = num_asiento
            if num_asiento in pasajeros:
                del pasajeros[num_asiento]
            print("Anulación de vuelo exitosa.")
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")

# Función para modificar datos de pasajero
def modificar_datos():
    mostrar_asientos()
    try:
        num_asiento = int(input("Ingrese el número de asiento para modificar datos: "))
        rut = input("Ingrese el RUT para verificar los datos: ")
        if num_asiento in pasajeros and pasajeros[num_asiento]['rut'] == rut:
            print("1. Modificar nombre")
            print("2. Modificar teléfono")
            opcion = input("Seleccione la opción que desea modificar: ")
            if opcion == '1':
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                pasajeros[num_asiento]['nombre'] = nuevo_nombre
                print("Nombre modificado exitosamente.")
            elif opcion == '2':
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                pasajeros[num_asiento]['telefono'] = nuevo_telefono
                print("Teléfono modificado exitosamente.")
            else:
                print("Opción inválida.")
        else:
            print("Asiento o RUT no encontrado.")
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")

# Función principal del menú
def menu():
    while True:
        print("\n--- Menú de Vuelos-Duoc ---")
        print("1. Ver asientos disponibles")
        print("2. Comprar asiento")
        print("3. Anular vuelo")
        print("4. Modificar datos de pasajero")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_asientos()
        elif opcion == '2':
            comprar_asiento()
        elif opcion == '3':
            anular_vuelo()
        elif opcion == '4':
            modificar_datos()
        elif opcion == '5':
            print("Gracias por utilizar el sistema de Vuelos-Duoc.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú principal
menu()
