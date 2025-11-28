import os
nombre_archivo = "productos.txt"
mis_productos = [
    "Mouse,150.50,100",
    "Fuente,1085.00,50",
    "Monitor,12000.00,20"
]
productos_lista_diccionarios = []

# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantida

def crear_archivo(nombre_archivo, mis_productos):
    if os.path.exists(nombre_archivo):
        print("El archivo ya existe.")
    else:
        with open(nombre_archivo, "w") as archivo:
            for producto in mis_productos:
                archivo.write(producto + "\n")
        print("El archivo ha sido creado exitosamente.")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

def leer_mostrar_productos(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            producto = linea.strip().split(",")
            print(f"Producto: {producto[0]:>10} | Precio: {producto[1]:>10} | Cantidad: {producto[2]:>5}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

def cargar_nuevo_producto(productos_lista_diccionarios, nombre_archivo):
    nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
    nuevo_precio = float(input("Ingrese el precio del nuevo producto: "))
    nuevo_cantidad = int(input("Ingrese la cantidad del nuevo producto: "))
    # agregar el nuevo producto a la lista
    productos_lista_diccionarios.append({"nombre": nuevo_producto, "precio": nuevo_precio, "cantidad": nuevo_cantidad})
    # guardar el nuevo producto en el archivo
    with open(nombre_archivo, "a") as archivo:
        archivo.write(f"{nuevo_producto},{nuevo_precio},{nuevo_cantidad}\n")
    print(f"Producto {nuevo_producto} agregado exitosamente.")
    return productos_lista_diccionarios


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

def cargar_productos_en_lista(nombre_archivo, productos_lista_diccionarios):
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            producto = linea.strip().split(",")
            productos_lista_diccionarios.append({"nombre": producto[0], "precio": producto[1], "cantidad": producto[2]})
    return productos_lista_diccionarios

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

def buscar_producto(productos_lista_diccionarios):
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
    for producto in productos_lista_diccionarios:
        if producto["nombre"] == nombre_producto:
            print(producto)
            break
    else:
        print("Producto no encontrado.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

def guardar_productos_actualizados(nombre_archivo, productos_lista_diccionarios):
    with open(nombre_archivo, "w") as archivo:
        for producto in productos_lista_diccionarios:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Productos actualizados guardados exitosamente.")


# Menu de opciones
def menu():
    while True:
        print("")
        print("1. Crear archivo inicial con productos")
        print("2. Leer y mostrar productos")
        print("3. Agregar productos desde teclado")
        print("4. Cargar productos en una lista de diccionarios")
        print("5. Buscar producto por nombre")
        print("6. Guardar los productos actualizados")
        print("7. Salir")
        opcion = int(input("Ingrese el numero de la opcion: "))
        match opcion:
            case 1:
                crear_archivo(nombre_archivo, mis_productos)
                productos_lista_diccionarios = cargar_productos_en_lista(nombre_archivo, productos_lista_diccionarios)
            case 2:
                leer_mostrar_productos(nombre_archivo)
            case 3:
                productos_lista_diccionarios = cargar_nuevo_producto(productos_lista_diccionarios, nombre_archivo)
            case 4:
                productos_lista_diccionarios = cargar_productos_en_lista(nombre_archivo, productos_lista_diccionarios)
                print(productos_lista_diccionarios)
            case 5:
                if len(productos_lista_diccionarios) == 0:
                    print("Primero debe cargar productos en una lista de diccionarios.")
                else:
                    buscar_producto(productos_lista_diccionarios)
            case 6:
                guardar_productos_actualizados(nombre_archivo, productos_lista_diccionarios)
            case 7:
                print("Adios")
                break
            case _:
                print("Opcion no valida.")

menu()
