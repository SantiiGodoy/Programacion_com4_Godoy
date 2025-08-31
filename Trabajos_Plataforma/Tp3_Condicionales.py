#ej1====
print("==Ejercicio 1==")
edad_usuario = int(input("Digite su edad: "))

if edad_usuario >= 18:
    print("Usted es mayor de edad ")
else:
    print("Usted es menor de edad ")
print("")

#ej2====
print("==Ejercicio 2==")
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado ")
else:
    print("Desaprobado")
print("")

#ej3====
print("==Ejercicio 3==")
numero = int(input("Ingrese un numero para saber si es PAR o IMPAR: "))
if numero % 2 == 0:
    print("El numero ingresado es PAR! ")
else:
    print("El numero ingresado es IMPAR! ")
print("")

#ej4====
print("==Ejercicio 4==")
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Eres un niño/a")
elif edad >= 12 and edad < 18:
    print("Eres adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un adulto/a joven")
elif edad >= 30:
    print ("Eres un adulto/a")
print("")

#ej5====
while True:
    texto = input("Ingrese una clave (entre 8 y 14 caracteres:)")

    if 8<= len(texto)<= 14:
        print("Su clave fue exitosamente registrada")
        break
    else: 
        print("Clave inválida, porfavor intente de nuevo:")
print("")

#ej6====
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

from statistics import mean, median, mode, multimode

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

moda = multimode(numeros_aleatorios)[0]
print(f"La media es: {media}\nLa mediana es: {mediana}\n La moda es: {moda}")
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
else:
    print("No hay sesgo")
print("")

#ej7====
palabra = input("Ingrese una frase o palabra: ")
if palabra[-1].lower() in "aeiou":
    print(palabra,"!")
else:
    print(f"La palabra/frase ingresada es:", palabra)
print("")

#ej8====
print("")
nombre_usu = input("Ingrese su nombre:")
numero_seleccionado = int(input("Ingrese el numero 1, 2 o 3:\n1: Si queres tu nombre en mayúsculas\n2: Si queres tu nombre en minúsculas\n3: Si queres solo la primer letra en mayúsculas\nElección de numero: "))

if numero_seleccionado == 1:
    print(nombre_usu.upper())
elif numero_seleccionado == 2:
    print(nombre_usu.lower())
elif numero_seleccionado == 3:
    print(nombre_usu.title())
elif numero_seleccionado >=3:
    print("Numero no válido")
print("")

#ej9====
print("")
magnitud = int(input("Ingrese la magnitud de un terremoto(1 al 7): "))
if magnitud < 3:
    print("Muy leve (imperceptible) ")
elif magnitud >= 3 and magnitud < 4:
    print("Leve(ligeramente perceptible) ")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte(puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte(puede causar daños significativos) ")
elif magnitud >= 7:
    print("Extremo(puede causar graves daños a gran escala)")
else:
    print("Número no válido.")
print("")

#ej10====
hemisferio_usuario = input("Ingrese a que hemisferio pertenece (N o S): ").upper()
mes_usuario = int(input("Ingrese en que mes se encuentra(1-12): "))
dia_usario = int(input("Ingrese día(1-31)"))

if (mes_usuario == 12 and dia_usario >= 21) or (1 <= mes_usuario <= 2) or (mes_usuario == 3 and dia_usario <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif(mes_usuario == 3 and dia_usario >= 21 ) or (4 <= mes_usuario <= 5) or (mes_usuario == 6 and dia_usario <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif(mes_usuario == 6 and dia_usario >= 21 ) or (7 <= mes_usuario <= 8) or (mes_usuario == 9 and dia_usario <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif(mes_usuario == 9 and dia_usario >= 21 ) or (10 <= mes_usuario <= 11) or (mes_usuario == 12 and dia_usario <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    print("Formato invalido")

if hemisferio_usuario == "N":
    print ("El hemisferio en el que te encuentras es:",estacion_norte)
elif hemisferio_usuario == "S":
    print("El hemisferio en el que te encuentras es:", estacion_sur)
else:
    print("Hemisferio invalido.")
