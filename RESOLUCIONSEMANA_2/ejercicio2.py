"""
SEMANA 2 EJERCICIO N° 2

2-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es positivo, negativo o cero.
"""

num = int(input("Ingrese un numero: "))

if num == 0:
    print(f"El numero ingresado es igual a cero: {num}.")
elif num < 0:
    print(f"El numero ingresado es negativo: {num}.")
else:
    print(f"El numero ingresado es positivo: +{num}.")


"""
DETALLES DEL CODIGO:

1_ La línea num = int(input("Ingrese un número: ")) solicita al usuario que ingrese un número entero y lo guarda en la variable num después de convertirlo utilizando la función int().
2_ La línea if num == 0: verifica si el número ingresado es igual a cero.
3_ Si la condición es verdadera (es decir, si el número es igual a cero), se ejecuta la línea print(f"El número ingresado es igual a cero: {num}."), que muestra en la pantalla un mensaje 
indicando que el número ingresado es igual a cero y muestra el número ingresado.
4_ Si la condición del if es falsa, se pasa a la siguiente condición.
5_ La línea elif num < 0: verifica si el número ingresado es menor que cero.
6_ Si la condición es verdadera (es decir, si el número es menor que cero), se ejecuta la línea print(f"El número ingresado es negativo: {num}."), que muestra en la pantalla un mensaje 
indicando que el número ingresado es negativo y muestra el número ingresado.
7_ Si ninguna de las condiciones anteriores es verdadera, se ejecuta la línea else:, lo que significa que el número ingresado es positivo.
8_ Dentro del bloque else, se ejecuta la línea print(f"El número ingresado es positivo: +{num}."), que muestra en la pantalla un mensaje indicando que el número ingresado es positivo y 
muestra el número con un signo "+".

En resumen, el programa solicita al usuario que ingrese un número entero y muestra un mensaje indicando si el número es igual a cero, negativo o positivo. Dependiendo del valor ingresado, 
se mostrará un mensaje correspondiente en la pantalla.
"""