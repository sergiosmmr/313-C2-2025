"""IF - ELSE -ELIF

1_ A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
el programa deberá determinar la posición del jugador en la cancha, 
considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot"""


altura = float(input("ingrese altura en centimetros: "))
if altura < 160:
    posicion = "base"
elif altura >= 160 and altura < 179:
    posicion = "escolta"
elif altura >= 180 and altura < 199:
    posicion = "alero"
else:
    posicion = "Ala-Pívot o Pívot"

print(f"la posicion del jugador es {posicion}")    


"""2_ Calcular una nota aleatoria entre el 1 y el 10 inclusive, 
para luego mostrar un mensaje según el valor:
                                             _6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
                                             _4 y 5                ---> Aprobado, la nota es ...
                                             _1, 2 y 3            ---> Desaprobado, la nota
                                             _es ...
"""

nota = float(input("ingrese nota: "))

if nota >= 6 and nota <= 10:
    print(f"Promoción directa, la nota es {nota}")
if nota >= 4 and nota <= 5:
    print(f"Aprobado, la nota es {nota}")
if nota >= 1 and nota <= 3:
    print(f"Desaprobado, la nota es {nota}")


           

