"""
SEMANA 2 EJERCICIO N° 3

3-Escribir un programa que pida al usuario dos números y muestre por pantalla
cuál de ellos es mayor.
"""
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(f"El numero 1 es mayor con: {num1}")
else:
    print(f"El numero 2 es mayor con: {num2}")

"""
DETALLES DEL CODIGO:

1_ La línea num1 = int(input("Ingrese el primer número: ")) solicita al usuario que ingrese el primer número entero y lo guarda en la variable num1 después de convertirlo 
utilizando la función int().
2_ La línea num2 = int(input("Ingrese el segundo número: ")) solicita al usuario que ingrese el segundo número entero y lo guarda en la variable num2 después de convertirlo 
.utilizando la función int().
3_ La línea if num1 > num2: compara si el valor de num1 es mayor que el valor de num2.
4_ Si la condición es verdadera (es decir, si num1 es mayor que num2), se ejecuta la línea print(f"El número 1 es mayor con: {num1}"), que muestra en la pantalla un mensaje 
indicando que el número 1 es mayor y muestra el valor de num1.
5_ Si la condición del if es falsa, se ejecuta la línea else:, lo que significa que num2 es mayor que o igual a num1.
6_ Dentro del bloque else, se ejecuta la línea print(f"El número 2 es mayor con: {num2}"), que muestra en la pantalla un mensaje indicando que el número 2 es mayor y muestra 
el valor de num2.

En resumen, el programa solicita al usuario que ingrese dos números enteros y muestra un mensaje indicando cuál de los dos números es mayor. Dependiendo de la comparación entre 
los números, se mostrará un mensaje correspondiente en la pantalla.
"""