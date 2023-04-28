"""
SEMANA 2 EJERCICIO N° 9

9-Escribir un programa que pida al usuario tres números y muestre por pantalla
el mayor de ellos.
"""
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

if num1 == num2 and num2 == num3:
    print("Los tres numeros ingresados son iguales")
else:
    print("El mayor numero ingresado es: ", max(num1,num2,num3))

"""
DETALLES DEL CODIGO:

1_ La línea num1 = float(input("Ingresa el primer numero: ")) solicita al usuario que ingrese el primer número y lo guarda en la variable num1. El número ingresado se convierte a tipo float.
2_ La línea num2 = float(input("Ingresa el segundo numero: ")) solicita al usuario que ingrese el segundo número y lo guarda en la variable num2. También se convierte a tipo float.
3_ La línea num3 = float(input("Ingresa el tercer numero: ")) solicita al usuario que ingrese el tercer número y lo guarda en la variable num3. Igualmente, se convierte a tipo float.
4_ La condición if num1 == num2 and num2 == num3: verifica si los tres números ingresados son iguales utilizando el operador de igualdad ==. Si se cumple esta condición, se ejecuta la 
línea print("Los tres numeros ingresados son iguales"), que muestra en la pantalla el mensaje indicando que los tres números son iguales.
5_ Si la condición no se cumple, se ejecuta el bloque else:. Esto significa que al menos dos números son distintos entre sí. En este caso, se utiliza la función max() para determinar 
el mayor número ingresado entre num1, num2 y num3. La línea print("El mayor numero ingresado es: ", max(num1,num2,num3)) muestra en la pantalla el mensaje junto con el valor del mayor número.

En resumen, el programa permite al usuario ingresar tres números y luego realiza una comparación para determinar si son iguales o encuentra el mayor número ingresado. Dependiendo del 
resultado de la comparación, se muestra un mensaje apropiado en la pantalla.
"""

