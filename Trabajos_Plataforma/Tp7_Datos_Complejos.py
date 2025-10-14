#===================================================================================================
#Ejercicio 1
print("==Ejercicio 1==")
print("")

precios_frutas = {'Banana': 1200, 'Ananá' : 2500, 'Melón' : 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
print(precios_frutas)

#Ejercicio 3
frutas = list(precios_frutas.keys())
print(frutas)

#Ejercicio 4
print("")
print("==Ejercicio 4==")
print("")

agenda = {}

while True:
    print("\n--- AGENDA TELEFÓNICA ---")
    print("1. Agregar contacto")
    print("2. Consultar contacto")
    print("3. Mostrar todos")
    print("4. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        numero = input("Ingrese el número telefónico: ")

        # Validar que el número contenga solo dígitos
        if not numero.isdigit():
            print("El número debe contener solo dígitos.")
        else:
            agenda[nombre] = numero
            print(f"Contacto '{nombre}' agregado correctamente.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre que desea buscar: ")
        if nombre in agenda:
            print(f"El número de {nombre} es: {agenda[nombre]}")
        else:
            print(f"No se encontró el contacto '{nombre}'.")

    elif opcion == "3":
        print("\nContactos guardados:")
        if not agenda:
            print("No hay contactos aún.")
        else:
            for nombre, numero in agenda.items():
                print(f"{nombre}: {numero}")

    elif opcion == "4":
        print("Programa finalizado.")
        break 

    else:
        print("Opción no válida. Intente nuevamente.")

#Ejercicio 5
print("==Ejercicio 5==")
frase = input("Escribí una frase:").lower()

palabras = frase.split()

palabras_set = set(palabras)
print(f"Palabras únicas, {palabras_set}")

cantidad = {}

for palabra in palabras:
    if palabra in cantidad:
        cantidad[palabra] += 1
    else:
        cantidad[palabra] = 1

        print("Frecuencia de palabras:",cantidad)

#Ejercicio 6
print("")
print("==Ejercicio 6==")
print("")

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}:")

    n1 = float(input("Ingrese la primer nota:"))
    n2 = float(input("Ingrese la segunda nota:"))
    n3 = float(input("Ingrese la tercer nota:"))

alumnos[nombre] = (n1,n2,n3)

print("==Promedios==")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

#Ejercicio 7
print("")
print("==Ejercicio 7==")
print("")

p1 = {"Matías","Facundo","Santino"}
p2 = {"Lautaro","Facundo","Santino"}

ambos = p1 & p2
print(f"Aprobaron los dos parciales: {ambos}")

aprob_uno = p1 ^ p2
print(f"Aprobó uno solo: {aprob_uno}")

#Ejercicio 8
print("")
print("==Ejercicio 8==")
print("")

stock = {
    "chocolate": 5,
    "banana": 8,
}
print(f"Stock: {stock}")

producto = input("Ingrese el nombre del producto:").lower()

if producto in stock:
    print(f"{producto} es: {stock[producto]}")
    agregar = int(input("Ingrese unidades para agregar al stock:"))
    stock[producto] += agregar
    print(f"Stock actualizado de {producto}: {stock[producto]}")
else:
    print("El producto no está cargado.")
    nuevo_stock = int(input("Ingrese el stock inicial del producto nuevo:"))
    stock[producto] = nuevo_stock
    print(f"Producto agregado: {producto} con stock {nuevo_stock}")

    print("Stock actualizado:", stock)

#Ejercicio 9
print("")
print("==Ejercicio 9==")
print("")

agenda = {
    ("lunes", "08:00"): "Clase de programación",
    ("martes", "08:00"): "Clase de matemáticas",
    ("viernes", "16:00"): "Horario de salida laboral"}

print("Agenda actual:")
for clave, evento in agenda.items():
    print(f"{clave}: {evento}")

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay actividad programada en ese día y hora.")

#Ejercicio 10
print("")
print("==Ejercicio 10==")
print("")

paises = {"Argentina": "Buenos Aires","Chile": "Santiago","Uruguay": "Montevideo","Brasil": "Brasilia","Paraguay": "Asunción"}

print("Diccionario original (país -> capital):")
print(paises)

capitales = {capital: pais for pais, capital in paises.items()}

print("Nuevo diccionario (capital -> país):")
print(capitales)
