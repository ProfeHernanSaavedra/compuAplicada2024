# Definimos un diccionario de estudiantes donde la clave es el nombre y el valor es una lista de calificaciones
estudiantes = {
    'Juan': [85, 90, 88],
    'María': [92, 88, 95],
    'Pedro': [78, 85, 80]
}

# Iteramos sobre el diccionario de estudiantes para mostrar sus nombres y calificaciones
for nombre, calificaciones in estudiantes.items():
    print(f'Estudiante: {nombre}')
    print('Calificaciones:', calificaciones)
    
    # Calculamos el promedio de calificaciones
    promedio = sum(calificaciones) / len(calificaciones)
    print(f'Promedio: {promedio:.2f}')
    
    # Mostramos la calificación más alta
    maxima_calificacion = max(calificaciones)
    print(f'Calificación más alta: {maxima_calificacion}')
    
    # Mostramos la calificación más baja
    minima_calificacion = min(calificaciones)
    print(f'Calificación más baja: {minima_calificacion}')
    
    print('-' * 30)  # Separador entre estudiantes
