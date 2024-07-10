import csv
import random
import time
import os




def limpiar_detener_pantalla():
    os.system("cls")
    time.sleep(4)
    os.system("cls")

def registrar_pedido():
    
    with open('archivo.csv', 'a', newline='') as lista:
        nmrped=random.randint(1,1000)
        cliente=input("escriba su nombre: ")
        direccion=input("escriba su direccion: ")
        sector=input("escriba el sector donde vive: ")
        saco5kg=int(input("¿cuantos sacos de 5 kg quiere?: "))
        saco10kg=int(input("¿cuantos sacos de 10 kg quiere?: "))
        saco20kg=int(input("¿cuantos sacos de 20 kg quiere?: "))
        lista=['Nmr.Ped','Cliente','Direccion','Sector','Saco 5 kg','Saco 10 kg','Saco 20 kg'
        ]
        archivo=csv.DictWriter(lista, fieldnames=lista)

        archivo.writeheader([
            'Nmr.Ped',
            'Cliente',
            'Direccion',
            'Sector',
            'Saco 5 kg',
            'Saco 10 kg',
            'Saco 20 kg'
        ])

        lista.append(nmrped)
        lista.append(cliente)
        lista.append(direccion)
        lista.append(sector)
        lista.append(saco5kg)
        lista.append(saco10kg)
        lista.append(saco20kg)

def listar_Pedido():
    print(registrar_pedido)

def menu():
    limpiar_detener_pantalla()
    print("****CatPremiun****")
    print("1.Registrar pedido")
    print("2.listar todos los pedidos")
    print("3.Imprimir hoja de ruta")
    print("4.Salir")


listar_Pedido()