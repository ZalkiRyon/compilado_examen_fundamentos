#Importacin de librerias
import os
import time
import csv
import random

#Funcion para limpiar pantalla
def Limpiar_pantalla():
    time.sleep(1)
    os.system("cls")

#Menu de opciones
def menu():
    while True:
        print("Bienvenido a CatPremium")
        try:
            opc=int(input("1.Registar pedido\n2.Listar todos los pedidos\n3.Imprimir hoja de ruta\n4.Salir del programa\nElije opcion: "))
        except ValueError:
            print("Error elije un numero del 1 al 4")
        if opc == 1:
            Registrar_pedido()
            Limpiar_pantalla()
        elif opc == 2:
            Lista_pedidos()
            Limpiar_pantalla()
        elif opc == 3:
            Imprimir_hoja()
            Limpiar_pantalla()
        elif opc == 4:
            print("Salio del programa")
            break

#Opcion 1 del Menu
def NumeroRandom():
    NumAlazar=0
    NumAlazar=random.randint(1,1000)
    NumAlazar += 1
    print(NumAlazar)

def Registrar_pedido():
    nombre=input("Escribre tu nombre y apellido: ")
    dirreccion=input("Escriba su dirreccion: ")
    comuna=input("Escriba su comuna: ")
    while True:
        #contador de sacos
        saco5kg=0
        saco10kg=0
        saco20kg=0
        #opciones de sacos de kilos
        try:
            opc2=int(input("1.Saco de 5Kg\n2.Saco de 10Kg\n3.Saco de 20Kg\n4.Volver al menu\nElija su opcion: "))
        except ValueError:
            print("Error elije un numero del 1 al 3")
        if opc2 == 1:
            saco5kg = int(input("Cuantos quieres: "))
            Limpiar_pantalla()
        elif opc2 == 2:
            saco10kg = int(input("Cuantos quieres: "))
            Limpiar_pantalla()
        elif opc2 == 3:
            saco20kg = int(input("Cuantos quieres: "))
            Limpiar_pantalla()
        elif opc2 == 4:
            print("Volviendo al menu")
            break
        #diccionario para guardar datos
    registro={
        "Nro.Ped" : NumeroRandom(),
        "Nombre" : nombre,
        "Direccion" : dirreccion,
        "Comuna" : comuna,
        "Saco 5kg" : saco5kg,
        "Saco 10kg" : saco10kg,
        "Saco 20kg" : saco20kg
        }
    #Creacion de archivo csv sale mal

    with open("Registro_pedido.csv","w",newline="")as registro_csv:
        escritor_csv=csv.writer(registro_csv)
        escritor_csv.writerows([
            "Nro.Ped","Cliente","Direccion","Sector","Saco 5kg","Saco 10kg","Saco 20kg"
            ])
    #Guardar las variables al archivo
    with open("Registro_pedido.csv","a",newline="")as registro_csv:
        escritor_csv=csv.writer(registro_csv)
        escritor_csv.writerow(NumeroRandom(),nombre,dirreccion,comuna,saco5kg,saco10kg,saco20kg)
    #leer el archivo csv
    with open("Registro_pedido.csv","r",newline="")as registro_csv:
        lector_csv=csv.reader(registro_csv)
        for i in registro_csv:
            print(i)

#Mostrar lista de pedidos de archivo csv

def Lista_pedidos():
    with open("Registro_pedido.csv","r",newline="")as registro_csv:
        lector_csv=csv.reader(registro_csv)
        for i in registro_csv:
            print(lector_csv)

#Mostrar hoja con archivo txt            

def Imprimir_hoja():
    sector=["San Bernardo","Calera de Tango","Buin"]
    opc3= input("Escribe el sector San Bernardo,Calera de Tango,Buin\n")
    if opc3 == len(sector):
        with open("Registro_pedido.txt","r+",newline="")as registro_txt:
            print(registro_txt)
menu()