import os
import time
import random
import csv

op = 0
# Generar numero de pedido


lista_pedidos = []


def limpiar_pantalla():
    os.system('cls')

def menu():
    print('¡Bienvenido a nuestra tienda "CatPremium"!\n'
          'Nuestro menu:'
          '\n1. Registrar pedido'
          '\n2. Listar todos los pedidos'
          '\n3. Imprimir hoja de ruta'
          '\n4. Salir del programa')
    
    validar_op = True
    while validar_op:
        try:
            op = int(input('¿Que deseas?: '))
            if op not in range(1,5):
                print('¡Error! Ingresa un valor entre 1 y 4\n')
            else:
                validar_op = False
        except ValueError:
            print('¡Error! Ingresa un valor numerico\n')
    return op


def registrar_pedido():
    num_pedido_random = random.randint(1, 1000)
    num_pedido = num_pedido_random
    limpiar_pantalla()
    print('Seleccionaste registrar pedido:\n')
    num_sacos_5kilos = 0
    num_sacos_10kilos = 0
    num_sacos_20kilos = 0



    # Solicitar nombre, apellido, comuna
    nombre = input('¿Cual es tu nombre?: ')
    apellido = input('¿Cual es tu apellido?: ')
    cliente = (nombre + ' ' + apellido)
    direccion = input('¿Cual es tu dirección?: ')

    validar_sector = True
    while validar_sector:
        sector = input('¿En cual comuna vives?: ').upper()
        if sector not in ['SAN BERNARDO', 'CALERA DE TANGO', 'BUIN']:
            print('\nSolo realizamos envios a: San Bernardo, Calera de tango y Buin, por favor selecciona una de esas direcciones')
        else:
            validar_sector = False
        

    # Menu de pedido 
    menu_pedido_sacos = True
    while menu_pedido_sacos:
        validar_pedido = True
        while validar_pedido:
            print('\nMenu de pedido:'
                '\n1. Saco de 5 kilos'
                '\n2. Saco de 10 kilos'
                '\n3. Saco de 20 kilos'
                '\n4. Volver al menu principal')
            try:
                pedido = int(input('¿Cual opción deseas?: '))
                if pedido not in range(1,5):
                    print('¡Error! Selecciona un valor entre 1 y 4\n')
                else:
                    validar_pedido = False
            except ValueError:
                print('¡Error! Ingresa un valor\n')


        # Solicitar la cantidad de sacos a solicitar
        if pedido == 1:
            print('\nSeleccionaste el saco de 5 kilos')
            validar_sacos = True
            while validar_sacos:
                try:
                    num_sacos_5kilos = int(input('¿Cuantos sacos de 5 kilos deseas?: '))
                    if num_sacos_5kilos <= 0:
                        print('¡Error! Ingresa un valor mayor a 0\n')
                    else: 
                        validar_sacos = False
                except ValueError:
                    print('¡Error! Ingresa un numero\n')
            print(f'\nSe agregaron {num_sacos_5kilos} sacos de 5 kilos a tu pedido con exito')
            time.sleep(2)

        elif pedido == 2:
            print('\nSeleccionaste el saco de 10 kilos')
            validar_sacos = True
            while validar_sacos:
                try:
                    num_sacos_10kilos = int(input('¿Cuantos sacos de 10 kilos deseas?: '))
                    if num_sacos_10kilos <= 0:
                        print('¡Error! Ingresa un valor mayor a 0\n')
                    else: 
                        validar_sacos = False
                except ValueError:
                    print('¡Error! Ingresa un numero\n')
            print(f'\nSe agregaron {num_sacos_10kilos} sacos de 10 kilos a tu pedido con exito')
            time.sleep(2)


        elif pedido == 3:
            print('\nSeleccionaste el saco de 20 kilos')
            validar_sacos = True
            while validar_sacos:
                try:
                    num_sacos_20kilos = int(input('¿Cuantos sacos de 20 kilos deseas?: '))
                    if num_sacos_20kilos <= 0:
                        print('¡Error! Ingresa un valor mayor a 0\n')
                    else: 
                        validar_sacos = False
                except ValueError:
                    print('¡Error! Ingresa un numero\n')
            print(f'\nSe agregaron {num_sacos_20kilos} sacos de 20 kilos a tu pedido con exito')
            time.sleep(2)

        elif pedido == 4:
            pedido_actual = {'nro pedido':num_pedido, 'cliente':cliente, 'direccion':direccion, 'sector':sector, 'sacos 5 kgs':num_sacos_5kilos, 'sacos 10kgs':num_sacos_10kilos, 'sacos 20kgs':num_sacos_20kilos}
            lista_pedidos.append(pedido_actual)
            menu_pedido_sacos = False
            num_sacos_5kilos = 0
            num_sacos_10kilos = 0
            num_sacos_20kilos = 0
            num_pedido += 1
            print('\nSeleccionaste salir al menu principal')
            time.sleep(2)
            
        
    
    # Reiniciar variables para un nuevo pedido


def listar_pedidos():
    limpiar_pantalla()
    print('Seleccionaste listar los pedidos:\n')
    formato_planilla = f'{{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}}'
    print(formato_planilla.format('Nro. Pedido', 'Cliente', 'Dirección', 'Sector', 'Saco 5kg', 'Saco 10kg', 'Saco 20kg'))
    for pedido in lista_pedidos:
            print(formato_planilla.format(pedido['nro pedido'], pedido['cliente'], pedido['direccion'], pedido['sector'],pedido['sacos 5 kgs'],pedido['sacos 10kgs'],pedido['sacos 20kgs']))
    input('\nPresiona Enter para volver al menu principal')
  

def imprimir_hoja_de_ruta():
    limpiar_pantalla()
    formato_planilla = f'{{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}}'

    print('Seleccionaste imprimir hoja de ruta\n')
    # Usuario debe elegir alguno de los sectores
    print('Hojas de rutas:'
          '\n1. San Bernardo'
          '\n2. Calera de Tango'
          '\n3. Buin')
    validar_hoja_ruta = True
    while validar_hoja_ruta:
        try:
            hoja_de_ruta = int(input('¿Cual hoja de ruta deseas imprimir?: '))
            if hoja_de_ruta not in range(1,4):
                print('¡Error! Selecciona un valor entre 1 y 4\n')
            else:
                validar_hoja_ruta = False
        except ValueError:
            print('¡Error! Ingresa un valor numerico\n')

    

    if hoja_de_ruta == 1:
        limpiar_pantalla()
        print('Hoja de ruta de San Bernardo:\n')
        formato_planilla = f'{{:<{20}}}'
        with open('HojaDeRutaSanBernardo.txt', 'w') as archivo:
            archivo.write(formato_planilla.format('Nro. Pedido'))
            archivo.write(formato_planilla.format('Cliente'))
            archivo.write(formato_planilla.format('Dirección'))
            archivo.write(formato_planilla.format('Sector'))
            archivo.write(formato_planilla.format('Saco 5kg'))
            archivo.write(formato_planilla.format('Saco 10kg'))
            archivo.write(formato_planilla.format('Saco 20kg'))
            archivo.write('\n')
            formato_planilla = f'{{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}}'
            for pedido in lista_pedidos:
                print(pedido['direccion'])
                if pedido['sector'] == 'SAN BERNARDO':
                    
                    archivo.write(formato_planilla.format(pedido['nro pedido'], pedido['cliente'], pedido['direccion'], pedido['sector'],pedido['sacos 5 kgs'],pedido['sacos 10kgs'],pedido['sacos 20kgs']))
                    archivo.write('\n')
        
        with open('HojaDeRutaSanBernardo.txt', 'r') as archivo:
            lectura = archivo.read()
            print(lectura)
        input('Presiona enter para volver al menu')

    elif hoja_de_ruta == 2:
        limpiar_pantalla()
        print('Hoja de ruta de Calera de Tango:\n')
        formato_planilla = f'{{:<{20}}}'
        with open('HojaDeRutaCaleraDeTango.txt', 'w') as archivo:
            archivo.write(formato_planilla.format('Nro. Pedido'))
            archivo.write(formato_planilla.format('Cliente'))
            archivo.write(formato_planilla.format('Dirección'))
            archivo.write(formato_planilla.format('Sector'))
            archivo.write(formato_planilla.format('Saco 5kg'))
            archivo.write(formato_planilla.format('Saco 10kg'))
            archivo.write(formato_planilla.format('Saco 20kg'))
            archivo.write('\n')
            formato_planilla = f'{{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}}'
            for pedido in lista_pedidos:
                if pedido['sector'] == 'CALERA DE TANGO':
                    
                    archivo.write(formato_planilla.format(pedido['nro pedido'], pedido['cliente'], pedido['direccion'], pedido['sector'],pedido['sacos 5 kgs'],pedido['sacos 10kgs'],pedido['sacos 20kgs']))
                    archivo.write('\n')
        
        with open('HojaDeRutaCaleraDeTango.txt', 'r') as archivo:
            lectura = archivo.read()
            print(lectura)
                    
            

            

        input('Presiona enter para volver al menu')

    elif hoja_de_ruta == 3:
        limpiar_pantalla()
        print('Hoja de ruta de Buin:\n')
        formato_planilla = f'{{:<{20}}}'
        with open('HojaDeRutaBuin.txt', 'w') as archivo:
            archivo.write(formato_planilla.format('Nro. Pedido'))
            archivo.write(formato_planilla.format('Cliente'))
            archivo.write(formato_planilla.format('Dirección'))
            archivo.write(formato_planilla.format('Sector'))
            archivo.write(formato_planilla.format('Saco 5kg'))
            archivo.write(formato_planilla.format('Saco 10kg'))
            archivo.write(formato_planilla.format('Saco 20kg'))
            archivo.write('\n')
            formato_planilla = f'{{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}}'
            for pedido in lista_pedidos:
                if pedido['sector'] == 'BUIN':
                    
                    archivo.write(formato_planilla.format(pedido['nro pedido'], pedido['cliente'], pedido['direccion'], pedido['sector'],pedido['sacos 5 kgs'],pedido['sacos 10kgs'],pedido['sacos 20kgs']))
                    archivo.write('\n')
        with open('HojaDeRutaBuin.txt', 'r') as archivo:
            lectura = archivo.read()
            print(lectura)
        
        input('Presiona enter para volver al menu')

def salir_del_programa():
    limpiar_pantalla()
    print('Seleccionaste salir del programa...\n\n¡Vuelve pronto!')
    with open('ListaPedidos.csv', 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(['Nro. Pedido', 'Cliente', 'Dirección', 'Sector', 'Saco 5kg', 'Saco 10kg', 'Saco 20kg'])
        for pedido in lista_pedidos:
            lista = []
            for valor in pedido.values():
                lista.append(valor)
            escritor_csv.writerow(lista)
            





while op != 4:
    limpiar_pantalla()
    op = menu()
    if op == 1:
        registrar_pedido()

    elif op == 2:
        listar_pedidos()

    elif op == 3:
        imprimir_hoja_de_ruta()

    elif op == 4:
        salir_del_programa()