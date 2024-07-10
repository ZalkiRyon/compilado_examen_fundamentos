import csv
import random

def asignar_credito(alumnos):
    try:
        data = []
        for i in alumnos:
            datos_usuario = {
                "nombre" : i,
                "credito" : random.randint(50,200)
            }
            data.append(datos_usuario)
        return data
    except Exception as e:
        print({f"Error! mas info : {e} ; {e.with_traceback}"})

def clasificar_alumno(datos):
    try:
        alumnos_bajo = 0
        alumnos_medio = 0
        alumnos_alto = 0
        for i in datos:
            if i['credito'] < 100:
                i['clasificacion_credito'] = "Bajo"
                alumnos_bajo += 1
            elif i['credito'] <= 150:
                i['clasificacion_credito'] = "Medio"
                alumnos_medio += 1
            elif i['credito'] > 150 :
                i['clasificacion_credito'] = "Alto"
                alumnos_alto +=1
        print("Sus datos han sido categorizados!")
        print("*** Resumen ***")
        print(f"Categoria 'Bajo' : {alumnos_bajo}\nCategoria 'Medio' : {alumnos_medio}\nCategoria 'Alto' : {alumnos_alto}")
        print("*** Fin Resumen ***")
        return datos
    except Exception as e:
        print({f"Error! mas info : {e} ; {e.with_traceback}"})

def analisis_creditos(datos_categorizados,agregacion):
    if agregacion == "max" :
        try:
            max_credito = 0
            for i in datos_categorizados:
                if i['credito'] > max_credito:
                    max_credito = i['credito']
            return max_credito
        except Exception as e:
            print({f"Error! mas info : {e} ; {e.with_traceback}"})
    elif agregacion == "min":
        try:
            min_credito = 0
            for i in datos_categorizados:
                if min_credito == 0:
                    min_credito = i['credito']
                elif i['credito'] < min_credito:
                    min_credito = i['credito']
            return min_credito
        except Exception as e:
            print({f"Error! mas info : {e} ; {e.with_traceback}"})
    elif agregacion == "prom":
        try:
            lista_creditos = []
            for i in datos_categorizados:
                lista_creditos.append(i['credito'])
            promedio_creditos = round(sum(lista_creditos) / len(lista_creditos),2)
            return promedio_creditos
        except Exception as e:
            print({f"Error! mas info : {e} ; {e.with_traceback}"})
    else: # El menu se preocupa de que la gente elija solo agregaciones que existan , pero porsiacaso...
        print(f"Agregación {agregacion} no soportada!")
        return None

def generar_reporte(datos_categorizados):
    columnas = ['nombre','credito','clasificacion_credito']
    with open("reporte_creditos.csv","w",encoding='utf-8',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(datos_categorizados)