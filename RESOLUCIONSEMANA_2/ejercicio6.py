"""
SEMANA 2 EJERCICIO N° 6

6-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es múltiplo de 2 y de 3 a la vez.
"""

num = int(input("Ingrese el numero para la verificación: "))

if (num % 2 == 0) and (num % 3 == 0):
    print(f"El numero {num} es multiplo de 2 y 3.")
elif (num % 2 == 0) and (num % 3 != 0):
    print(f"El numero {num} es multiplo de 2 pero 'NO' es multiplo de 3.")
elif (num % 2 != 0) and (num % 3 == 0):
    print(f"El numero {num} es multiplo de 3 pero 'NO' es multiplo de 2.")
else:
    print(f"El numero {num} 'NO' es multiplo de 2 y 3.")

"""
DETALLES DEL CODIGO:

1_ La línea num = int(input("Ingrese el número para la verificación: ")) solicita al usuario que ingrese un número y lo guarda en la variable num después de convertirlo en un 
número entero utilizando la función int().
2_ La primera condición if (num % 2 == 0) and (num % 3 == 0): verifica si el número ingresado es divisible entre 2 y 3 simultáneamente. Si ambas condiciones son verdaderas, 
se ejecuta la línea print(f"El número {num} es múltiplo de 2 y 3."), que muestra en la pantalla un mensaje indicando que el número es múltiplo de 2 y 3.
3_ Si la primera condición no se cumple, se pasa a la siguiente condición elif (num % 2 == 0) and (num % 3 != 0):. Esta condición verifica si el número es divisible entre 2 pero 
no es divisible entre 3. Si esta condición es verdadera, se ejecuta la línea print(f"El número {num} es múltiplo de 2 pero 'NO' es múltiplo de 3."), que muestra en la pantalla un 
mensaje indicando que el número es múltiplo de 2 pero no de 3.
4_ Si ninguna de las dos condiciones anteriores se cumple, se pasa a la siguiente condición elif (num % 2 != 0) and (num % 3 == 0):. Esta condición verifica si el número no es 
divisible entre 2 pero es divisible entre 3. Si esta condición es verdadera, se ejecuta la línea print(f"El número {num} es múltiplo de 3 pero 'NO' es múltiplo de 2."), 
que muestra en la pantalla un mensaje indicando que el número es múltiplo de 3 pero no de 2.
5_ Si ninguna de las tres condiciones anteriores se cumple, se ejecuta la línea else:, lo que significa que el número no es múltiplo de 2 ni de 3. En este caso, se muestra en la 
pantalla el mensaje print(f"El número {num} 'NO' es múltiplo de 2 y 3.").

En resumen, el programa solicita al usuario que ingrese un número y determina si es múltiplo de 2 y/o 3 utilizando la operación de módulo. Dependiendo de las condiciones cumplidas, 
se mostrará un mensaje correspondiente en la pantalla.
"""