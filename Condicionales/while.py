"""                     WHILE


        Contadores - Acumuladores - Máximos y mínimos


1_ Mostrar 10 repeticiones de números ascendentes desde el 1 al 10."""

# numero = 1
# while numero < 11:
#     print(numero)
#     numero += 1


"""2_ Mostrar 10 repeticiones de números descendentes desde el 10 al 1."""

# numero = 10
# while numero > 0:
#     print(numero)
#     numero -= 1

"""3_Mostrar la suma de los números desde el 1 hasta el 10."""

# numero = 1
# acumulador = 0
# while numero < 11:
#     acumulador += numero 
#     numero += 1

#     print(acumulador)

"""4_ Mostrar la suma de los números pares desde el 1 hasta el 10."""

# numero = 1
# acumulador = 0
# while numero < 11:
#     acumulador += numero 
#     numero += 1
#     if acumulador % 2 == 0:
#         print(acumulador)


"""5_Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla."""

# numero = 1
# acumulador = 0
# while numero < 6:
#     ingreso = float(input(f"ingrese numero {numero}: "))
#     acumulador += ingreso
#     numero += 1
# print(f"la suma de los numeros es {acumulador}\n el promedio de los numeros es {acumulador/5}")

"""6_Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos."""

# numero = 0
# acumulador = 0
# respuesta = True
# while respuesta == True:
#     numero += 1
#     ingreso = float(input(f"ingrese numero {numero}: "))
#     acumulador += ingreso
#     pregunta = input("desea seguir ingresando numeros? [S/N]: ").upper()
#     print(f"la respuesta del primer while es: {pregunta}")
#     while pregunta != "S" and pregunta != "N":
#         pregunta = input("ingrese respuesta correcta: [S/N]").upper()
#         print(f"la respuesta del segundo while es: {pregunta}")

        
#     if pregunta == "N":
#         respuesta = False
          

# print(f"la suma de los numeros es {acumulador}\n el promedio de los numeros es {acumulador/numero}")

"""7_Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
Calcular la suma de los números positivos y el producto de los negativos.
"""

# numero = 0
# acumulador_positivo = 0
# acumulador_negativo = 1
# hay_negativos = False  # bandera para saber si se ingresaron negativos
# respuesta = True

# while respuesta:
#     numero += 1
#     ingreso = float(input(f"Ingrese número {numero}: "))

#     if ingreso > 0:
#         acumulador_positivo += ingreso
#     elif ingreso < 0:
#         acumulador_negativo *= ingreso
#         hay_negativos = True  # marco que hubo al menos un negativo

#     pregunta = input("¿Desea seguir ingresando números? [S/N]: ").upper()
#     while pregunta != "S" and pregunta != "N":
#         pregunta = input("Ingrese respuesta correcta [S/N]: ").upper()

#     if pregunta == "N":
#         respuesta = False

# print(f"La suma de los números positivos es {acumulador_positivo}")
# if hay_negativos:
#     print(f"El producto de los números negativos es {acumulador_negativo}")
# else:
#     print("No se ingresaron números negativos")


# """8_Ingresar 10 números enteros. Determinar el máximo y el mínimo."""

# contador = 0
# maximo = 0
# minimo = 0

# while contador < 10:
#     contador += 1
#     numero = int(input(f"ingrese numero entero {contador}: "))
#     if contador == 1:
#         minimo = maximo = numero
#     if maximo < numero:
#         maximo = numero
#     elif minimo > numero:
#         minimo = numero
    
# print(f"el numero maximo es: {maximo}")
# print(f"el numero minimo es: {minimo}")
"""
9_Solicitar al usuario que ingrese como mínimo 5 números.
Calcular la suma de los números ingresados y el promedio de los mismos.
"""

contador = 0
acumulador = 0.0

# Primero: asegurar mínimo 5
while contador < 5:
    ingreso = float(input("Ingrese número: "))
    acumulador += ingreso
    contador += 1

# Luego: permitir seguir cargando si querés
while True:
    continuar = input("¿Desea continuar? [S/N]: ").strip().upper()
    while continuar not in ("S", "N"):
        print("\tERROR: ingrese S o N\n")
        continuar = input("¿Desea continuar? [S/N]: ").strip().upper()

    if continuar == "N":
        break

    ingreso = float(input("Ingrese número: "))
    acumulador += ingreso
    contador += 1

print(f"La suma de los números es {acumulador}")
print(f"El promedio de los números es {acumulador/contador:.2f}")


    
""""
10_Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos."""



