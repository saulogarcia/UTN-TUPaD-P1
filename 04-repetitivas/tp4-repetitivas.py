# TP 4 - Repetitivas

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

print("--------------------------------")
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
print("--------------------------------")
print("Ejercicio 2 ")
print("--------------------------------")

numero = int(input("Ingrese un numero entero: "))
cantidad_digitos = 0
while numero > 0:
    numero = numero // 10
    cantidad_digitos += 1

print(f"El numero tiene {cantidad_digitos} digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
print("--------------------------------")
print("Ejercicio 3 ")
print("--------------------------------")

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(primer_numero , segundo_numero + 1 ):
    suma += i

print(f"La suma de los numeros entre {primer_numero} y {segundo_numero} es {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
print("--------------------------------")
print("Ejercicio 4 ")
print("--------------------------------")

suma = 0
numero = int(input("Ingrese un numero: "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un numero: "))

print(f"La suma de los numeros ingresados es {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("--------------------------------")
print("Ejercicio 5 ")
print("--------------------------------")

import random

numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    numero = int(input("Ingrese un numero: "))
    intentos += 1
    if numero == numero_aleatorio:
        print(f"Acertaste el numero en {intentos} intentos")
        break


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.
print("--------------------------------")
print("Ejercicio 6 ")
print("--------------------------------")


for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
print("--------------------------------")
print("Ejercicio 7 ")
print("--------------------------------")

numero = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(numero + 1):
    suma += i

print(f"La suma de los numeros entre 0 y {numero} es {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("--------------------------------")
print("Ejercicio 8 ")
print("--------------------------------")


numeros_pares = 0
numeros_impares = 0
numeros_negativos = 0
numeros_positivos = 0

for i in range(100):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    if numero < 0:
        numeros_negativos += 1
    else:
        numeros_positivos += 1

print(f"Hay {numeros_pares} numeros pares")
print(f"Hay {numeros_impares} numeros impares")
print(f"Hay {numeros_negativos} numeros negativos")
print(f"Hay {numeros_positivos} numeros positivos")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor)
print("--------------------------------")
print("Ejercicio 9 ")
print("--------------------------------")

numeros = 0
for i in range(100):
    numeros += int(input("Ingrese un numero: "))

print(f"La media de los numeros ingresados es {numeros / 100}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745
print("--------------------------------")
print("Ejercicio 10 ")
print("--------------------------------")

numero = int(input("Ingrese un numero: "))
numero_invertido = 0
while numero > 0:
    numero_invertido = numero_invertido * 10 + numero % 10
    numero = numero // 10

print(numero_invertido)