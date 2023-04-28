"""
SEMANA 1 EJERCICIO N° 6

6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
Supongamos que pi = 3.1416

"""

A = int(input("Ingrese el valor del radio del circulo: "))
pi = 3.1416
#area = pi * pow(A,2)
area = pi * A ** 2
print(f"El area del circulo es: {area}")

"""
DETALLES DEL CODIGO:

1_ La línea A = int(input("Ingrese el valor del radio del círculo: ")) solicita al usuario que ingrese el valor del radio del círculo y lo guarda en la variable A. 
El int alrededor de input se utiliza para convertir la entrada del usuario en un número entero.
2_ La línea pi = 3.1416 define la variable pi y le asigna el valor de aproximadamente 3.1416. Esta es una aproximación del número pi, que se utiliza para el cálculo del área de un círculo.
3_ La línea area = pi * A ** 2 calcula el área del círculo utilizando la fórmula: área = pi * radio al cuadrado. 
En este caso, el radio es el valor ingresado por el usuario almacenado en la variable A.
4_ La última línea, print(f"El área del círculo es: {area}"), imprime en la pantalla un mensaje que muestra el área del círculo. 
El valor de la variable area se interpola en el mensaje utilizando la f-string.

En resumen, el programa solicita al usuario que ingrese el valor del radio de un círculo, calcula el área utilizando la fórmula correspondiente y muestra el resultado en la pantalla.
"""
