# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.
print("--------------------------------")
print("Ejercicio 1 ")
print("--------------------------------")

notas = [2,8,7,9,6,5,4,3,2,10]

max_nota = 0 # se inicializa con el valor minimo de la nota
min_nota = 10 # se inicializa con el valor maximo de la nota

for nota in notas:
    if nota > max_nota:
        max_nota = nota
    if nota < min_nota:
        min_nota = nota

print(notas)
print(f"El promedio de las notas es {sum(notas) / 10}")
print(f"La nota mas alta es {max_nota}")
print(f"La nota mas baja es {min_nota}")

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
print("--------------------------------")
print("Ejercicio 2 ")
print("--------------------------------")

productos = []
for i in range(5):
    productos.append(input("Ingrese el producto: "))

print(sorted(productos))

producto_eliminar = input("Ingrese el producto que desea eliminar: ")
productos.remove(producto_eliminar)
print(sorted(productos))

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.
print("--------------------------------")
print("Ejercicio 3 ")
print("--------------------------------")

import random

numeros = [random.randint(1, 100) for i in range(15)]
print(numeros)

numeros_pares = []
numeros_impares = []

for indice in range(15):
    numero = numeros[indice]
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f"La cantidad de numeros pares es {len(numeros_pares)}")
print(f"La cantidad de numeros impares es {len(numeros_impares)}")
print(f"La lista de numeros pares es {numeros_pares}")
print(f"La lista de numeros impares es {numeros_impares}")

# 4) Dada una lista con valores repetidos:
# [1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
print("--------------------------------")
print("Ejercicio 4 ")
print("--------------------------------")

lista = [1,3,5,3,7,1,9,5,3]
lista_sin_repetidos = list(set(lista)) # set() es una funcion que elimina los elementos repetidos de la lista
print(lista_sin_repetidos)

# alternativa
lista_sin_repetidos = []
for i in range(len(lista)):
    if lista[i] not in lista_sin_repetidos:
        lista_sin_repetidos.append(lista[i])
print(lista_sin_repetidos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
print("--------------------------------")
print("Ejercicio 5 ")
print("--------------------------------")

estudiantes = ["Juan", "Luciano", "Santiago", "Martin", "Diego", "Pedro", "Jose", "Maria"]
print(estudiantes)

print("Opciones:")
print("1. Agregar un nuevo estudiante")
print("2. Eliminar un estudiante existente")
opcion = input("Ingrese el numero de la opcion: ")
if opcion == "1":
    estudiantes.append(input("Ingrese el nombre del estudiante: "))
elif opcion == "2":
    estudiantes.remove(input("Ingrese el nombre del estudiante: "))
print(estudiantes)

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero)
print("--------------------------------")
print("Ejercicio 6 ")
print("--------------------------------")

numeros = [1,2,3,4,5,6,7]
aux = numeros[0]
for i in range(len(numeros) - 1):
    numeros[i] = numeros[i + 1]

numeros[len(numeros) - 1] = aux
print(numeros)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.
print("--------------------------------")
print("Ejercicio 7 ")
print("--------------------------------")
# [2,4,3,8,10,12,14] minimas
# [18,22,25,40,29,21,30] maximas

matriz = [
    [2,4,3,8,10,12,14],
    [18,22,25,40,29,21,30]
    ]

print(f"El promedio de las temperaturas minimas es {sum(matriz[0]) / 7}")
print(f"El promedio de las temperaturas maximas es {sum(matriz[1]) / 7}")

amplitud = 0
for i in range(len(matriz[0])):
    if matriz[1][i] - matriz[0][i] > amplitud:
        amplitud = matriz[1][i] - matriz[0][i]
        dia_max_amplitud = i + 1

print(f"El dia con la mayor amplitud térmica es {dia_max_amplitud}")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

print("--------------------------------")
print("Ejercicio 8 ")
print("--------------------------------")

matriz = [
    [10,7,9,4,6],
    [10,3,8,7,5],
    [10,8,5,9,10]
]
# promedio de cada estudiante
for i in range(len(matriz)):
    print(f"El promedio de las notas del estudiante {i + 1} es {sum(matriz[i]) / 5}")

# promedio de cada materia
for i in range(len(matriz[0])):
    suma = 0
    for j in range(len(matriz)):
        suma += matriz[j][i]
    print(f"El promedio de las notas de la materia {i + 1} es {suma / 3}")

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
print("--------------------------------")
print("Ejercicio 9 ")
print("--------------------------------")

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

for fila in range(3):
    for columna in range(3):
        print(tablero[fila][columna], end=" ")
    print()

jugador = 1
# observarcion utilizo while true para hacer uso de la sentencia break en lugar de una bandera
while True:
    print("--------------------------------")
    print(f"Jugador {jugador}")
    print("--------------------------------")
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    if jugador == 1:
        tablero[fila-1][columna-1] = "X"
        jugador = 2
    else:
        tablero[fila-1][columna-1] = "O"
        jugador = 1
    print(tablero)
    print("--------------------------------")
    print("Tablero actualizado")
    for fila in range(3):
        for columna in range(3):
            print(tablero[fila][columna], end=" ")
        print()

    salir = input("¿Desea salir? (s/n): ")
    if salir == "s":
        break # salir del bucle while


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana

print("--------------------------------")
print("Ejercicio 10 ")
print("--------------------------------")

matriz = [
    [1,2,3,8,5,6,7],
    [8,9,20,9,1,3,4],
    [5,6,80,1,9,2,3],
    [2,3,400,5,6,3,8]
]

# total vendido por cada producto
for producto in range(len(matriz)):
    suma = 0
    for dia in range(len(matriz[0])):
        suma += matriz[producto][dia]
    print(f"El total vendido por el producto {producto + 1} es {suma}")


print()
# dia con mayores ventas totales
venta_max_dia = 0
dia_max_venta = 0

for dia in range(len(matriz[0])):
    suma = 0
    for producto in range(len(matriz)):
        suma += matriz[producto][dia]
    if suma > venta_max_dia:
        venta_max_dia = suma
        dia_max_venta = dia

# se suma 1 porque el rango de los dias es de 0 a 6
print(f"El dia con mayores ventas totales es {dia_max_venta+1} se vendieron {venta_max_dia} unidades de productos")

print()
# producto mas vendido en la semana
venta_max_producto = 0
producto_max_venta = 0
for producto in range(len(matriz)):
    suma = 0
    for dia in range(len(matriz[0])):
        suma += matriz[producto][dia]
    if suma > venta_max_producto:
        venta_max_producto = suma
        producto_max_venta = producto

# se suma 1 porque el rango de los productos es de 0 a 3
print(f"El producto mas vendido en la semana es el {producto_max_venta+1} se vendieron {venta_max_producto} unidades de productos")