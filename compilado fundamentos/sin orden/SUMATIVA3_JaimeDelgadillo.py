import os
import time
import csv
import random
LISTA=[]

SND=[]
BUIN=[]
CTGO=[]

SECTORES=["san bernardo","calera de tango","buin"]
PEDIDO=random.randint(1,1000)
SUMA5K=0
SUMA5K10K=0
SUMA20K=0

def registro():
    
    a=True
    b=True
    c=True
    while a==True:
        cli=input("Ingrese nombre y apellido del cliente  :")
        dir=input("Ingrese Direccion de cliente :")
        while c==True:
            com=input("Ingrese Comuna san bernardo / calera de tango / buin :").lower()
            if com not in SECTORES:
                print ("Sector no existe , ingrese nuevamente .")
                time.sleep(2)
                continue
            else:
                break
        while b==True:
            try:
                sac=int(input("Que tipo de saco desea cargar 5 / 10 / 20 Kilos : "))
            except:
                print("Error,debe ser un valor numerico ")
                time.sleep(2)
                continue
            if sac==5:
                cant5=int(input("Ingrese cantidad de sacos de 5 kilos :"))
                SUMA5K=SUMA5K+cant5

            elif sac==10:
                cant10=int(input("Ingrese cantidad de sacos de 10 kilos :"))
                SUMA10K+=cant10              
            elif sac==20:
                
                cant20=int(input("Ingrese cantidad de sacos de 20 kilos :"))
                SUMA20K+=cant20  
            else:
                print("Esta cantidad no existe en los productos ")
                time.sleep(2)
                continue
        LISTA.append(PEDIDO,cli,dir,com,SUMA5K,SUMA10K,SUMA20K)
        if com=="san bernado":
            SND.append(PEDIDO,cli,dir,com,SUMA5K,SUMA10K,SUMA20K)
        elif com=="calera de tango":
            CTGO.append(PEDIDO,cli,dir,com,SUMA5K,SUMA10K,SUMA20K )    
        elif com=="buin":
            BUIN.append(PEDIDO,cli,dir,com,SUMA5K,SUMA10K,SUMA20K )    

def listar():
    print("Numero de pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10Kg","Saco 20Kg")
    for i in LISTA:
        print(i)
    tecla=input("Presione [Enter], para continuar ")

def imprimir():
    f=True
    print("Detalle de hoja de ruta")
    while f==True:
        ruta=input("Ingrese sector de ruta / san bernardo / calera de tango / buin ").lower()
        if ruta not in SECTORES:
            print("El sector no existe , intente nuevamente")
            time.sleep(2)
        elif ruta=="san bernardo":
            with open ("Ruta_San_Bernardo.txt","w") as rutasbn:
                rutasbn.write("Numero de pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10Kg","Saco 20Kg\n")
                for planillas in SND:
                    rutasbn.write(str(planillas)+ "\n")
            print("Archivo Ruta_San_Bernado.txt creado con exito ")
            teclas=input("Presione [Enter] para continuar")
            break

        elif ruta=="calera de tango":
            with open ("Ruta_Calera_Tgo.txt","w") as rutactg:
                rutactg.write("Numero de pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10Kg","Saco 20Kg\n")
                for planillas1 in CTGO:
                    rutactg.write(str(planillas1)+ "\n")
            print("Archivo Ruta_Calera_Tgo.txt creado con exito ")
            teclas=input("Presione [Enter] para continuar")
            break    

        elif ruta=="buin":
            with open ("Ruta_buin.txt","w") as rutabuin:
                rutabuin.write("Numero de pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10Kg","Saco 20Kg\n")
                for planillas2 in BUIN:
                    rutactg.write(str(planillas2)+ "\n")
            print("Archivo Ruta_Buin.txt creado con exito ")
            teclas=input("Presione [Enter] para continuar")
            break    

def csvfinal():
    with open ("Archivo_TOTAL_PEDIDOS.csv","w", newline="") as final:
        escritor=csv.writer(final)
        escritor.csv.writerrows(LISTA)


def menu():

    p=True
    while p==True:
        os.system("cls")
        print("MENU PRINCIPAL")
        print("[1]..Registrar pedido")
        print("[2]..Listar todos los pedidos")
        print("[3]..Imprimir ruta")
        print("[4]..Salir del programa")
        try:
            opc=int(input("Ingrese su opcion :"))
        except ValueError:
            print ("Error, debe ser un valor numerico")
            time.sleep(2)
            continue
        if opc==1:
            registro()
        elif opc==2:
            listar()
        elif opc==3:
            imprimir()
        elif opc==4:
            csvfinal()
            break
        else:
            print ("Error de eleccion, reintente")
            time.sleep(2)
            continue                


           
menu()

