import csv
import random
from os import system
opciones=0
empresa="CatPremiun"
pedido={}

def menu():
    system('cls')
    print("--------------------------------")
    print("Bienvenido " + empresa)
    print("1.Regitrar pedido")
    print("2.Listar todo los pedido")
    print("3.Imprimir hoja de ruta")
    print("4.Salir del programa")
    print("--------------------------------")

def registro_de_pedido():
    with open('registro pedido.csv', "a+") as archivo_csv:
        system('cls')
        escrito_csv=csv.writer(archivo_csv)
        gen_pedido=random.randint(1,1000)
        print(f"su numero de pedido es {gen_pedido}")
        nombre_cliente=str.upper(input("Ingrese el nombre del cliente: "))
        apellido_cliente=str.upper(input("Ingrese su apellido del cliente: "))
        direccion_cliente=str.upper(input("Ingrese su direccion cliente: "))
        comuna_cliente=str.upper(input("Ingrese la comuna del cliente: "))
        system('cls')
        print("debera ingresa cuanto sacos se lleva el cliente")
        try:
            saco_5kg=int(input("Ingrese cuanto saco de 5kg se lleva el cliente: "))
            saco_10kg=int(input("Ingrese cuanto saco de 10kg se lleva el cliente: "))
            saco_20kg=int(input("Ingrese cuanto saco de 20kg se lleva el cliente: "))

        except(ValueError,SyntaxError,TypeError):
            print("Ingreso de dato errroneo")
        escrito_csv.writerow([gen_pedido,nombre_cliente + " " +apellido_cliente,direccion_cliente,comuna_cliente,saco_5kg,saco_10kg,saco_20kg])


def listar_pedidos():
    pedido={}
    with open('registro pedido.csv', "r+") as archivo_csv:
        lector_csv=csv.DictReader(archivo_csv)
        print("|Nro.ped| |Cliente| |Direccion| |Comuna| |Saco 5kg| |Saco 10kg| |Saco 20kg|")
        for pedido in lector_csv:
            numero_pedido=pedido['Nro.ped']
            cliente=pedido['Cliente']
            direccion=pedido['Direccion']
            comuna=pedido['Comuna']
            saco_5kg=pedido['Saco 5kg']
            saco_10kg=pedido['Saco 10kg']
            saco_20kg=pedido['Saco 10kg']
            print(numero_pedido,"\t ",cliente,"\t ",direccion,"\t ",comuna,"\t ",saco_5kg,"\t ",saco_10kg,"\t ",saco_20kg)

def hoja_ruta():
    with open('registro pedido.csv', "r+") as archivo_csv:
        lector_csv=csv.DictReader(archivo_csv)
        system('cls')
        print("Elija la ruta que desea tomar")
        print("1.San Bernardo")
        print("2.Calera de tango")
        print("3.Buin")
        print("4.salir")
        try: 
            sector=int(input(""))
        except (ValueError,SyntaxError,TypeError):
            print("dato erroneo ingresado")
        if sector == 1:
            with open('hoja ruta SAN BERNARDO.txt','a')as archivo:
                        system('cls')
                        archivo.write("Nro.ped  Cliente  Direccion  Comuna  Saco 5kg  Saco 10kg  Saco 20kg")
                        archivo.writelines("    ")
                        for pedido in lector_csv:
                            comuna=pedido['Comuna']
                            numero_pedido=pedido['Nro.ped']
                            cliente=pedido['Cliente']
                            direccion=pedido['Direccion']
                            saco_5kg=pedido['Saco 5kg']
                            saco_10kg=pedido['Saco 10kg']
                            saco_20kg=pedido['Saco 10kg']
                            if comuna == "SAN BERNARDO":
                                with open('hoja ruta.txt','a+')as archivo:
                                        archivo.write(numero_pedido)
                                        archivo.write(" ")
                                        archivo.write(cliente)
                                        archivo.write(" ")
                                        archivo.write(direccion)
                                        archivo.write(" ")
                                        archivo.write(comuna)
                                        archivo.write(" ")
                                        archivo.write(saco_5kg)
                                        archivo.write(" ")
                                        archivo.write(saco_10kg)
                                        archivo.write(" ")
                                        archivo.write(saco_20kg)
                                        print("se ha registrado una direccion")
        elif sector == 2:
            with open('hoja ruta.txt','a')as archivo:
                        system('cls')
                        archivo.write("Nro.ped  Cliente  Direccion  Comuna  Saco 5kg  Saco 10kg  Saco 20kg")
                        archivo.writelines("    ")
                        for pedido in lector_csv:
                            comuna=pedido['Comuna']
                            numero_pedido=pedido['Nro.ped']
                            cliente=pedido['Cliente']
                            direccion=pedido['Direccion']
                            saco_5kg=pedido['Saco 5kg']
                            saco_10kg=pedido['Saco 10kg']
                            saco_20kg=pedido['Saco 10kg']
                            if comuna == "CALERA DE TANGO":
                                with open('hoja ruta.txt','a+')as archivo:
                                        archivo.write(numero_pedido)
                                        archivo.write(" ")
                                        archivo.write(cliente)
                                        archivo.write(" ")
                                        archivo.write(direccion)
                                        archivo.write(" ")
                                        archivo.write(comuna)
                                        archivo.write(" ")
                                        archivo.write(saco_5kg)
                                        archivo.write(" ")
                                        archivo.write(saco_10kg)
                                        archivo.write(" ")
                                        archivo.write(saco_20kg)
                                        print("se ha registrado una direccion")
        elif sector == 3:
            with open('hoja ruta.txt','a')as archivo:
                    system('cls')
                    archivo.write("Nro.ped  Cliente  Direccion  Comuna  Saco 5kg  Saco 10kg  Saco 20kg")
                    archivo.writelines("    ")
                    for pedido in lector_csv:
                        comuna=pedido['Comuna']
                        numero_pedido=pedido['Nro.ped']
                        cliente=pedido['Cliente']
                        direccion=pedido['Direccion']
                        saco_5kg=pedido['Saco 5kg']
                        saco_10kg=pedido['Saco 10kg']
                        saco_20kg=pedido['Saco 10kg']
                        if comuna == "CALERA DE TANGO":
                            with open('hoja ruta.txt','a+')as archivo:
                                    archivo.write(numero_pedido)
                                    archivo.write(" ")
                                    archivo.write(cliente)
                                    archivo.write(" ")
                                    archivo.write(direccion)
                                    archivo.write(" ")
                                    archivo.write(comuna)
                                    archivo.write(" ")
                                    archivo.write(saco_5kg)
                                    archivo.write(" ")
                                    archivo.write(saco_10kg)
                                    archivo.write(" ")
                                    archivo.write(saco_20kg)
                                    print("se ha registrado una direccion")

                

        

while opciones != 4:
    menu()
    try:
        opciones=int(input("Ingrese la opcion correspondiente: "))
    except(ValueError,SystemError,TypeError):
        print("dato erroneo ingresado ")

    if opciones == 1:
        registro_de_pedido()
    elif opciones == 2:
        listar_pedidos()
    elif opciones == 3:
        hoja_ruta()
    else:
        print("guardando en el registro de pedido")
        print("Saliendo del programa")