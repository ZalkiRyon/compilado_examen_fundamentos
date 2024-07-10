#NOMBRE: BAYRON BAEZ, BENJAMIN GUERRERO, RODRIGO RUIZ
lista_estudiantes=[]
ListaTitulo=["NOMBRE","EDAD","CURSO","PROMEDIO"]
listacursos=["4° Basico","7° Basico","8° Basico", "1° Basico","2° Basico","3° Basico","5° Basico","6° Basico"]
#Esta funcion sirve para agregar estudiantes
def agregar_estudiante():
    while True:
        try:
            nombre=input("Ingrese el nombre del estudiante: ")
            edad=int(input("Ingrese la edad del estudiante: "))
            curso=input("Ingrese el curso del estudiante, Ejemplo (4° Basico): ")
            promedio=float(input("Ingrese el promedio del estudiante, Ejemplo (6.4): "))
        except ValueError:
            print("Error, ingrese un valor valido")
        else:
            estudiante={
                "Nombre":nombre,
                "Edad":edad,
                "Curso":curso,
                "Promedio":promedio,         
                }
            lista_estudiantes.append(estudiante)
            print("Datos de estudiante ingresados correctamente")
            print("")
            break
#Esta funcion sirve para mostrar los estudiantes
def ver_estudiantes():
    if not lista_estudiantes:
        print("No hay estudiantes en la lista.")
    else:
        for estudiante in lista_estudiantes:
            print(estudiante)
            print("")
#Esta funcion sirve para modificar la lista de estudiantes
def modificar_estudiante():
    ver_estudiantes()
    if lista_estudiantes:
        nombre = input("Ingrese el nombre del estudiante a modificar: ")
        for estudiante in lista_estudiantes:
            if estudiante["Nombre"] == nombre:
                try:
                    nuevo_nombre = input("Nuevo nombre del estudiante: ")
                    nueva_edad = int(input("Nueva edad del estudiante: "))
                    nuevo_curso = input("Nuevo curso del estudiante, Ejemplo (4° Basico): ")
                    nuevo_promedio = float(input("Nuevo promedio del estudiante, Ejemplo (6.4): "))
                except ValueError:
                    print("Error, ingrese un valor valido")
                else:
                    estudiante["Nombre"] = nuevo_nombre
                    estudiante["Edad"] = nueva_edad
                    estudiante["Curso"] = nuevo_curso
                    estudiante["Promedio"] = nuevo_promedio
                    print("Estudiante modificado correctamente!")
                    break
        else:
            print("El estudiante no se encuentra en la lista.")
#Esta funcion sirve para eliminar estudiantes de la lista
def eliminar_estudiante():
    ver_estudiantes()
    if lista_estudiantes:
        try:
            nombre = input("Ingrese el nombre del estudiante que desea borrar: ")
        except ValueError:
            print("Ingrese una opcion valida")
        else:
            for estudiante in lista_estudiantes:
                if estudiante["Nombre"] == nombre:
                    lista_estudiantes.remove(estudiante)
                    print("Estudiante eliminado correctamente!")
                    break
            else:
                print("El estudiante no se encuentra en la lista.")
#Esta funcion sirve para guardar la lista en un archivo .txt
def guardar_archivo():
    with open("Estudiantes.txt","w",encoding="utf-8") as archivo:
        archivo.write(f"{ListaTitulo}")
        for estudiante in lista_estudiantes:
                archivo.write(f"\n{estudiante['Nombre']},{estudiante['Edad']},{estudiante['Curso']},{estudiante['Promedio']}")
    print("Archivo creado exitosamente")
#Muestra el menu
def mostrar_menu():
        print("1.- Agregar estudiante")
        print("2-  Ver todos los estudiantes")
        print("3.- Modificar producto")
        print("4.- Eliminar producto")
        print("5.- Guardar coleccion en un archivo")
        print("6.- Salir del programa")
        print("")
#Aqui se ejecutan las acciones
def menu():
    print("")
    while True:
        mostrar_menu()
        try:
            opcion=int(input("Seleccione una opcion: "))
        except ValueError:
            print("Opcion invalida, intentelo de nuevo")
        else:
            if opcion==1:
                agregar_estudiante()
            elif opcion==2:
                ver_estudiantes()
            elif opcion==3:
                modificar_estudiante()
            elif opcion==4:
                eliminar_estudiante()
            elif opcion==5:
                guardar_archivo()
            elif opcion==6:
                print("Saliendo del programa...")
                break
            else:
                print("Seleccione una opcion valida, intentelo de nuevo")
