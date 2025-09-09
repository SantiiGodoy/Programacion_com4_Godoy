#Ejercicio 1 
print("==Ejercicio 1==")
print("")
for num in range(0, 101):
    print(num)

#Ejercicio 2
print("")
print("==Ejercicio 2==")
print("")
numero_ent = input("Ingresa un número entero:")
print(len(numero_ent))

#Ejercicio 3
print("")
print("==Ejercicio 3==")
print("")
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor "))
menor = min(valor1, valor2)
mayor = max(valor1, valor2)
suma = 0
for i in range(valor1, valor2):
    suma += i

print(f"La suma de los números entre {valor1} y {valor2}, sin contar ambos, es: {suma}")

#Ejercicio 4
print("")
print("==Ejercicio 4==")
print("")
suma = 0
print("Ingresa números enteros para sumarlos. 0 para finalizar: ")
while True:
    nums = int(input("Ingrese números: "))
    if nums == 0:
        break 
    suma += num

print(f"La suma total de los números es: {sum}")

#Ejercicio 5
print("")
print("==Ejercicio 5==")
print("")
import random
numero_aleatorio = random.randint(0,9)
intentos = 0
adivino = False
while not adivino:
    try:
        num_usu = int(input("Ingrese su número: "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        continue
    intentos += 1
    if num_usu == numero_aleatorio:
        adivino = True
    else:
        print("No es correcto, intenta nuevamente. ")

print(f"Adivinaste el número aleatorio: {numero_aleatorio} ")

#Ejercicio 6
print("")
print("==Ejercicio 6==")
for i in range(99, -1, -2):
    print(i)

#Ejercicio 7 
print("")
print("==Ejercicio 7==")
print("")

suma = 0
numero_ingr = int(input("Ingrese un número:"))
for i in range(0, numero_ingr+1):
    suma += (i)

print(f"La suma comprendida entre 0 y {numero_ingr} es :{suma}")

#Ejercicio 8
print("")
num_pares = 0
num_impares = 0
num_negativos = 0
num_postivos = 0
totalnumeros = 100

print(f"Ingrese {totalnumeros} números enteros: ")
for i in range(totalnumeros):
    numeros = int(input(f"Número {i+1}:"))
    if numeros % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    if numeros > 0:
        num_postivos += 1
    elif numeros < 0:
        num_negativos += 1

print(f"Números pares: {num_pares}")
print(f"Números impares: {num_impares}")
print(f"Numeros negativos: {num_negativos}")
print(f"Números positivos: {num_postivos}")

#Ejercicio 9
print("")
print("==Ejercicio 9==")
import statistics
totalnumeros = 3
numeros = []

for i in range(totalnumeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

media = statistics.mean(numeros)
print(f"La media es:", round(media,2))

#Ejercicio 10
print("")
print("==Ejercicio 10==")
print("")

numero = input("Ingresa un número: ")
invertir = ""

for i in range (len(numero)-1, -1, -1):
    invertir += numero [i]
print(f"El número invertido queda: {invertir}")




