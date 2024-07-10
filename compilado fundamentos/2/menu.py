import funciones as fn
def menu(alumnos):
    while True:
        try:
            print("Bienvenido, seleccione una de las opciones : ")
            print("1.- Agregar creditos a los alumnos (simulacion que reemplaza los valores si se ejecuta denuevo)")
            print("2.- Clasificar creditos alumnos")
            print("3.- Calcular estadisticas")
            print("4.- Generar reporte")
            print("5.- Salir")
            opcion = int(input("Porfavor seleccione el número que indica su opción : "))
            if opcion == 1:
                try:
                    datos = fn.asignar_credito(alumnos)
                    print(f"Sus datos generados son : ")
                    print(datos)
                except Exception as e:
                    print(f"Error ! : {e} ; {e.with_traceback}")

            elif opcion == 2:
                try:
                    datos_categorizados = fn.clasificar_alumno(datos) # La funcion por si imprime el resumen categorizado!
                except UnboundLocalError:
                    print("Debe de haber asignado los creditos primero en la opción 1 primero!")
            elif opcion == 3:
                    try: # Try para ver si existe la variable datos categorizados y chequear error
                        if datos_categorizados:
                            while True:
                                try:
                                    print("Seleccione que calculo desea hacer")
                                    print("1 .- Obtener el máximo credito")
                                    print("2 .- Obtener el credito minimo")
                                    print("3 .- Obtener el promedio de creditos")
                                    print("4 .- Ir al menu principal")
                                    opcion_calculo = int(input("Seleccione con el número que corresponda : "))
                                    if opcion_calculo == 1:
                                        max_credito = fn.analisis_creditos(datos_categorizados,"max")
                                        print(f"El credito mas alto es de :  {max_credito}")
                                    elif opcion_calculo == 2:
                                        min_credito = fn.analisis_creditos(datos_categorizados,"min")
                                        print(f"El menor credito otorgado fue de : {min_credito}")
                                    elif opcion_calculo == 3:
                                        prom_credito = fn.analisis_creditos(datos_categorizados,"prom")
                                        print(f"El promedio de creditos otorgados es de : {prom_credito}")
                                    elif opcion_calculo == 4:
                                        break
                                    else:
                                        print("Debe de elegir un valor entre 1 y 4!")
                                except ValueError:
                                    print("Debe de seleccionar con un número válido!")
                    except UnboundLocalError:
                        print("Debe de haber asignado los creditos primero en la opción 1 primero!")
            elif opcion == 4:
                try:
                    fn.generar_reporte(datos_categorizados)
                    print("Reporte generado en archivo 'reporte_creditos.csv' ")
                except UnboundLocalError:
                    print("Debe de haber asignado los creditos primero en la opción 1 primero!")
                except Exception as e:
                    print(f"Error ! : {e} ; {e.with_traceback}")
            elif opcion == 5:
                print("Terminando programa ....")
                break
            else:
                print("Debe de seleccionar un valor entre 1 y 5!")
        except ValueError:
            print("Debe de dar un valor valido!")