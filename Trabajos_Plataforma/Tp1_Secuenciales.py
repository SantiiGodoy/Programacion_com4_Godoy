#ej1===
print("Hola mundo!") 


#ej2===
nombre = input("Como es su nombre?")
print(f"Hola {nombre}!")


#ej3===
nombre_apellido = input("Digite su nombre completo:")
edad = input ("Ingrese su edad:")
lugar = input("Digite lugar de residencia:")

print(f"Soy {nombre_apellido}, tengo {edad} y soy de {lugar}")


#ej4===
radio = float(input("Ingrese el radio que desea calcular:"))
PI = 3.14
area = PI * radio**2
perimetro = 2 * PI * radio

print(f"El area de {radio} es {area} y su perimetro es {perimetro} ")


#ej5===
segundos_usuario = int(input("Ingrese segundos para ver su equivalencia en horas:"))
hora = segundos_usuario / 3600
print(f"{segundos_usuario} segundos equivalen a {hora} horas")


#ej6===
numero_ingresado = int(input("Ingresar un numero para sacar su tabla de multiplicar:"))
print(f"Tabla de multiplicar del {numero_ingresado}")
i = 1
while i <= 10:
    print(f"{numero_ingresado} x {i} = {numero_ingresado * i}")
    i += 1


#ej7===
print("")
print("")

print("Ingrese dos numeros enteros (distintos a 0):")
numero1 = int(input("Digite el primer numero:"))
numero2 = int(input("Digite el segundo numero:"))

suma = numero1 + numero2
resta = numero1 - numero2
div = numero1 / numero2
multip = numero1 * numero2

print("===SUMA===")

print(f"{numero1} + {numero2} = {suma}")

print("===RESTA===")
print(f"{numero1} - {numero2} = {resta}")

print("===DIVISION===")
print(f"{numero1} / {numero2} = {div}")

print("===MULTIPLICACION===")
print(f"{numero1} x {numero2} = {multip}")


#ej8===
print("")

print("===INDICE DE MASA CORPORAL===")
peso = float(input("Ingrese su pesaje:"))
altura = float(input("Ingrese su altura:"))
masa = peso / (altura * altura)

print(f"El indice de masa corporal es", round(masa, 2))


#ej9===
celsius = float(input("Digite la temperatura en grados Celsius:"))
fahrenheit = (celsius * 9/5) + 32

print("La temperatura en Fahrenheit es", fahrenheit)


#ej10===
print("")

print("===SACAR PROMEDIO===")

numero1 = float(input("Ingresa el primer numero:"))
numero2 = float(input("Ingresa el segundo numero:"))
numero3 = float(input("Ingresa el tercer numero:"))

promedio = (numero1 + numero2 + numero3 ) / 3

print ("Da como promedio:", promedio)