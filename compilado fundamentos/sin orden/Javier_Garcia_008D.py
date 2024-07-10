import csv
import os
import time
import random

os.system('cls')
pedidos = []

def numeroPedido():
    return random.randint(1, 1000)

# Registrar al cliente 
def registrarPedido():
    nombre = input("Ingresar el nombre del cliente: ")
    apellido = input("Ingresar el apellido del cliente: ")
    direccion = input("Ingresar la direccion del cliente: ")
    sector = input("Ingresar el sector o comuna donde vive: ")
    sacos_5 = int(input("Ingresar la cantidad de sacos de 5kg: "))
    sacos_10 = int(input("Ingresar la cantidad de sacos de 10 kg: "))
    sacos_20 = int(input("Ingresar la cantidad de sacos de 20kg que desea llevar: "))
    
    pedido_num = numeroPedido()
    pedido = {
        'numeroPedido': pedido_num,
        'nombre': nombre,
        'apellido': apellido,
        'direccion': direccion,
        'sector': sector,
        'sacos de 5kg': sacos_5,
        'sacos de 10 kg': sacos_10,
        'sacos de 20 kg': sacos_20
    }
    
    pedidos.append(pedido)
    guardarPedidoCsv(pedido)
    print(f"Pedido {pedido_num} registrado exitosamente")

#Guardado pedido
def guardarPedidoCsv(pedido):
    file_exists = os.path.isfile('pedidos.csv')
    with open('pedidos.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=pedido.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(pedido)
     
def listarPedido():
    if not pedidos:
        print("No hay pedidos registrados.")
    else:
        for pedido in pedidos:
            print(pedido)

#Hoja ruta              
def imprimirHojaRuta():
    if not pedidos:
        print("No hay pedidos para imprimir.")
    else:
        with open('imprimirHojaRuta.txt', 'w') as file:
            for pedido in pedidos:
                file.write(str(pedido) + "\n")
        print("Hoja de ruta impresa en imprimirHojaRuta.txt")

def menu():
    # Menú
    while True:
        print("Menu")
        print("1 - Registrar pedido.")
        print("2 - Listar todos los pedidos.")
        print("3 - Imprimir hoja de ruta.")
        print("4 - Salir del programa")
        
        # Opciones
        opcion = int(input("Ingrese su opcion: "))
        
        if opcion == 1:
            print("****Registrar pedido****")
            registrarPedido()
        elif opcion == 2:
            print("****Listar pedidos****")
            listarPedido()
        elif opcion == 3:
            print("****Hoja de ruta****")
            imprimirHojaRuta()
        elif opcion == 4:
            print("Saliendo del programa....")
            break
        else:
            print("Ingrese una opcion valida por favor intente de nuevo....")

menu()
