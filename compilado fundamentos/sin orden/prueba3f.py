import csv
import os
import time

def Limpiar():
    time.sleep(1)
    os.system("cls")
    
reg_trab=[]

def descuento_salud(sueldo_bruto):
    return sueldo_bruto * 0.07
    
def descuento_afp(sueldo_bruto):
    return sueldo_bruto * 0.12
    
def liquido_pagar(sueldo_bruto, desc_salud, desc_afp):
    return sueldo_bruto - desc_salud - desc_afp 
    
def registrar_trabajador(reg_trab):
    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador (CEO, Desarrollador, Analista de datos): ")
    sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
    
    if nombre and apellido and cargo and sueldo_bruto:
        desc_salud = descuento_salud(sueldo_bruto)
        desc_afp = descuento_afp(sueldo_bruto)
        liquido_total = liquido_pagar(sueldo_bruto, desc_salud, desc_afp)
    
    with open("Registro_trabajador.csv","w",newline="") as Reg_csv:
        escritor_csv = csv.writer(Reg_csv delimiter=";")
        escritor_csv.writerow(['Trabajador', 'Cargo', 'Sueldo Bruto','Desc.Salud','Desc.AFP','Liquido a pagar'])
        escritor_csv.writerows([])

