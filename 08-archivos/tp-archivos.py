import os
nombre_archivo = "productos.txt"
mis_productos_iniciales = [
    {"nombre": "Mouse", "precio": 150.50, "cantidad": 100},
    {"nombre": "Fuente", "precio": 1085.00, "cantidad": 50},
    {"nombre": "Monitor", "precio": 12000.00, "cantidad": 20}
]
mis_productos = []

# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantida

def crear_archivo(nombre_archivo, mis_productos):
    if os.path.exists(nombre_archivo):
        print("El archivo ya existe.")
    else:
        with open(nombre_archivo, "w") as archivo:
            for producto in mis_productos:
                archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
        print("El archivo ha sido creado exitosamente.")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

def leer_mostrar_productos(nombre_archivo, mis_productos):
    mis_productos.clear()
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            producto = linea.strip().split(",")
            # agregar el producto a la lista diccionario
            mis_productos.append({"nombre": producto[0], "precio": producto[1], "cantidad": producto[2]})
            print(f"Producto: {producto[0]:>10} | Precio: {producto[1]:>10} | Cantidad: {producto[2]:>5}")
    print("---" * 20)
    print("")
    return mis_productos

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

def cargar_nuevo_producto(mis_productos, nombre_archivo):
    nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
    nuevo_precio = float(input("Ingrese el precio del nuevo producto: "))
    nuevo_cantidad = int(input("Ingrese la cantidad del nuevo producto: "))
    # agregar el nuevo producto a la lista
    mis_productos.append({"nombre": nuevo_producto, "precio": nuevo_precio, "cantidad": nuevo_cantidad})
    # guardar el nuevo producto en el archivo
    with open(nombre_archivo, "a") as archivo:
        archivo.write(f"{nuevo_producto},{nuevo_precio},{nuevo_cantidad}\n")
    print(f"Producto {nuevo_producto} agregado exitosamente.")


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

# resuelto en el punto 2

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

def buscar_producto(mis_productos):
    nombre_producto = input("Ingrese el nombre del producto a buscar: ").lower().strip()
    for producto in mis_productos:
        if producto["nombre"].lower() == nombre_producto:
            print(f"Producto encontrado: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
            break
    else:
        print("Producto no encontrado.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

def guardar_productos_actualizados(nombre_archivo, mis_productos):
    with open(nombre_archivo, "w") as archivo:
        for producto in mis_productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Productos actualizados guardados exitosamente.")


# Menu de opciones
def menu():
    while True:
        print("")
        print("---" * 20)
        print("MENU")
        print("---" * 20)
        print("1. Crear archivo inicial con productos")
        print("2. Leer y mostrar productos (Cargar productos en una lista de diccionarios)")
        print("3. Mostrar y agregar productos desde teclado")
        print("4. Buscar producto por nombre")
        print("5. Guardar los productos en el archivo desde la lista de diccionarios")
        print("6. Salir")
        print("")
        opcion = int(input("Ingrese el numero de la opcion: "))
        print("---" * 20)
        match opcion:
            case 1:
                crear_archivo(nombre_archivo, mis_productos_iniciales)
            case 2:
                leer_mostrar_productos(nombre_archivo,mis_productos)
            case 3:
                cargar_nuevo_producto(leer_mostrar_productos(nombre_archivo,mis_productos), nombre_archivo)
            case 4:
                buscar_producto(mis_productos)
            case 5:
                guardar_productos_actualizados(nombre_archivo, mis_productos)
            case 6:
                print("Adios")
                break
            case _:
                print("Opcion no valida.")

menu()
