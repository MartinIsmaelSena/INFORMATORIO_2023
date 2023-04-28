"""
SEMANA 2 EJERCICIO N° 11

11-Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares.
"""

num1 = int(input("Ingrese un numero para la operación: "))
num2 = int(input("Ingrese un segundo numero para la operación: "))

if (num1 % 2 == 0) and  (num2 % 2 == 0):
    print(f"El resultado de la suma del los numeros ingresados {num1} + {num2}: {num1+num2}")
else:
    print("No cumplen con los requisitos para la operación.")

"""
DETALLES DEL CODIGO:

1_ La línea num1 = int(input("Ingrese un numero para la operación: ")) solicita al usuario que ingrese un número y lo guarda en la variable num1. El número ingresado se convierte 
a entero utilizando la función int().
2_ La línea num2 = int(input("Ingrese un segundo numero para la operación: ")) solicita al usuario que ingrese otro número y lo guarda en la variable num2. Al igual que en el caso 
anterior, el número ingresado se convierte a entero.
3_ La condición if (num1 % 2 == 0) and (num2 % 2 == 0): verifica si tanto num1 como num2 son números pares. La expresión (num1 % 2 == 0) verifica si num1 es divisible por 2, 
es decir, si es par. De manera similar, la expresión (num2 % 2 == 0) verifica si num2 es par.
4_ Si la condición se cumple, se ejecuta la línea print(f"El resultado de la suma de los números ingresados {num1} + {num2}: {num1+num2}"), que muestra en pantalla el resultado de 
la suma de los dos números ingresados.
5_ Si la condición no se cumple, es decir, al menos uno de los números no es par, se ejecuta el bloque else:. En este caso, se ejecuta la línea print("No cumplen con los requisitos 
para la operación."), que muestra en pantalla un mensaje indicando que los números ingresados no cumplen con los requisitos para realizar la operación.

En resumen, el programa solicita dos números al usuario y verifica si ambos son pares. Si ambos números son pares, se realiza la suma de ellos y se muestra el resultado en pantalla. 
Si al menos uno de los números no es par, se muestra un mensaje indicando que no se cumplen los requisitos para realizar la operación.
"""