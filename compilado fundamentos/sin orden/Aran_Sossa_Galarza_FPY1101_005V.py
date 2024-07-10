import datetime
import json

precio_pizzas = {
    "Margarita": {
        "Pequeña": 5500,
        "Mediana": 8500,
        "Familiar": 11000
    },
    "Mexicana": {
        "Pequeña": 7000,
        "Mediana": 10000,
        "Familiar": 13000
    },
    "Barbacoa": {
        "Pequeña": 6500,
        "Mediana": 9500,
        "Familiar": 12500
    },
    "Vegetariana": {
        "Pequeña": 5000,
        "Mediana": 8000,
        "Familiar": 10500
    }
}

descuentos = {
    "Estudiante Diurno": 0.15,
    "Estudiante Vespertino": 0.18,
    "Administrativo": 0.11
}

ventas = []

def registrar_venta():
    print("Registrar de venta:")
    nombre_cliente = input("Ingrese nombre del cliente: ")
    tipo_usuario = input("Tipo de usuario (Estudiante diurno, Estudiante vespertino, Administrativo): ")
    
    print("\nTipos de pizza disponibles:")
    for pizza in precio_pizzas:
        print(f"- {pizza}")
        
    tipo_pizza = input("\nIngrese tipo de pizza: ")
    
    while tipo_pizza not in precio_pizzas:
        print("Tipo de pizza no válido. Intente de nuevo.")
        tipo_pizza = input("Ingrese tipo de pizza: ")
    
    print("\nTamaños disponibles:")
    for tamaño in precio_pizzas[tipo_pizza]:
        print(f"- {tamaño}")
        
    tamaño_pizza = input("\nIngrese tamaño de la pizza: ")
    

    while tamaño_pizza not in precio_pizzas[tipo_pizza]:
        print("Tamaño de pizza no válido. Intente de nuevo.")
        tamaño_pizza = input("Ingrese tamaño de la pizza: ")
    
    cantidad = int(input("Ingrese cantidad de pizzas: "))
    
    precio_unitario = precio_pizzas[tipo_pizza][tamaño_pizza]
    precio_total = precio_unitario * cantidad
    
    if tipo_usuario in descuentos:
        descuento = descuentos[tipo_usuario]
        precio_total -= precio_total * descuento
    
    venta = {
        "Cliente": nombre_cliente,
        "Tipo de usuario": tipo_usuario,
        "Tipo de pizza": tipo_pizza,
        "Tamaño": tamaño_pizza,
        "Cantidad": cantidad,
        "Precio total": precio_total,
        "Fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    ventas.append(venta)
    print("\nVenta registrada exitosamente.\n")

def mostrar_ventas():
    print("Listado de ventas realizadas:")
    for venta in ventas:
        print("\n------------------------------")
        for clave, valor in venta.items():
            print(f"{clave}: {valor}")
    print("\n----------------------------------\n")

def buscar_por_cliente():
    cliente_buscar = input("Ingrese nombre del cliente para buscar ventas: ")
    print(f"Ventas encontradas para '{cliente_buscar}':")
    encontradas = False
    for venta in ventas:
        if venta["Cliente"].lower() == cliente_buscar.lower():
            encontradas = True
            print("Boleta Interna")
            print("\n-------------------------")
            for clave, valor in venta.items():
                print(f"{clave}: {valor}")
    if not encontradas:
        print(f"No se encontraron ventas para el cliente '{cliente_buscar}'.")
    print("\n-------------------------\n")

def guardar_ventas():
    with open('ventas.json', 'w') as archivo:
        json.dump(ventas, archivo)
    print("Ventas guardadas en el archivo 'ventas.json'.\n")

def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as archivo:
            ventas = json.load(archivo)
        print("Ventas cargadas desde el archivo 'ventas.json'.\n")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'. No hay ventas cargadas.\n")

def generar_boleta():
    if not ventas:
        print("No hay ventas registradas para generar una boleta.\n")
        return
    
    print("Generando boleta...\n")
    
    ultima_venta = ventas[-1]
    print("  ..:::Pizzas DUOC:::..")
    print("    - Boleta Cliente - ")
    print("-------------------------")
    for clave, valor in ultima_venta.items():
        print(f"{clave}: {valor}")
    print("-------------------------")
    print("¡Gracias por su compra!")

def anular_venta():
    if not ventas:
        print("No hay ventas registradas para anular.\n")
        return
    
    cliente_anular = input("Ingrese nombre del cliente para anular venta: ")
    encontrado = False
    for venta in ventas:
        if venta["Cliente"].lower() == cliente_anular.lower():
            ventas.remove(venta)
            encontrado = True
            print(f"Venta para '{cliente_anular}' anulada correctamente.\n")
            break
    if not encontrado:
        print(f"No se encontró ninguna venta para el cliente '{cliente_anular}'.\n")

def mostrar_menu():
    print("\nBienvenido al sistema de ventas de pizzas en DUOC UC")
    while True:
        print("\nMenú:\n 1. Registrar una venta\n 2. Mostrar todas las ventas\n 3. Buscar ventas por cliente\n 4. Guardar las ventas en un archivo\n 5. Cargar las ventas desde un archivo\n 6. Generar Boleta\n 7. Anular venta\n 8. Salir del programa")
        
        opc = input("Seleccione una opción: ")
        
        if opc == "1":
            registrar_venta()
        elif opc == "2":
            mostrar_ventas()
        elif opc == "3":
            buscar_por_cliente()
        elif opc == "4":
            guardar_ventas()
        elif opc == "5":
            cargar_ventas()
        elif opc == "6":
            generar_boleta()
        elif opc == "7":
            anular_venta()
        elif opc == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo -_-.")


if __name__ == "__main__":
    mostrar_menu()