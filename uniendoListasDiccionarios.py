# Creamos una lista de diccionarios que representan libros
libros = [
    {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "año_publicacion": 1943},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año_publicacion": 1967},
    {"titulo": "1984", "autor": "George Orwell", "año_publicacion": 1949},
    {"titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "año_publicacion": 1997}
]

# Mostramos la lista de libros
print("Lista de libros:")
for libro in libros:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año de publicación: {libro['año_publicacion']}")

# Añadimos un nuevo libro a la lista
nuevo_libro = {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "año_publicacion": 1605}
libros.append(nuevo_libro)

# Mostramos la lista de libros actualizada
print("\nLista de libros actualizada:")
for libro in libros:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año de publicación: {libro['año_publicacion']}")

# Buscamos un libro por su título
titulo_buscar = "1984"
for libro in libros:
    if libro['titulo'] == titulo_buscar:
        print(f"\nInformación del libro '{titulo_buscar}':")
        print(f"Autor: {libro['autor']}, Año de publicación: {libro['año_publicacion']}")
        break
else:
    print(f"\nEl libro '{titulo_buscar}' no se encontró en la lista.")

# Eliminamos un libro de la lista por su título
titulo_eliminar = "El principito"
for libro in libros:
    if libro['titulo'] == titulo_eliminar:
        libros.remove(libro)
        print(f"\nSe ha eliminado el libro '{titulo_eliminar}' de la lista.")
        break

# Mostramos la lista de libros actualizada después de eliminar
print("\nLista de libros actualizada después de eliminar:")
for libro in libros:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año de publicación: {libro['año_publicacion']}")
