import os
usuario = []
registro = []
libro = []
titulo = []

def registro ():
    try:
        usuario = input("Ingrese su nombre de usuario")
        titulo = input("Ingrese el nombre del libro: ")
        autor = input("Ingrese el nombre del Autor del libro: ")
        año = int(input("Ingrese el año de publicaión del libro: "))
        sku = int(input("Ingrese el sku del libro: "))

        if titulo == "" or autor == "" or año == 0 or sku == 0:
         print("El nombre o número ingresado del libro no son válidos")


        libro = {
            'titulo' : titulo,
            'autor' : autor,
            'año' : año,
            'sku' : sku,
        }
        libro.append (libro)
        print("El registro del libro se realizo correctamente")
    except ValueError:
        print("Titulo o datos ingresados no son válidos")
        print("Por favor intente nuevamente: ")


def prestar ():
    usuario = input("Ingrese su usuario")


def lista ():
    print("TÍTULO \\t AUTOR \\t AÑO DE PUBLICACIÓN \\t SKU \n")
    for libro in titulo:
        print(f"{libro['titulo']}\\t {libro['autor']}\\t {libro['año']}\\t {libro['sku']}\n")

def imrpimir ():
    try:
        op = int(input("¿Como desea imprimir el reporte de préstamo?\n 1.Todos \n 2. Autor \n 3. Lista de todos los libros"))
        if op == 1:
            with open('planilla_registro.txt','w') as archivo:
            archivo.write("titulo\\t autor\\t año\\t sku")
            for libro in registro:
            archivo.write(f"{libro['titulo']}\\t {libro['autor']}\\t {libro['año']}\\t {libro['sku']}\n")
            print("La planilla se realizó exitosamente")
        elif op == 2:
            autor = input(" Ingrese el nombre del autor").lower ()

            print("El nombre del Autor ingresado no existe")
        else:
            with open(f'planilla{autor}.txt', 'w') as archivo:
                archivo.write ("titulo \\t autor \\t año \\t sku\n")
                for libro in registro:
                    if libro['titulo'].lower () == titulo:
                        print('Planilla generada exitosamente en: ')

    except ValueError:
        print("Los datos ingresados son incorrector, intentelo nuevamente")


def menu ():
    while True:
        try:
            print ("n. 1 Registrar libro\n 2. Prestar libro \n 3. Listar de todos los libros \n 4. Imprimir el reposte de préstamos\n 5. Salir del Programa")
            op = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Dato ingresado incorrecto, intentelo nuevamente")
            if op == 1:
                registro ()
            elif op == 2:
                prestar ()
            elif op == 3:
                lista ()
            elif op == 4:
                imrpimir ()
            elif op == 5:
                print("Esta saliendo del programa")
                break
            else:
                 print("La opcion ingresada no es valida, por favor interlo nuevamente")


              