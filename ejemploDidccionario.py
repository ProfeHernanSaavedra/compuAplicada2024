# Definimos un diccionario de información de una persona
persona = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Ciudad de México',
    'profesion': 'Ingeniero'
}

# Accedemos e imprimimos algunos datos del diccionario
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona["edad"]}')
print(f'Cuidad: {persona["ciudad"]}')
print(f'Profesión: {persona["profesion"]}')

# Modificamos un valor en el diccionario
persona['edad'] = 32

# Imprimimos el diccionario actualizado
print('\nDiccionario actualizado:')
print(persona)
