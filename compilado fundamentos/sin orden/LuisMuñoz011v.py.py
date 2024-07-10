import csv



op1=0
pedido = []
comuna = ["San Bernardo", "Calera de Tango", "Buin"]

def menu ():
    print("-"*50)
    print("----------Bienvenido a nuestro menu----------")
    print("-"*50)
    print("1. Registrar pedido")
    print("2. Listar pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir")


while True:

    menu()

    while True:
        try:
            print("")
            op1 = int(input("Que opcion deceas realizar: "))
            print("")
            if op1 >=1 and op1 <= 4:
                break
            else:
                print("")
                print("Opcion invalida, intenta nuevamente")
                print("")
        except ValueError:
            print("")
            print("Opcion invalida, intenta nuevamente")
            print("")
            continue
    
    if op1 == 1:
        nombre_cliente = input("Ingrese el nombre y apellido del cliente: ")
        direccion_cliente = input("Ingrese la direcciòn del cliente: ")
        comuna_cliente = input("Ingrese la comuna del cliente: ")
        while comuna_cliente not in comuna:
            print("")
            comuna_cliente = input("Esta comuna no esta en nuetra BDD intenta nuevamente: ")
            print("")

        while True:
            try:
                print("")
                saco_5 = int(input("Ingrece cantidad de sacos de 5Kg: "))
                print("")
                if saco_5 >=0 and saco_5 <= 100:
                    break
                else:
                    print("")
                    print("Ingresa una cantidad valida")
                    print("")
            except ValueError:
                print("")
                print("Ingresa una cantidad valida")
                print("")

        while True:
            try:
                print("")
                saco_10 = int(input("Ingrece cantidad de sacos de 10Kg: "))
                print("")
                if saco_10 >=0 and saco_10 <= 100:
                    break
                else:
                    print("")
                    print("Ingresa una cantidad valida")
                    print("")
            except ValueError:
                print("")
                print("Ingresa una cantidad valida")
                print("")
        while True:
            try:
                print("")
                saco_20 = int(input("Ingrece cantidad de sacos de 20Kg: "))
                print("")
                if saco_20 >=0 and saco_20 <= 100:
                    break
                else:
                    print("")
                    print("Ingresa una cantidad valida")
                    print("")
            except ValueError:
                print("")
                print("Ingresa una cantidad valida")
                print("")

        pedido.append({
            "Nombre cliente" : nombre_cliente,
            "Direccion cliente" : direccion_cliente,
            "Comuna cliente" : comuna_cliente,
            "Sacos 5Kg" : saco_5,
            "Saco 10Kg" : saco_10,
            "Saco 20Kg" : saco_20          
        })  

    elif op1 == 2:
        print("")
        print("Lista de pedidos: ")
        print("")
        for pedidos in pedido:
            print(pedidos)

    elif op1 == 3:
        print("")
        comuna_seleccionada= input("Ingresa una comuna para imprimir, o bien oprima ENTER para imprimir todas las comunas: ")
        print("")

        if comuna_seleccionada == "":
            comunas_a_imprimir = comuna
            nombre_archivo ='Planilla_todos.txt'
        elif comuna_seleccionada in comuna:
            comunas_a_imprimir = []
            for pedido in pedidos:
                if pedido ['Comuna cliente'] == comuna_seleccionada:
                    comunas_a_imprimir.append(comuna)
            nombre_archivo =f'Planilla {comuna_seleccionada}.txt'
        else:
            print("")
            print("Comuna no valida")
            print("")
            break

        with open(nombre_archivo,'w') as archivo:
            for comuna in comunas_a_imprimir:
                archivo.write(f"Nombre cliente: {pedido['Nombre cliente']}\n")
                archivo.write(f"Direccion cliente: {pedido['Direccion cliente']}\n")
                archivo.write(f"Comuna cliente: {pedido['Comuna cliente']}\n")
                archivo.write(f"Saco 5Kg: {pedido['Saco 5Kg']}\n")
                archivo.write(f"Saco 10Kg: {pedido['Saco 10Kg']}\n")
                archivo.write(f"Saco 20Kg: {pedido['Saco 20Kg']}\n")

    elif op1 == 4:
        break

print("Gracias por usar nuestra aplicacion :)")

