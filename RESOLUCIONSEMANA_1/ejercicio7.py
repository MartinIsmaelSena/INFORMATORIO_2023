"""
SEMANA 1 EJERCICIO N° 7

7-Escribe un programa que calcule el área de un triángulo a partir de la base y la
altura dadas.

"""
base = float(input("Ingrese el valor de la base: "))
altura = float(input("Ingrese el valor de la altura: "))
area = (base * altura) / 2
print(f"El area del circulo es: {area}")

"""
DETALLES DEL CODIGO:

1_ La línea base = float(input("Ingrese el valor de la base: ")) solicita al usuario que ingrese el valor de la base del triángulo y lo guarda en la variable base. 
El float alrededor de input se utiliza para convertir la entrada del usuario en un número decimal.
2_ La línea altura = float(input("Ingrese el valor de la altura: ")) solicita al usuario que ingrese el valor de la altura del triángulo y lo guarda en la variable altura. 
Al igual que en el paso anterior, float se utiliza para convertir la entrada en un número decimal.
3_ La línea area = (base * altura) / 2 calcula el área del triángulo utilizando la fórmula: área = (base * altura) / 2. 
Los valores de la base y la altura ingresados por el usuario se utilizan en el cálculo.
4_ La última línea, print(f"El área del triángulo es: {area}"), imprime en la pantalla un mensaje que muestra el área del triángulo. 
El valor de la variable area se interpola en el mensaje utilizando la f-string.

En resumen, el programa solicita al usuario que ingrese el valor de la base y la altura de un triángulo, calcula el área utilizando la fórmula correspondiente y muestra el resultado en la pantalla.
"""