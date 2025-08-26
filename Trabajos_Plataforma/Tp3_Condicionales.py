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
    print("Usted es un niño.")
elif edad >= 12 and edad < 18:
    print("Usted es adolecente.")

