import funciones as fn

### Pasando de CSV a JSON ###
df = fn.csv_a_json('alumnos_detallado.csv')

### JSON con todos los promedios ###

df_json_promedios = fn.obtener_promedios(df)

### Mejor promedio por asignatura (diccionario de diccionarios) ###

df_mejores_notas_asignatura = fn.mejor_nota_por_asignatura(df_json_promedios)

## Asignaturas con mejor asistencia por año

df_asist_asignaturas = fn.mejor_asitencia_asignatura(df_json_promedios)

## Mejor alumno por año

df_mejor_alumno_anio = fn.mejor_alumno_anio(df_json_promedios)

## Falto el menu, pero no esta dentro del scope del ejercicio