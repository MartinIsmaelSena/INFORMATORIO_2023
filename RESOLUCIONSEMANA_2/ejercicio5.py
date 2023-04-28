"""
SEMANA 2 EJERCICIO N° 5

5-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es par o impar.
"""

num = int(input("Ingrese un numero: "))

if num % 2 == 0:
    print(f"El numero {num} es par.")
else:
    print(f"El numero {num} es impar.")

"""
DETALLES DEL CODIGO:

1_ La línea num = int(input("Ingrese un número: ")) solicita al usuario que ingrese un número y lo guarda en la variable num después de convertirlo en un número entero utilizando 
la función int().
2_ La línea if num % 2 == 0: verifica si el resto de la división del número ingresado entre 2 es igual a 0. Esto se utiliza para determinar si el número es divisible entre 2, 
lo que indica que es par.
3_ Si la condición es verdadera (es decir, si el número es par), se ejecuta la línea print(f"El número {num} es par."), que muestra en la pantalla un mensaje indicando que el 
número ingresado es par.
4_ Si la condición del if es falsa, se ejecuta la línea else:, lo que significa que el número es impar.
5_ Dentro del bloque else, se ejecuta la línea print(f"El número {num} es impar."), que muestra en la pantalla un mensaje indicando que el número ingresado es impar.

En resumen, el programa solicita al usuario que ingrese un número y determina si es par o impar utilizando la operación de módulo. Dependiendo de si el número es divisible entre 2 o no, 
se mostrará un mensaje correspondiente en la pantalla.
"""