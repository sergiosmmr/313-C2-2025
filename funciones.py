# Nivel Básico
# 1. Función que saluda a una persona

# Enunciado:
# Escribí una función que reciba un nombre y muestre un saludo personalizado.
# que lo ingrese por consola


# def saludar (persona):
#     print(f"hola {persona}")

# nombre = input ("ingrese su nombre: ")

# saludar(nombre)

# """
# Enunciado:
# Escribí una función que reciba base y altura, y devuelva el área.
# Datos por consola un argumento por defecto =10
# """

# def calcular_area(base = 10, altura = 10) -> int:
#     area = base * altura

#     return area 

# base = float (input ("ingrese base de traingulo: "))
# altura = float (input ("ingrese altura del triangulo: "))

# print (f"el area del triangulo es: {calcular_area(base,altura)}")

"""Nivel Intermedio
Función que devuelva suma, resta y multiplicación

Enunciado:
Escribí una función que reciba dos números y devuelva los tres resultados: 
suma, resta y multiplicación."""

# def operatoria (num_1, num_2):
#     suma = num_1 + num_2
#     resta = num_1 - num_2
#     multiplicacion = num_1 + num_2

#     return suma,resta,multiplicacion

# numero_1 = float(input("ingrese primer numero a operar: "))
# numero_2 = float(input("ingrese segundo numero a operar: "))

# suma ,resta ,multiplicacion = operatoria(numero_1,numero_2)
# print(f"la suma de sus numeros es : {suma}")
# print(f"la resta de sus numeros es : {resta}")
# print(f"la multiplicacion de sus numeros es : {multiplicacion}")

"""Enunciado:
Escribí una función que reciba cualquier cantidad de números y los multiplique los parametros por consola.

Ayuda: pedir al usuario cuantos numeros cargar, luego usar ese valor para iterar"""

def multiplicar_numeros():
    cantidad = int(input("ingrese Cuántos números quiere multiplicar: "))
    resultado = 1
    
    for i in range(0,cantidad):
        numero = float(input(f"Ingresa el número {i + 1}: "))
        resultado *= numero
    
    print(f"El resultado de la multiplicación es: {resultado}")

multiplicar_numeros()
