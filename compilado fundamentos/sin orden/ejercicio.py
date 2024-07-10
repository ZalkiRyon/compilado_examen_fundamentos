# Librerias
import funciones as fn
import json
# Parametros
ARCHIVO = 'sueldos_1.csv'
# Datos
datos = fn.leer_csv(ARCHIVO)
# Menu
fn.menu(datos)