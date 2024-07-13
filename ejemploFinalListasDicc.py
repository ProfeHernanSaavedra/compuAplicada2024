# Inicializamos una lista de diccionarios que representa el inventario de productos
inventario = []

# Ciclo principal del programa con el menú
while True:
    print("\nMenú:")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Actualizar cantidad en stock")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ")

    if opcion == '1':
        # Mostrar inventario
        if inventario:
            print("\nInventario actual:")
            for producto in inventario:
                print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad en stock: {producto['cantidad']}")
        else:
            print("\nEl inventario está vacío.")
    
    elif opcion == '2':
        # Agregar producto
        nombre = input("Ingrese el nombre del nuevo producto: ")
        precio = float(input("Ingrese el precio del nuevo producto: "))
        cantidad = int(input("Ingrese la cantidad en stock del nuevo producto: "))
        nuevo_producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        inventario.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado al inventario.")
    
    elif opcion == '3':
        # Buscar producto
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in inventario:
            if producto['nombre'] == nombre_buscar:
                print(f"\nInformación del producto '{nombre_buscar}':")
                print(f"Precio: ${producto['precio']}")
                print(f"Cantidad en stock: {producto['cantidad']}")
                encontrado = True
                break
        if not encontrado:
            print(f"\nEl producto '{nombre_buscar}' no se encontró en el inventario.")
    
    elif opcion == '4':
        # Actualizar cantidad en stock
        nombre_actualizar = input("Ingrese el nombre del producto para actualizar su cantidad en stock: ")
        for producto in inventario:
            if producto['nombre'] == nombre_actualizar:
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad en stock para '{nombre_actualizar}': "))
                producto['cantidad'] = nueva_cantidad
                print(f"Se ha actualizado la cantidad en stock de '{nombre_actualizar}' a {nueva_cantidad}.")
                break
        else:
            print(f"\nEl producto '{nombre_actualizar}' no se encontró en el inventario.")
    
    elif opcion == '5':
        # Eliminar producto
        nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        for producto in inventario:
            if producto['nombre'] == nombre_eliminar:
                inventario.remove(producto)
                print(f"El producto '{nombre_eliminar}' ha sido eliminado del inventario.")
                break
        else:
            print(f"\nEl producto '{nombre_eliminar}' no se encontró en el inventario.")
    
    elif opcion == '6':
        # Salir del programa
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú (1-6).")
