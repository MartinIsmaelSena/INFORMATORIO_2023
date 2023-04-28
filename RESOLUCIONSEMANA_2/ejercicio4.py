"""
SEMANA 2 EJERCICIO N° 4

4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
pantalla si está aprobado (5 o más) o no.
"""

nota = int(input("Ingrese su nota: "))

if nota > 5:
    print(f"Aprobaste con un: {nota}")
else:
    print(f"Desaprobaste con un: {nota}")

"""
DETALLES DEL CODIGO:

1_ La línea nota = int(input("Ingrese su nota: ")) solicita al usuario que ingrese una nota y la guarda en la variable nota después de convertirla en un número entero utilizando 
la función int().
2_ La línea if nota > 5: verifica si la nota ingresada es mayor que 5.
3_ Si la condición es verdadera (es decir, si la nota es mayor que 5), se ejecuta la línea print(f"Aprobaste con un: {nota}"), que muestra en la pantalla un mensaje indicando que 
el estudiante aprobó y muestra la nota ingresada.
4_ Si la condición del if es falsa, se ejecuta la línea else:, lo que significa que la nota es igual a 5 o menor.
5_ Dentro del bloque else, se ejecuta la línea print(f"Desaprobaste con un: {nota}"), que muestra en la pantalla un mensaje indicando que el estudiante desaprobó y muestra la nota 
ingresada.

En resumen, el programa solicita al usuario que ingrese una nota y muestra un mensaje indicando si el estudiante aprobó o desaprobó según si la nota ingresada es mayor que 5. Dependiendo del valor de la nota, se mostrará un mensaje correspondiente en la pantalla.
"""