''' Integrantes del grupo: 
- Ignacio Chacón 
- Miguel Muñoz 
- David Nahuelcar
'''


import estudiantes as llamar
import time

lista_main = []
matriz_main = [[]]

while True:
    llamar.menu()
    try:
        opcion = int(input("\nIngrese una opción de 1 al 6 ---> "))
    except:
        print("Valor inválido, solo se aceptan números")
    else:
        if opcion == 1:
            llamar.agregar_estudiante(lista_main)
        elif opcion == 2:
            llamar.mostrar(lista_main)
        elif opcion == 4:
            alumno = input(": ")
            llamar.eliminar_producto(alumno)
        elif opcion == 5:
            llamar.archivo(lista_main, matriz_main)
        elif opcion == 6:
            print("Saliendo del programa....")
            time.sleep(1)
            print("....")
            time.sleep(1)
            print("....")
            time.sleep(1)
            print("Muchas gracias por usar uesro programa :)")
            break
        else:
            print("La opción ingresada no es válida, solo se puede del 1 al 6.")
            
