
#Ejercicio 1
print("==Ejercicio 1==")
print("")

for numeros_lista in range(1, 101):
    if numeros_lista % 4 == 0:
        print(numeros_lista)

#Ejercicio 2
print("")
print("==Ejercicio 2==")
print("")
lista = [1, 2, 3, 4, 5]
print (lista)
print("Penúltimo valor de la lista:", lista[-2])

#Ejercicio 3
print("")
print("==Ejercicio 3==")
print("")

lista_vacia = []
lista_vacia.append("manzana")
lista_vacia.append("pera")
lista_vacia.append("banana")
print(lista_vacia)

#Ejercicio 4
print("")
print("==Ejercicio 4==")
print("")

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

#Ejercicio 5 
print("")
print("==Ejercicio 5==")
print("")

#ANALIZAR EL SIGUIENTE PROGRAMA:
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros) #Lo que pasa en este ejercicio es que el .remove(max(numeros)) hace que saque de la lista el número mayor, en este caso el 22.

#Ejercicio 6
print("")
print("==Ejercicio 6==")
print("")

nums = list(range(10,31,5))
print (nums)
print("Primeros dos números:", nums[:2])

#Ejercicio 7
print("")
print("==Ejercicio 7==")
print("")

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "mercedes"
autos[2] = "audi"
print(autos)

#Ejercicio 8
print("")
print("==Ejercicio 8==")
print("")

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Ejercicio 9
print("")
print("==Ejercicio 9==")
print("")

compras = [["pan", "leche"],["arroz", "fideos", "salsa"],["agua"]]
#Agregamos jugo a la 3er lista:
compras[2].append("jugo")
#Reemplazamos fideos por tallarines:
compras[1][1] = "tallarines"
#Eliminamos pan de la lista:
compras[0].remove("pan")
print(compras)

#Ejercicio 10 
print("")
print("==Ejercicio 10==")
print("")

lista_anidada = ["15"],["True"],["25.5", "57.9", "30.6"], ["False"]
print(lista_anidada)


