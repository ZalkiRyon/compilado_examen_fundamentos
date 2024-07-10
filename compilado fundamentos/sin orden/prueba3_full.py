import random
import csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]


def generar_sueldos():
    sueldos = [random.randint(300000, 2500000) for _ in range(len(trabajadores))]
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
    reporte = []
    for i in range(len(trabajadores)):
        sueldo_base = sueldos[i]
        descuento_salud = int(sueldo_base * 0.07)
        descuento_afp = int(sueldo_base * 0.12)
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        reporte.append([trabajadores[i], sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
    return reporte

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
    import json
    with open('reporte_sueldos.json', mode='w') as file:
        json.dump(reporte, file, indent=4)

def main():
    sueldos = []
    while True:
        print("\nMenú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Reporte de sueldos")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sueldos = generar_sueldos()
            print("Sueldos asignados correctamente")
        elif opcion == "2":
            if not sueldos:
                print("Debe asignar sueldos primero")
            else:
                clasificacion = clasificar_sueldos(sueldos)
                for rango, lista in clasificacion.items():
                    print(f"{rango}: {len(lista)} trabajadores")
                    if lista:
                        print("Nombre empleado\t: Sueldo")
                    for sueldo in lista:
                        empleado_index = sueldos.index(sueldo)
                        empleado = trabajadores[empleado_index]
                        print(f"{empleado}: {sueldo}")
                    print(f"Sumatoria de sueldos en {rango}: ${sum(lista)}\n")
                acumulado = sum(sueldos)
                print(f"Sumatoria total de sueldos: ${acumulado}")                                    
                
        elif opcion == "3":
            if not sueldos:
                print("Debe asignar sueldos primero")
            else:
                reporte = generar_reporte(sueldos)
                guardar_reporte_csv(reporte)
                guardar_reporte_txt(reporte)
                guardar_reporte_json(reporte)
                print("Reportes generados correctamente")
        elif opcion == "4":
            print("Finalizando programa...")
            print("Desarrollado por Sebastian Valdivia")
            print("RUT 17.753.940-6")
            break
        else:
            print("Opción no válida")

main()