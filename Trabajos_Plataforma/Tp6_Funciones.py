#===================================================================================================
#Ejercicio 1
print("==Ejercicio 1==")
print("")

def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()

#Ejercicio 2
print("==Ejercicio 2==")
print("")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#Codigo principal:
nombre = input("Ingrese su nombre:").capitalize()
saludar_usuario(nombre)

#Ejercicio 3
print("==Ejercicio 3==")
print("")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Codigo principal:
nombre = input("Ingrese su nombre:").capitalize()
apellido = input("Ingrese su apellido:").capitalize()
edad = int(input("Ingrese su edad:"))
residencia = input("Ingrese dónde vive:").capitalize()

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
print("==Ejercicio 4==")
print("")

import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

#Codigo principal:
radio = float(input("Ingrese un radio para sacar área:"))
radio = float(input("Ingrese un radio para sacar el perímetro:"))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del del circulo es: {round(area, 2)}")
print(f"El perímetro del círculo con un radio de {radio} es: {round(perimetro, 2)}")

#Ejercicio 5
print("==Ejercicio 5==")
print("")

def segundos_a_horas(segundos):
    horas = segundos / 3600
    resto = segundos % 3600
    minutos = resto // 60
    seg_restantes = resto % 60
    print(f"Segundos recibidos: {segundos}, equivalen a {horas} hs {minutos}min y {seg_restantes}seg.")

#Codigo principal:
segundos = int(input("Ingrese segundos:"))
segundos_a_horas(segundos)

#Ejercicio 6
print("==Ejercicio 6==")
print("")

def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero * i}")

#Codigo principal:

numero_tabla = int(input("Ingrese el número para mostrar su tabla:"))
tabla_multiplicar(numero_tabla)

#Ejercicio 7
print("==Ejercicio 7==")
print("")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multip = a * b
    div = a / b
    print(f"Suma de {a} + {b} = {suma}")
    print(f"Resta de {a} - {b} = {resta}")
    print(f"Multiplicación de {a} x {b} = {multip}")

    if b != 0:
        div = a / b
        print(f"División de {a} : {b} = {div}")
    else:
        print("No se puede dividir entre 0!")

#Codigo principal:

print("Ingrese 2 números")
num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))
operaciones_basicas(num1,num2)

#Ejercicio 8
print("==Ejercicio 8==")
print("")

def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc

#Codigo principal:
print("==Sacar IMC:==")
peso = float(input("Ingrese su peso en Kg:"))
altura = float(input("Ingrese su altura en metros:"))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {round(imc, 2)}")

#Ejercicio 9
print("==Ejercicio 9==")
print("")

def celsius_a_fahrenheit(celsius):
    calculo = (temp * 1.8) + 32
    return calculo

#Codigo principal:
print("==Temperatura en Celsius a Fahrenheit==")
temp = float(input("Ingrese temperatura en Celsius:"))
calculo = celsius_a_fahrenheit(temp)
print(f"{temp}°C a Farhengeit es {calculo}°F")

#Ejercicio 10
print("==Ejercicio 10==")
print("")

import statistics

def calcular_promedio(a,b,c):
    promedio = statistics.mean[a,b,c]
    return promedio

#Codigo principal:
print("Ingrese 3 notas para sacar promedio:")
num1 = int(input("Ingrese la primer nota:"))
num2 = int(input("Ingrese la segunda nota:"))
num3 = int(input("Ingrese la tercer nota"))
promedio = calcular_promedio(num1,num2,num3)
print(f"El promedio de las notas es: {promedio}")

#===================================================================================================