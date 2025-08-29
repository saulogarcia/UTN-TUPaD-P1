# Alumno: Saulo Garcia
# Comision:5 Ag25-1C-05
# TP1

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("ejercicio 1\n")
print("Hola mundo\n")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
print("ejercicio 2\n")
nombre = input("Ingrese el nombre:")
print(f"Hola {nombre}\n")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
print("ejercicio 3\n")
nombre = input("Ingrese el Nombre: ")
apellido = input("Ingrese el Apellido: ")
edad = input("Ingrese el Edad: ")
residencia = input("Ingrese el lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}\n")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
print("ejercicio 4\n")
radio_circulo = float(input("Ingrese el radio del circulo: "))
area = 3.14 * radio_circulo ** 2
perimetro = 3.14 * radio_circulo * 2
print(f"El area del circulo es {area} y el perimetro es {perimetro}\n")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale
print("ejercicio 5\n")
segundos = int(input("ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"La cantidad de segundos ingresados representa {horas} horas\n")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
print("ejercicio 6\n")
numero = int(input("Ingrese un numero: "))
print(f"La tabla de multiplicar del numero {numero} es:")
print(1 * numero)
print(2 * numero)
print(3 * numero)
print(4 * numero)
print(5 * numero)
print(6 * numero)
print(7 * numero)
print(8 * numero)
print(9 * numero)
print(10 * numero)


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("ejercicio 7\n")
primer_numero = int(input("Ingrese un primer numero entero: "))
segundo_numero = int(input("Ingrese un segundo numero entero: "))
print(f"La suma entre los dos numeros es {primer_numero + segundo_numero}")
print(f"La resta entre los dos numeros es {primer_numero - segundo_numero}")
print(f"La multiplicacion entre los dos numeros es {primer_numero * segundo_numero}")
if segundo_numero == 0:
  print("No es valido dividir por cero")
else:
  print(f"La division entre los dos numeros es {primer_numero / segundo_numero}\n")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
print("ejercicio 8\n")
altura = float(input("Ingrese su altura:"))
peso = float(input("Ingrese su peso:"))
imc = peso / altura ** 2
print(f"Su indice de masa corporal es: {imc}\n")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
print("ejercicio 9\n")
celsius = float(input("Ingrese la temperatura en grados celsius: "))
print(f"La temperatura en grados fahrenheit es {celsius * (9/5) + 32}\n")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
print("ejercicio 10\n")
primer_numero = float(input("Ingrese un primer numero: "))
segundo_numero = float(input("Ingrese un segundo numero: "))
tercer_numero = float(input("Ingrese un tercer numero: "))
print(f"El promedio de los numero ingresados es { (primer_numero + segundo_numero+ tercer_numero)/3} \n")