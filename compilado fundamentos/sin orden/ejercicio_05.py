#Crear una aplicación que le pida al usuario la siguiente información:
#- Nombre
#- Rut
#- Dirección
#- Cantidad de servicios que tiene en su domicilio, debe seleccionar SOLO una
#Agua:
#- Esval
#- Aguas Andina
#Gas:
#- Lipigas
#- Gasco
#- Abastible
#Luz:
#- CGE
#- Colbun
#- Chilquinta
#- Chilectra
#Internet:
#- VTR
#- Movistar
#- Entel
#Teléfono:
#- Entel
#- WOM
#- Movistar
#- Claro
import json

def to_dictionary(name, id, address, water, gas, electricity, internet, phone):
    user_info = {
        'nombre': name,
        'rut': id,
        'direccion': address,
        'servicios':{
            'agua': water,
            'gas': gas,
            'electricidad': electricity,
            'internet': internet,
            'telefono': phone
        }
    }
    return user_info

def to_json(data):
    with open('user.json', 'w') as file:
        data_json = json.dump(data, file)
    return data_json

user = []
#
while True:
    print('\n1. Ingresa un usuario: ')
    print('0. Salir: ')
    opt = input(': ')

    if opt == '1':
        name = input('\nIngrese nombre: ')
        id = input('Ingrese rut: ')
        address = input('Ingrese direccion: ')
        #
        water = input('\nEscribe el nombre de tu compañia:\nEsval\nAguas Andinas\n: ')
        gas = input('\nEscribe el nombre de tu compañia:\nLipigas\nGasco\nAbastible\n: ')
        electricity = input('\nEscribe el nombre de tu compañia:\nCGE\nColbun\nChilquinta\nChilectra\n: ')
        internet = input('\nEscribe el nombre de tu compañia:\nVTR\nMovistar\nEntel\n: ')
        phone = input('\nEscribe el nombre de tu compañia:\nEntel\nWOM\nMovistar\nClaro\n: ')
        #
        user.append(to_dictionary(name, id, address, water, gas, electricity, internet, phone))
    else:
        to_json(user)
        break
