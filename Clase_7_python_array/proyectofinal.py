# 1. TUPLA: Categorías fijas (No cambian durante la ejecución)
CATEGORIAS = ('Electronica', 'Ropa', 'Alimentos')

# 2. DICCIONARIO: Info de productos {nombre: {detalles}}
inventario = {}

# 3. LISTA: Nombres de productos disponibles para mostrar rápido
productos_lista = []

# 4. SET: Marcas únicas (No permite duplicados)
marcas_unicas = set()

def menu():
    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar por categoría")
        print("4. Ver marcas únicas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ").capitalize()
            precio = float(input("Precio: "))
            stock = int(input("Cantidad en stock: "))
            marca = input("Marca: ").upper()
            
            print(f"Categorías disponibles: {CATEGORIAS}")
            cat = input("Seleccione categoría: ").capitalize()

            if cat in CATEGORIAS:
                # Guardar en Diccionario
                inventario[nombre] = {"precio": precio, "stock": stock, "categoria": cat}
                # Guardar en Lista
                if nombre not in productos_lista:
                    productos_lista.append(nombre)
                # Guardar en Set (las marcas no se repiten)
                marcas_unicas.add(marca)
                print("¡Producto agregado con éxito!")
            else:
                print("Error: Categoría no válida.")

        elif opcion == '2':
            print("\n--- Inventario Completo ---")
            for nombre, info in inventario.items():
                print(f"Producto: {nombre} | Precio: ${info['precio']} | Stock: {info['stock']} | Cat: {info['categoria']}")

        elif opcion == '3':
            busqueda = input("Categoría a buscar: ").capitalize()
            print(f"\nProductos en {busqueda}:")
            encontrado = False
            for nombre, info in inventario.items():
                if info['categoria'] == busqueda:
                    print(f"- {nombre}")
                    encontrado = True
            if not encontrado: print("No hay productos en esta categoría.")

        elif opcion == '4':
            print(f"\nMarcas registradas (sin repetir): {marcas_unicas}")

        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
menu()