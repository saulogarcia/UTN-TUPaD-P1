# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def hola_mundo():
    print("Hola Mundo!")

hola_mundo()

print()
print("--------------------------------")
print()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario('Marcos')

print()
print("--------------------------------")
print()

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal("Juan", "Perez", 25, "Argentina")

print()
print("--------------------------------")
print()

# 4. Crear dos funciones:
# calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return 3.14 * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingrese el radio: "))

print(f"El area del circulo es {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es {calcular_perimetro_circulo(radio)}")

print()
print("--------------------------------")
print()

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese el numero de segundos: "))
print(f"El numero de horas es {segundos_a_horas(segundos)}")

print()
print("--------------------------------")
print()

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

print()
print("--------------------------------")
print()

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos.
# Mostrar los resultados de forma clara.

# tupla en pyhton = (a, b, c, d)

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
resultados = operaciones_basicas(a, b)
print(f"{a} + {b} = {resultados[0]}")  # accedo a la tupla usando el indice
print(f"{a} - {b} = {resultados[1]}")
print(f"{a} * {b} = {resultados[2]}")
print(f"{a} / {b} = {resultados[3]}")

print()
print("--------------------------------")
print()

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.

# Nota: el IMC es el peso medido en kg dividido entre la altura en metros.

# Composición corporal	Índice de masa corporal (IMC)
# Peso inferior al normal	Menos de 18.5
# Normal	18.5 – 24.9
# Peso superior al normal	25.0 – 29.9
# Obesidad	Más de 30.0

def calcular_imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
print(f"El IMC es {calcular_imc(peso, altura):.2f}")

print()
print("--------------------------------")
print()

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"La temperatura en Fahrenheit es {celsius_a_fahrenheit(celsius):.2f}")

print()
print("--------------------------------")
print()

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
print(f"El promedio es {calcular_promedio(a, b, c)}")


