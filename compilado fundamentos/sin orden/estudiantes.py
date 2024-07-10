import csv

lista_estudiante = []

matrizE = [[]]

def agregar_estudiante(lista_estudiante):

    nombre = input("\nIngrese el nombre y apellido del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    curso = input("Curso del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))

    lista_estudiante.append([nombre, edad, curso, promedio])
    print("Los datos se han agregado correctamente")

def mostrar (lista_estudiante):
    print("Nombre -- Edad -- Curso -- Promedio")
    for i in lista_estudiante:
        print(i)

def eliminarAlumno(alumno):
    if not alumno in lista_estudiante:
        print("El alumno que ingresó no existe.")
    elif alumno in lista_estudiante:
        lista_estudiante.remove(alumno)
        print("El alumno ha sido eliminado.")

def archivo(lista_estudiante, matrizE):
    with open('nuevo_archivo.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # Escribir una fila en el archivo CSV
        escritor_csv.writerow(lista_estudiante)
        # Escribir múltiples filas en el archivo CSV
        escritor_csv.writerows(matrizE)
    
    print("Se creó correctamente el archivo .CSV")

def menu (): 
    print("\n</>  Menú de Opciones </>\n")
    print("1. Agregar un estudiante.\n2. Ver todos los estudiantes.\n3. Modificar un estudiante.\n4. Eliminar un estudiante\n5. Guardar colección en un archivo\n6. Salir del programa.")
def eliminar_producto ():
    if agregar_estudiante in lista_estudiante:
        print("")


def guardar_Archivo():
    with open ("lista_archivo.txt",'w') as archivo:
        archivo.write (f"{lista_estudiante}")
