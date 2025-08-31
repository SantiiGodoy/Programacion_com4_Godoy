#Ej Condicional Presencial
print("==Bienvenido==")
print("")


formato_correcto_dia ={
    "lunes": "Nivel Inicial",
    "martes": "Nivel Intermedio",
    "miercoles":"Nivel Avanzado",
    "jueves": "Practica hablada",
    "viernes": "Ingles para viajeros"
}
formato_correcto_mes = ["1","2","3","4","5","6","7","8","9","10","11","12"]
dia = str(input("Digite dia de la Semana(Lunes a Viernes): ")).lower()
numero_dia = int(input("Digite numero del Dia: "))
mes = int(input("Digite numero de Mes(1 al 12): "))
print("")

if dia in formato_correcto_dia:
    print(f"Fecha:{numero_dia}/{mes}\nIngresaste: Dia {dia.capitalize()} = {formato_correcto_dia[dia]}")
else:
    print(f"El dia que ingresaste es inválido!")
print("")









