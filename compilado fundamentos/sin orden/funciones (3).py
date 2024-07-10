import csv
import json

def leer_csv(nombre_archivo):
    try:
        datos = []
        with open(nombre_archivo,'r',encoding='utf-8') as file:
            data_raw = csv.reader(file)
            contador = 0
            for i in data_raw:
                if contador == 0:
                    contador =+ 1
                    continue
                else:
                    diccionario = {
                        "nombre" : i[0],
                        "apellido" : i[1],
                        "edad" : i[2],
                        "rut" : i[3],
                        "AFP" : i[4],
                        "Cargo" : i[5],
                        "antiguedad" : i[6],
                        "Sueldo" : i[7],
                        "Mes" : i[8],
                        "anio" : i[9],
                        "genero" : i[10]
                    }
                    datos.append(diccionario)
            with open (f'datos_json.json','w',encoding='utf-8') as file:
                json.dump(datos,file,ensure_ascii=False,indent=4)  
        return datos
    except Exception as e:
        print(f"Error : {e} - {e.with_traceback}")
        return []


def obtener_mejor_sueldo(datos_json):
    try:
        mejor_sueldo = 0
        datos_persona_mejor_sueldo = {
                        "nombre" : None,
                        "apellido" : None,
                        "edad" : None,
                        "rut" : None,
                        "AFP" : None,
                        "Cargo" : None,
                        "antiguedad" : None,
                        "Sueldo" : None,
                        "Mes" : None,
                        "anio" : None,
                        "genero" : None       
        }
        for i in datos_json:
            sueldo = float(i['Sueldo'])
            if sueldo > mejor_sueldo:
                mejor_sueldo = sueldo
                datos_persona_mejor_sueldo["nombre"] = i["nombre"]
                datos_persona_mejor_sueldo["apellido"] = i["apellido"]
                datos_persona_mejor_sueldo["edad"] = i["edad"]
                datos_persona_mejor_sueldo["rut"] = i["rut"]
                datos_persona_mejor_sueldo["AFP"] = i["AFP"]
                datos_persona_mejor_sueldo["Cargo"] = i["Cargo"]
                datos_persona_mejor_sueldo["antiguedad"] = i["antiguedad"]
                datos_persona_mejor_sueldo["Sueldo"] = i["Sueldo"]
                datos_persona_mejor_sueldo["Mes"] = i["Mes"]
                datos_persona_mejor_sueldo["anio"] = i["anio"]
                datos_persona_mejor_sueldo["genero"] = i["genero"]    
        mensaje_consola = f"El trabajador {datos_persona_mejor_sueldo["nombre"]} {datos_persona_mejor_sueldo["apellido"]} tiene un sueldo de {datos_persona_mejor_sueldo["Sueldo"]:} en el año {datos_persona_mejor_sueldo["anio"]}\nSe ha creado el archivo {datos_persona_mejor_sueldo["nombre"]}_{datos_persona_mejor_sueldo["apellido"]}_info.json"
        with open (f'{datos_persona_mejor_sueldo["nombre"]}_{datos_persona_mejor_sueldo["apellido"]}_info.json','w',encoding='utf-8') as file:
            json.dump(datos_persona_mejor_sueldo,file,ensure_ascii=False,indent=4)            
        return mensaje_consola
    except Exception as e:
        print(f"Error : {e} - Info : {e.with_traceback}")
        return []
    
def buscar_usuario(datos,rut):
    try:
        existe = False
        datos_usuario = []
        for i in datos:
            if i['rut'] == rut:
                existe = True
                datos_usuario.append(i)
        if not existe:
            print(f"El rut {rut} no se ha encontrado, se devolvio nada")
            return []
        else:
            # Devolvemos toda la info que se encuentre para ese rut
            with open (f'datos_rut_{rut}.json','w',encoding='utf-8') as file:
                json.dump(datos_usuario,file,ensure_ascii=False,indent=4)
            return datos_usuario # Imprimimos todo por consola (ese es mi formato)
    except ValueError:
        print(f"Error en el dato otorgado!")
    except Exception as e:
        print(f"Algo ocurrió! : {e} - Mas info : {e.with_traceback}")

def obtener_categorias(datos,columna): # Funcion para obtener valores unicos
    try:
        categorias = []
        for i in datos:
            categorias.append(i[columna])
        categorias = set(categorias)
        categorias = list(categorias)
        return categorias
    except Exception as e:
        print(f"Algo ocurrió! : {e} - Mas info : {e.with_traceback}")

def mejores_sueldos_cargos(datos):
    try:
        cargos = obtener_categorias(datos,'Cargo')

        mejores_sueldos_cargos_2022 = {

        }

        for i in cargos:
            mejores_sueldos_cargos_2022[i] = {
                "nombre" : None,
                "apellido" : None,
                "sueldo" : 0
            }
        for i in datos:
            for j in cargos:
                if (i['Cargo'] == j) and i['anio'] == '2022':
                    sueldo = i['Sueldo']
                    nombre = i['nombre']
                    apellido = i['apellido']
                    if float(sueldo) > float(mejores_sueldos_cargos_2022[j]["sueldo"]):
                        mejores_sueldos_cargos_2022[j]["sueldo"] = sueldo
                        mejores_sueldos_cargos_2022[j]["apellido"] = apellido
                        mejores_sueldos_cargos_2022[j]["nombre"] = nombre
        #Escritura JSON
        with open (f'mejores_sueldos_cargos_2022.json','w',encoding='utf-8') as file:
            json.dump(mejores_sueldos_cargos_2022,file,ensure_ascii=False,indent=4)    

        return mejores_sueldos_cargos_2022
    except Exception as e:
        print(f"Algo ocurrió! : {e} - Mas info : {e.with_traceback}")

def menu(datos):
    while True:
        try:
            print("******* Seleccione que desea realizar *******")
            print("1.- Mejor Sueldo de la compañia")
            print("2.- Buscar información por RUT de un empleado")
            print("3.- Mejores Sueldos del año 2022 por cargo")
            print("4.- Salir")
            opcion = int(input("Seleccione con el número que corresponda : "))
            if opcion == 1:
                mejor_sueldo = obtener_mejor_sueldo(datos)
                print(mejor_sueldo)
            elif opcion == 2:
                rut_empleado = input("Porfavor ingrese el RUT de la persona : ")
                datos_empleado = buscar_usuario(datos,rut_empleado)
                print(datos_empleado)
                if len(datos_empleado) >= 1:
                    print(f'Se creo el archivo datos_rut_{rut_empleado}.json con todos los datos.')
            elif opcion == 3:
                mejor_sueldos_2022 = mejores_sueldos_cargos(datos)
                print("***** Mejores sueldos 2022 por cargo *****")
                for i in mejor_sueldos_2022:
                    print(f"El sueldo de {mejor_sueldos_2022[i]['nombre']} {mejor_sueldos_2022[i]['apellido']} correspondiente al cargo de {i} es de {mejor_sueldos_2022[i]['sueldo']} en el año 2022")
                print("******")
            elif opcion == 4:
                break
        except ValueError:
            print(f"Porfavor, solo elegir con los números que correspondan!")
        except Exception as e:
            print(f"Algo ocurrió! : {e} - Mas info : {e.with_traceback}")

