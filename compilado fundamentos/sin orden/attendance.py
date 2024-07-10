"""
Crear un programa que permita contabilizar la asistencia a clases.
Se debe guardar la asistencia en un archivo csv con fecha incluida automaticament
Tiene que existir un menu principal que pregunta si se quiere guardar asistencia o buscar
Si se elige guardar, el programa pregunta constantemente el nombre del estudiante y si esta o no presente. (la idea es registrar a toda una clase)
Esto se debe  realizar hasta que el usuario decida no seguir guardando asistencia.

Si elige buscar, el programa debe pedir el nombre del estudiante y la fecha.
Debe devolver si el alumno estuvo o no presente ese dia.

Se deben generar dos funciones. Una para guardar y otra para leer.

from datetime import date
date.today().strftime("%d-%m-%Y)
"""

import os
from datetime import datetime
import csv


def guardar_asistencia():
    class_attendance = []
    date = datetime.today().strftime("%d-%m-%Y")

    while True:
        attendance = False
        name = input(
            'Ingresa el nombre del estudiante a guardar, ingresa "salir" para terminar\n> '
        )
        if name == "salir":
            break

        is_present = input("Esta presente? (s/n): ").lower()

        if is_present == "s":
            attendance = True

        class_attendance.append({"date": date, "name": name, "attendance": attendance})
        os.system("cls||clear")

    with open(f"{date}_asistencia.csv", "w", newline="") as csv_file:
        fieldnames = ["date", "name", "attendance"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        csv_writer.writerows(class_attendance)

    os.system("cls||clear")
    print("\nClase registrada con exito\n")


def buscar_asistencia():
    date_to_search = input("Ingresa la fecha de la clase a buscar (DD-MM-YYYY)\n> ")

    attendance_file = f"{date_to_search}_asistencia.csv"

    if not os.path.exists(attendance_file):
        os.system("cls||clear")
        print("\nNo hay asistencia registrada para ese dia\n")
    else:
        student_name = input("Ingresa el nombre del estudiante\n> ")
        with open(attendance_file, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            found = [
                student for student in csv_reader if student["name"] == student_name
            ]
            if not found:
                os.system("cls||clear")
                print("Estudiante no encontrado!\n")
            else:
                if found[0]["attendance"] == "True":
                    print("El estudiante estuvo presente ese dia\n")
                else:
                    print("El estudiante no asistio ese dia\n")


def main():
    while True:
        print(" Menu ".center(30, "="))
        print("1. Guardar asistencia")
        print("2. Buscar estudiante")
        print("3. Salir")

        try:
            opt = int(input("> "))
            if opt < 1 or opt > 3:
                raise ValueError
        except ValueError:
            os.system("cls||clear")
            print("\nopcion no valida\n")
            continue

        os.system("cls||clear")
        if opt == 1:
            guardar_asistencia()
        if opt == 2:
            buscar_asistencia()
        if opt == 3:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    os.system("cls||clear")
    main()
