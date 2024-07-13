# Definimos una lista de números
numeros = [1, 2, 3, 4, 5]

# Imprimimos la lista completa
print("Lista de números:", numeros)

# Accedemos a elementos individuales de la lista por su índice
primer_numero = numeros[0]
segundo_numero = numeros[1]

print("Primer número:", primer_numero)
print("Segundo número:", segundo_numero)

# Modificamos un elemento de la lista
numeros[2] = 10

# Añadimos un nuevo elemento al final de la lista
numeros.append(6)

# Eliminamos el tercer elemento de la lista
del numeros[2]

# Imprimimos la lista actualizada
print("Lista actualizada:", numeros)

# Iteramos sobre la lista e imprimimos cada elemento
print("Recorriendo la lista:")
for numero in numeros:
    print(numero)
 