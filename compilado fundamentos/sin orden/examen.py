

# Definición de precios de pizzas
cuatroqueso_pequeña = 6000
cuatroqueso_mediana = 9000
cuatroqueso_familiar = 12000

hawaiana_pequeña = 6000
hawaiana_mediana = 9000
hawaiana_familiar = 12000

napolitana_pequeña = 5500
napolitana_mediana = 8500
napolitana_familiar = 11000

pepperoni_pequeña = 7000
pepperoni_mediana = 10000
pepperoni_familiar = 13000

# Lista para almacenar las ventas
ventas = []

#Aqui se guardara las listas creadas y se importara las listas
import json

#importamos la fecha y hora
from datetime import datetime 

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Registrar una venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar ventas por cliente")
    print("4. Guardar las ventas en un archivo")
    print("5. Cargar las ventas desde un archivo")
    print("6. Generar boleta")
    print("7. Anular boleta")
    print("8. Salir del menu")
    return input("Ingrese el número de la opción deseada: ")

# Función para registrar una venta
def registrar_venta():
    print("\nBienvenido, ¿qué sabor de pizza desea llevar?")
    print("1. Cuatroqueso")
    print("2. Hawaiana")
    print("3. Napolitana")
    print("4. Pepperoni")
    producto = int(input("Ingrese el número de la opción deseada: "))

    if producto == 1: #PIZZA DE cuatroqueso
        cliente = input("Nombre del cliente: ")
        print("¿Qué tamaño desea la pizza?")
        print("1. Familiar")
        print("2. Mediana")
        print("3. Pequeña")
        tamaño = int(input("Ingrese el número de la opción deseada: "))
        
        if tamaño == 1: #PIZZA cuatroqueso FAMILIAR
            precio_unitario = cuatroqueso_familiar
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)
                
        elif tamaño == 2: #PIZZA cuatroqueso MEDIANA
            precio_unitario = cuatroqueso_mediana
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)
                
        elif tamaño == 3: #PIZZA cuatroqueso PEQUEÑA
            precio_unitario = cuatroqueso_pequeña
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)

        # Agregar la venta a la lista de ventas
        ventas.append({
            'sabor': 'cuatroqueso',
            'tamaño': tamaño,
            'precio_unitario': precio_unitario,
            'descuento': descuento,
            'precio_final': preciofinal,
            'usuario': usuario,
            'cliente': cliente
            
        })

        print(f"El precio final con descuento es: {preciofinal}")

    elif producto == 2: #PIZZA hawaiana
        cliente = input("Nombre del cliente: ")
        print("¿Qué tamaño desea la pizza?")
        print("1. Familiar")
        print("2. Mediana")
        print("3. Pequeña")
        tamaño = int(input("Ingrese el número de la opción deseada: "))
        
        if tamaño == 1: #PIZZA hawaiana FAMILIAR
            precio_unitario = hawaiana_familiar
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)
                
        elif tamaño == 2: #PIZZA hawaiana MEDIANA
            precio_unitario = hawaiana_mediana
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)
                
        elif tamaño == 3: #PIZZA hawaiana PEQUEÑA
            precio_unitario = hawaiana_pequeña
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)

        # Agregar la venta a la lista de ventas
        ventas.append({
            'sabor': 'hawaiana',
            'tamaño': tamaño,
            'precio_unitario': precio_unitario,
            'descuento': descuento,
            'precio_final': preciofinal,
            'usuario': usuario,
            'cliente': cliente
        })

        print(f"El precio final con descuento es: {preciofinal}")

    elif producto == 3: #PIZZA napolitana
        cliente = input("Nombre del cliente: ")
        print("¿Qué tamaño desea la pizza?")
        print("1. Familiar")
        print("2. Mediana")
        print("3. Pequeña")
        tamaño = int(input("Ingrese el número de la opción deseada: "))
        
        if tamaño == 1: #PIZZA FAMILIAR napolitana
            precio_unitario = napolitana_familiar
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)
                
        elif tamaño == 2: #PIZZA MEDIANA napolitana
            precio_unitario = napolitana_mediana
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)
                
        elif tamaño == 3: #PIZZA PEQUEÑA napolitana
            precio_unitario = napolitana_pequeña
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)

        # Agregar la venta a la lista de ventas
        ventas.append({
            'sabor': 'napolitana',
            'tamaño': tamaño,
            'precio_unitario': precio_unitario,
            'descuento': descuento,
            'precio_final': preciofinal,
            'usuario': usuario,
            'cliente': cliente
        })

        print(f"El precio final con descuento es: {preciofinal}")

    elif producto == 4: #PIZZA pepperoni
        cliente = input("Nombre del cliente: ")
        print("¿Qué tamaño desea la pizza?")
        print("1. Familiar")
        print("2. Mediana")
        print("3. Pequeña")
        tamaño = int(input("Ingrese el número de la opción deseada: "))
        
        if tamaño == 1: #PIZZA FAMILIAR pepperoni
            precio_unitario = pepperoni_familiar
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)
                
        elif tamaño == 2: #PIZZA MEDIANA pepperoni
            precio_unitario = pepperoni_mediana
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)
                
        elif tamaño == 4: #PIZZA PEQUEÑA pepperoni
            precio_unitario = pepperoni_pequeña
            print("Selecciona qué tipo de usuario eres:")
            print("1. Estudiante vespertino")
            print("2. Estudiante Diurno")
            print("3. Administrativo")
            usuario = int(input("Ingrese el número de la opción deseada: "))
            if usuario == 1:
                descuento = 0.14  # 14% de descuento para estudiantes vespertinos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 2:
                descuento = 0.12  # 12% de descuento para estudiantes diurnos
                preciofinal = precio_unitario * (1 - descuento)
            elif usuario == 3:
                descuento = 0.10  # 10% de descuento para administrativos
                preciofinal = precio_unitario * (1 - descuento)

        # Agregar la venta a la lista de ventas
        ventas.append({
            'sabor': 'pepperoni',
            'tamaño': tamaño,
            'precio_unitario': precio_unitario,
            'descuento': descuento,
            'precio_final': preciofinal,
            'usuario': usuario,
            'cliente': cliente
        })

        print(f"El precio final con descuento es: {preciofinal}")

    else:
        print("Opción no válida")

# Función para mostrar todas las ventas registradas
def mostrar_todas_ventas():
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for idx, venta in enumerate(ventas, start=1):
            print("--------------------------")
            print(f"Venta {idx}:")
            print(f"Sabor: {venta['sabor']}")
            print(f"Tamaño: {venta['tamaño']}")
            print(f"Precio Unitario: {venta['precio_unitario']}")
            print(f"Descuento aplicado: {venta['descuento'] * 100}%")
            print(f"Precio Final: {venta['precio_final']}")
            print(f"Tipo de usuario: {venta['usuario']}")
            print(f"Nombre de cliente: {venta['cliente']} ")
            print("--------------------------")

# Función para buscar ventas por cliente
def buscar_ventas_por_cliente():
    cliente_buscar = input("Ingrese el nombre del cliente para buscar las ventas: ")
    ventas_encontradas = [] #lista para agregar temporalmente a los clientes buscados
    for venta in ventas:
        if venta['cliente'].lower() == cliente_buscar.lower(): #Aqui se busca el cliente en las ventas registradas
            ventas_encontradas.append(venta) #Se agrega el cliente de forma temporal en la lista "ventas_encontradas"
    
    if ventas_encontradas: #Cuando se encuentre el cliente:
        print(f"\nVentas encontradas para el cliente '{cliente_buscar}':")
        for venta in ventas_encontradas:
            print("\nVenta:")
            for key, value in venta.items():#Este es un bucle for que itera a través de cada elemento 
                print(f"{key}: {value}") #key representa la clave yvalue representa el valor asociado
    else:
        print(f"No se encontraron ventas para el cliente '{cliente_buscar}'.")

#Funcion para guardar la lista en los archivos
def guardar_ventas(nombre_archivo):
    if nombre_archivo == "":
        nombre_archivo = "archivo_personalizado.txt"

    with open(nombre_archivo, 'w') as file:
        json.dump(ventas, file, indent=4)
        print(f"Ventas guardadas correctamente en {nombre_archivo}")

# Función para mostrar todas las ventas registradas
def Generar_boleta():
    if not ventas:
        print("No hay ventas registradas.")
    else:
        print("")
        now = datetime.now()
        fecha_hora_actual = now.strftime("%d/%m/%Y %H:%M:%S")
        print("--------------------------")
        print(f"Fecha y Hora: {fecha_hora_actual}")
        print("\n--- Boleta ---")
        
        for idx, venta in enumerate(ventas, start=1):
            print(f"Venta {idx}:")
            print(f"Sabor: {venta['sabor']}")
            print(f"Tamaño: {venta['tamaño']}")
            print(f"Precio Unitario: {venta['precio_unitario']}")
            print(f"Descuento aplicado: {venta['descuento'] * 100}%")
            print(f"Precio Final: {venta['precio_final']}")
            print(f"Tipo de usuario: {venta['usuario']}")
            print(f"Nombre de cliente: {venta['cliente']} ")
            print("--------------------------")

def Anular_compra():
    if not ventas:
        print("No hay ventas registradas.")
    else:
        ventas.clear()
        print("La compra ha sido anulada")

def cargar_ventas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            ventas_cargadas = json.load(file)
            
            # Limpiamos la lista actual de ventas y cargamos las nuevas desde el archivo
            
            ventas.clear()
            ventas.extend(ventas_cargadas)
            print(f"Ventas cargadas correctamente desde {nombre_archivo}")
            
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}. No se cargaron ventas.")
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON en {nombre_archivo}. No se cargaron ventas.")

# Ciclo principal del programa

while True:
    
    opcion = mostrar_menu()

    if opcion == '1':
        registrar_venta()
    elif opcion == '2':
        mostrar_todas_ventas()
    elif opcion == '3':
        buscar_ventas_por_cliente()
    elif opcion == '4':
        nombre_archivo = input("Ingrese el nombre para el archivo de usuarios (dejar vacío para 'usuarios.json'): ").lower()
        guardar_ventas(nombre_archivo)
    elif opcion == '5':
        nombre_archivo = input("Ingrese el nombre del archivo de ventas a cargar: ").strip()
        cargar_ventas(nombre_archivo)
    elif opcion == '6':
        Generar_boleta()
    elif opcion == '7':
        Anular_compra()
    elif opcion == '8':
        print("Gracias por utilizar nuestro sistema de ventas.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
