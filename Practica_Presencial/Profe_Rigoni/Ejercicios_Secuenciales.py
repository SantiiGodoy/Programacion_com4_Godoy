#PROPINA RESTAURANTE:
#Pedir al usuario el monto total de la cuenta.
#Calcular la propina sugerida al 10%.
#Calcular la propina sugerida al 15%.
#Calcular el total a pagar en ambos casos (cuenta + propina).
#Mostrar todos los resultados en pantalla

monto_cuenta = float(input("Ingrese el monto a pagar de la cuenta: "))

propina_10 = (monto_cuenta *10) / 100
propina_15 = (monto_cuenta *15) / 100
monto_10 = propina_10 + monto_cuenta
monto_15 = propina_15 + monto_cuenta

print(" ===Cuenta UTN BAR=== ")
print("")

print(f"El total de la cuenta es: ${monto_cuenta} pesos.")
print(f"El 10% de propina es: ${propina_10} pesos. ")
print(f"El 15% de propina es: ${propina_15} pesos. ")
print(f"Con el 10% incluido al total: ${monto_10} ")
print(f"Con el 15% incluido al total: ${monto_15} ")