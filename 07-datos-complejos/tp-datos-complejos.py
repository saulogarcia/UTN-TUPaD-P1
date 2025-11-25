# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print("Ejercicio 1")
# chequeo
for clave, valor in precios_frutas.items():
    print(f"{clave}: {valor}")

print("---" * 10)
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("Ejercicio 2")
# chequeo
for clave, valor in precios_frutas.items():
    print(f"{clave}: {valor}")

print("---" * 10)
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios

precios = list(precios_frutas.keys())
print(precios)

print("---" * 10)
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}


def cargar_contactos(contactos):
    numero_contactos = 5

    # cargar los contactos
    for i in range(numero_contactos):
        nombre = input(f"Ingrese el nombre del contacto numero {i + 1}: ")
        numero = input(f"Ingrese el numero del contacto numero {i + 1}: ")
        contactos[nombre] = numero


# consultar contacto
def consultar_contactos(contactos):
    nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ")

    # mostrar el numero asociado si existe
    if nombre_consulta in contactos:
        print(f"El numero de {nombre_consulta} es {contactos[nombre_consulta]}")
    else:
        print(f"No existe el contacto {nombre_consulta}")


def menu_ejercicio_cuatro():
    while True:
        print("")
        print("---")
        print("Ejercicio 4")
        print("MENU")
        print("---")
        print("1. Cargar contactos 5 contactos")
        print("2. Consultar contacto")
        print("3. Salir")
        opcion = int(input("Elija una opción: ").strip())
        match opcion:
            case 1:
                cargar_contactos(contactos)
            case 2:
                consultar_contactos(contactos)
            case 3:
                print("Adios")
                break
            case _:
                print("Opcion no valida")


menu_ejercicio_cuatro()


print("---" * 10)
# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

print("Ejercicio 5")

palabras = input("Ingrese una frase: ").split()

palabras_unicas = set(palabras)

recuento_palabras = {}
for palabra in palabras:
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

print(f"palabras unicas: {palabras_unicas}")
print(f"recuento palabras: {recuento_palabras}")

print("---" * 10)
print("Ejercicio 6")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno numero {i + 1}: ")
    print(f"Ingrese las notas de {nombre} separadas por espacios:")
    print("Ejemplo: 4 5 6")
    n1, n2, n3 = input().split()
    alumnos[nombre] = (int(n1), int(n2), int(n3))

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio}")

print("---" * 10)
print("Ejercicio 7")
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {103, 104, 105, 106, 107}

print(f"Aprobaron Parcial 1: {parcial_1}")
print(f"Aprobaron Parcial 2: {parcial_2}")

# Aprobaron ambos (Interseccion)
ambos = parcial_1 & parcial_2
print(f"Aprobaron ambos: {ambos}")

# Aprobaron solo uno (Diferencia simetrica)
solo_uno = parcial_1 ^ parcial_2
print(f"Aprobaron solo uno: {solo_uno}")

# Aprobaron al menos uno (Union)
al_menos_uno = parcial_1 | parcial_2
print(f"Aprobaron al menos uno: {al_menos_uno}")

print("---" * 10)
print("Ejercicio 8")
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock_productos = {"manzanas": 50, "peras": 30, "naranjas": 40}

def menu_stock():
    while True:
        print("")
        print("--- GESTION DE STOCK ---")
        print("1. Consultar stock")
        print("2. Agregar stock / Nuevo producto")
        print("3. Salir") 
        opcion = int(input("Elija una opcion: ").strip())
        match opcion:
            case 1:
                producto = input("Ingrese el nombre del producto: ").lower()
                if producto in stock_productos:
                    print(f"El stock de {producto} es: {stock_productos[producto]}")
                else:
                    print(f"El producto {producto} no existe.")
            case 2:
                producto = input("Ingrese el nombre del producto: ").lower()
                cantidad = int(input("Ingrese la cantidad a agregar: ").strip())
                if producto in stock_productos:
                    stock_productos[producto] += cantidad
                    print(f"Se agregaron {cantidad} unidades a {producto}. Nuevo stock: {stock_productos[producto]}")
                else:
                    stock_productos[producto] = cantidad
                    print(f"Producto {producto} agregado con stock inicial de {cantidad}.")
            case 3:
                print("Adios")
                break
            case _:
                print("Opcion no valida.")

menu_stock()

print("---" * 10)
print("Ejercicio 9")
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:00"): "Meeting",
    ("martes", "14:00"): "Almuerzo con cliente",
    ("viernes", "18:00"): "Happy Hour"
}

print("Consulta de Agenda")
dia = input("Ingrese el dia (ej. lunes): ").lower()
hora = input("Ingrese la hora (ej. 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Evento programado: {agenda[clave]}")
else:
    print("No hay eventos programados para ese día y hora.")

print("---" * 10)
print("Ejercicio 10")
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Chile": "Santiago"
}

print(f"Diccionario original: {paises_capitales}")

# Invertir el diccionario usando dictionary comprehension
capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(f"Diccionario invertido: {capitales_paises}")

