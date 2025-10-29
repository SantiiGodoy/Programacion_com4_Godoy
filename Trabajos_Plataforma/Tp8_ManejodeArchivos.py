
#Ejercicio 1
print("==Ejercicio 1==")
print("")

with open("productos.txt", "w") as archivo:
    archivo.write("Galletas,300,30\n")
    archivo.write("Tortita,150,15\n")
    archivo.write("Jugo,220,5\n")

    print("Archivo 'productos.txt' creado.")

#Ejercicio 2
print("")
print("==Ejercicio 2==")
print("")

with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Ejercicio 3
print("")
print("==Ejercicio 3==")
print("")

with open ("productos.txt", "r") as archivo:
    print("Lista de productos:")
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("")
print("Agregar productos:")
nombre_producto = input("Ingrese el nombre del producto:")
precio = input("Ingrese el precio del producto:")
cantidad = input("Ingrese la cantidad del producto:")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre}, {precio}, {cantidad}")
print("El producto se agregó correctamente!")

#Ejercicio 4
print("")
print("==Ejercicio 4==")
print("")

productos = []

with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        producto = {
            "nombre" : nombre,
            "precio" : float(precio),
            "cantidad" : int(cantidad)
        }
        productos.append(producto)

print("Lista de productos cargados:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

#Ejercicio 5
print("")
print("==Ejercicio 5==")
print("")

buscar = input("Ingrese nombre del producto:")
with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append()

buscar = input("Ingrese el nombre del producto a buscar:")

encontrado = False

for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print("El producto ha sido encontrado:")
        print(f"Nombre {p["nombre"]}")
        print(f"Precio ${p["precio"]}")
        print(f"Cantidad {p["cantidad"]}")
        encontrado = True
        break

if not encontrado:
    print("El producto no existe en la lista.")

#Ejercicio 6
print("")
print("==Ejercicio 6==")
print("")

nuevos = {
    "nombre": "Tomate",
    "precio": 200,
    "cantidad": 12
}
productos.append(nuevos)

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p["nombre"]},{p["precio"]},{p["cantidad"]}")

print("Se actualizo la lista correctamente!")





