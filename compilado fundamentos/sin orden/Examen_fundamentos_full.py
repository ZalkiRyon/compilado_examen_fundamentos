import random
import csv
import statistics
import json
import math
import os

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def limpiar_pantalla():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        #se supone sirve para mac y linux 
        os.system('clear')

def numeros(a):
    return "{:,}".format(a).replace(",", ".")

def generar_sueldos():
    sueldos = [random.randint(300000, 2500000) for i in range(len(trabajadores))]
    return sueldos

def clasificar_sueldos(sueldos):
    clasificacion = {
        "Menores a $800.000": [],
        "Entre $800.000 y $1.500.000": [],
        "Entre $1.500.000 y $2.000.000": [],
        "Mayores a $2.000.000": []
    }
    for i in sueldos:
        if i < 800000:
            clasificacion["Menores a $800.000"].append(i)
        elif 800000 <= i <= 1500000:
            clasificacion["Entre $800.000 y $1.500.000"].append(i)
        elif 1500000 < i <= 2000000:
            clasificacion["Entre $1.500.000 y $2.000.000"].append(i)
        else:
            clasificacion["Mayores a $2.000.000"].append(i)
    return clasificacion

def generar_reporte(sueldos):
    global reporte
    reporte = []
    for i in range(len(trabajadores)):
        sueldo_base = sueldos[i]
        descuento_salud = int(sueldo_base * 0.07)
        descuento_afp = int(sueldo_base * 0.12)
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        reporte.append([trabajadores[i], numeros(sueldo_base), numeros(descuento_salud), numeros(descuento_afp), numeros(sueldo_liquido)])
    return reporte

def reporte_sueldos():
    print("Nombre empleado\t\tSueldo Base\tDescuento Salud\t    Descuento AFP     Sueldo Líquido")
    for i in reporte:
        #para la derecha de a uno, se logro centrar el texto
        print(f"{i[0]:<24}${i[1]:>10}     ${i[2]:>10}         ${i[3]:>10}       ${i[4]:>10}")
        #para abajo, de a uno
        #print(f"Trabajador: {i[0]}")
        #print(f"Sueldo Bruto: {i[1]}")
        #print(f"Descuento AFP: {i[2]}")
        #print(f"Descuento Salud: {i[3]}")
        #print(f"Sueldo Líquido: {i[4]}")
        #print("-" * 50)

def guardar_reporte_csv(reporte):
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(reporte)

def guardar_reporte_txt(reporte):
    with open('reporte_sueldos.txt', mode='w') as file:
        file.write("Nombre empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Líquido\n")
        for linea in reporte:
            file.write("\t".join(map(str, linea)) + "\n")

def guardar_reporte_json(reporte):
    with open('reporte_sueldos.json', mode='w') as file:
        json.dump(reporte, file, indent=4)

#crear función para calcular estadísticas que contenga, sueldo mayor, sueldo menor, promedio y media geométrica
def calcular_estadisticas(sueldos):
    estadisticas = {
        'Promedio\t': statistics.mean(sueldos),
        #'Mediana': statistics.median(sueldos),
        'Sueldo Máximo\t': max(sueldos),
        'Sueldo Mínimo\t': min(sueldos),
        'Media Geométrica': calcular_media_geometrica(sueldos)
    }
    #promedio por rangos
    """
    clasificacion = clasificar_sueldos(sueldos)
    for rango, lista in clasificacion.items():
        if lista:
            estadisticas[f'Promedio {rango}'] = statistics.mean(lista)
            """
    return estadisticas

def calcular_media_geometrica(sueldos):
    producto_sueldos = math.prod(sueldos)    
    return math.pow(producto_sueldos, 1/len(sueldos))
    #chino mandarín


def main():
    sueldos = []
    while True:
        limpiar_pantalla()        
        print("Menú de opciones: ".center(30, "="))
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Reporte de sueldos")
        print("4. Estadísticas de sueldos")
        print("5. Salir del programa")
        opcion = input("\nSeleccione una opción: -> ")

        if opcion == "1":
            limpiar_pantalla()
            if not sueldos:
                sueldos = generar_sueldos()
                print("Sueldos generados correctamente")
                input("\nPresione Enter para continuar...")
            else:
                limpiar_pantalla()
                print("Los sueldos ya fueron generados")
                while True:
                    reemplazar = input("¿Desea reemplazar los sueldos? (s/n): ").lower().strip()
                    if reemplazar == "s":
                        sueldos = generar_sueldos()
                        limpiar_pantalla()
                        print("Sueldos reemplazados correctamente")
                        input("\nPresione Enter para continuar...")
                        break
                    elif reemplazar == "n":
                        break
                    else:
                        limpiar_pantalla()
                        print("Opción no válida")
                        input("\nPresione Enter para continuar...")
                        
        elif opcion == "2":
            if not sueldos:
                limpiar_pantalla()
                print("Debe asignar sueldos primero")
                input("\nPresione Enter para continuar...")                
            else:
                clasificacion = clasificar_sueldos(sueldos)
                limpiar_pantalla()
                for rango, lista in clasificacion.items():
                    trabajadores_text = 'trabajador' if len(lista) == 1 else 'trabajadores'
                    print(f"{rango:29s} {len(lista):3d} {trabajadores_text}")
                    if lista:
                        print("Nombre empleado\t\t\tSueldo")
                    for sueldo in lista:
                        empleado_index = sueldos.index(sueldo)
                        empleado = trabajadores[empleado_index]
                        print(f"{empleado:30s}\t${numeros(sueldo):>10s}")
                    print("=" * 46)
                    print(f"Sumatoria de sueldos\t\t${numeros(sum(lista)):>10s}\n")
                acumulado = sum(sueldos)
                print(f"Sumatoria total de sueldos:\t${numeros(acumulado):>10s}")
                input("\nPresione Enter para continuar...")
                
        elif opcion == "3":
            if not sueldos:
                limpiar_pantalla()
                print("Debe asignar sueldos primero")
                input("\nPresione Enter para continuar...")   
            else:
                reporte = generar_reporte(sueldos)
                guardar_reporte_csv(reporte)
                guardar_reporte_txt(reporte)
                guardar_reporte_json(reporte)
                limpiar_pantalla()
                #modificar acorde al tipo de archivo que se quiera generar
                print("Reporte generados correctamente a archivos CSV, TXT y JSON")
                reporte_sueldos()
                input("\nPresione Enter para continuar...")                

        elif opcion == "4":
            if not sueldos:
                limpiar_pantalla()
                print("Debe asignar sueldos primero")
                input("\nPresione Enter para continuar...")   
            else:
                estadisticas = calcular_estadisticas(sueldos)
                limpiar_pantalla()
                print("Estadísticas de sueldos:")
                for parametro, valor in estadisticas.items():
                    print(f"{parametro}:\t${numeros(valor)}")
                input("\nPresione Enter para continuar...")
                
        elif opcion == "5":
            limpiar_pantalla()
            print("Finalizando programa...")
            print("Desarrollado por Sebastian Valdivia")
            print("RUT 17.753.940-6")
            break
        else:
            print("Opción no válida")

main()
