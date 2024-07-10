import csv

def menu_principal():
    while True:
        print("\nBienvenido al Sistema de Gestión de Inventario")
        print("Seleccione una opción:")
        print("1. Agregar producto al inventario")
        print("2. Leer el inventario")
        print("3. Clasificar productos y generar archivo de texto")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción escogida: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            leer_inventario()
        elif opcion == "3":
            clasificar_productos()
        elif opcion == "4":
            print("¡CYA!") #see u later!!
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def agregar_producto():
    print("Agregar producto al inventario")
    id_producto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto (Electrónica, Textil o Calzado): ")
    precio = float(input("Ingrese el precio del producto: "))

    with open("inventario.csv", "a", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([id_producto, nombre, categoria, precio])

    print("Producto agregado al inventario.")

def leer_inventario():
    print("Leyendo el inventario...")
    with open("inventario.csv", "r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Categoría: {fila[2]}, Precio: {fila[3]}")

def clasificar_productos():
    print("Clasificando productos y generando archivo de texto...")
    productos_electronicos = []
    productos_textiles = []
    productos_calzado = []

    with open("inventario.csv", "r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  
        for fila in lector_csv:
            id_producto, nombre, categoria, precio = fila
            if categoria == "Electrónica":
                productos_electronicos.append(f"ID: {id_producto}, Nombre: {nombre}, Precio: {precio}")
            elif categoria == "Textil":
                productos_textiles.append(f"ID: {id_producto}, Nombre: {nombre}, Precio: {precio}")
            elif categoria == "Calzado":
                productos_calzado.append(f"ID: {id_producto}, Nombre: {nombre}, Precio: {precio}")

    with open("clasificacion_productos.txt", "w") as archivo_texto:
        archivo_texto.write("Productos Electrónicos:")
        for producto in productos_electronicos:
            archivo_texto.write(f"- {producto}")
        archivo_texto.write("\nProductos Textiles:")
        for producto in productos_textiles:
            archivo_texto.write(f"- {producto}")
        archivo_texto.write("\nProductos de Calzado:")
        for producto in productos_calzado:
            archivo_texto.write(f"- {producto}")

    print("El archivo de clasificación de productosha sido generado con exito.")
menu_principal()
