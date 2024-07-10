import csv
import json

def csv_a_json(archivo): # CSV a JSON (Siempre se saltara la primera fila)
    datos = []
    with open(archivo,'r',encoding='utf-8') as csvfile:
        contador_fila = 0
        data_raw = csv.reader(csvfile)
        for i in data_raw:
            if contador_fila == 0:
                contador_fila += 1
            else:
                datos.append(i)
    return datos

def obtener_promedios(df): # Funcion que transforma las notas en promedio y devuelve todas las columnas en formato JSON
    datos_transformados = []
    for i in df:
        datos_alumno = {
            'rut' : i[0],
            'nombre' : i[1],
            'apellido' : i[2],
            'curso' : i[3],
            'asignatura' : i[4],
            'promedio' : round( ( float(i[5]) + float(i[6]) + float(i[7]) ) / 3, 2),
            'asistencia' : i[8]
        }
        datos_transformados.append(datos_alumno)
    return datos_transformados

def obtener_asignaturas(df_json): # Funcion que obtiene todas las asignaturas unicas del JSON
    asignaturas = []

    for i in df_json:
        asignaturas.append(i['asignatura'])
    asignaturas = set(asignaturas)
    asignaturas = list(asignaturas)
    asignaturas.sort()
    return asignaturas

def obtener_anios(df_json):
    anios = []
    
    for i in df_json:
        anios.append(i['curso'])
    anios = set(anios)
    anios = list(anios)
    return anios

def obtener_categorias(df_json,nombre_columna):
    categorias = []
    for i in df_json:
        categorias.append(i[nombre_columna])
    categorias = set(categorias)
    categorias = list(categorias)
    return categorias

def mejor_nota_por_asignatura(df_json): # Funcion que devuelve las mejores notas por asignatura
    asignaturas = obtener_asignaturas(df_json)

    # 1.-Creamos un diccionario con todas las asignaturas inicializado en 0

    mejor_notas_asignaturas = {}

    for i in asignaturas:
        mejor_notas_asignaturas[i] = {
            "mejor_nota" : 0.0,
            "rut_alumno" : ""
        }

    # 2.- Chequeamos asignatura por asignatura si es la mejor nota o no
        
    for i in df_json:
        asignatura = i['asignatura']
        nota = i['promedio']
        rut = i['rut']
        for j in list(mejor_notas_asignaturas.keys()):
            if asignatura == j:
                if float(nota) > float(mejor_notas_asignaturas[j]['mejor_nota']):
                    mejor_notas_asignaturas[j]['mejor_nota'] = nota
                    mejor_notas_asignaturas[j]['rut_alumno'] = rut

    return mejor_notas_asignaturas

def mejor_asitencia_asignatura(df_json): # Funcion que devuelve la asignatura con mejor asistencia por año(curso)
    # Calculamos primero promedio de asistencia de cada asignatura
    anios = obtener_anios(df_json)
    asignaturas = obtener_asignaturas(df_json)
    # Creamos diccionario con cada promedio de asistencia por año de cada asignatura
    diccionario_asistencia_anio = {}
    
    for i in anios:
        diccionario_asistencia_anio[i] = {}
        for j in asignaturas:
            diccionario_asistencia_anio[i][j] = []
    # Apendamos asistencias a cada asignatura
    for i in df_json:
        curso = i['curso']
        asignatura = i['asignatura']
        asistencia = i['asistencia']
        diccionario_asistencia_anio[curso][asignatura].append(int(asistencia))
    # Eliminamos asignaturas que no corresponden a cierto anio
    llaves_dict = list(diccionario_asistencia_anio.keys())
    for i in llaves_dict:
        for j in asignaturas:
            if len(diccionario_asistencia_anio[i][j]) < 1:
                del diccionario_asistencia_anio[i][j]
    # Ahora convertimos en promedio
    for i in llaves_dict:
        llaves_asignaturas = list(diccionario_asistencia_anio[i].keys())
        for j in llaves_asignaturas:
            diccionario_asistencia_anio[i][j] = round(sum(diccionario_asistencia_anio[i][j]) / len(diccionario_asistencia_anio[i][j]),2)
    # Creamos diccionario con todos los anios y dentro de de este asignatura con mejor asistencia
    mejor_asistencia_anio = {}
    for i in anios:
        mejor_asistencia_anio[i] = {
            "asist_mejor" : "",
            "prom_asistencia" : 0
        }
    
    for i in llaves_dict:
        for j in asignaturas:
            asignaturas_disponibles = list(diccionario_asistencia_anio[i].keys())
            if j in(asignaturas_disponibles):
                prom_asignatura = diccionario_asistencia_anio[i][j]
                if prom_asignatura > mejor_asistencia_anio[i]['prom_asistencia']:
                    mejor_asistencia_anio[i]['prom_asistencia'] = prom_asignatura
                    mejor_asistencia_anio[i]['asist_mejor'] = j

    return mejor_asistencia_anio

def mejor_alumno_anio(df_json):
    anios = obtener_anios(df_json)

    # Diccionario vacio con anios y sus mejores alumnos y notas

    mejores_notas_anio = {}

    for i in anios:
        mejores_notas_anio[i] = {
            "mejor_alumno" : "",
            "promedio" : 0
        }
    
    # Obtener promedios finales de cada alumno
    ruts_unicos = obtener_categorias(df_json,"rut")

    promedios_finales = {}

    for i in ruts_unicos:
        promedios_finales[i] = 0

    for i in ruts_unicos:
        notas_alumno = []
        for j in df_json:
            if i == j['rut']:
                nota = j['promedio']
                notas_alumno.append(nota)
        promedios_finales[i] = (sum(notas_alumno)/len(notas_alumno))
    
    for i in ruts_unicos:
        for j in df_json:
            if i in list(j.values()):
               anio = j['curso']
               promedio_final = promedios_finales[i]
            
               if float(promedio_final) > float(mejores_notas_anio[anio]["promedio"]):
                    mejores_notas_anio[anio]["promedio"] = promedio_final
                    mejores_notas_anio[anio]["mejor_alumno"] = i
    
    return mejores_notas_anio

    