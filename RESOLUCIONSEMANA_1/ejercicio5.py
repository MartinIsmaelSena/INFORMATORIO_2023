"""
SEMANA 1 EJERCICIO N° 5

5-Crea un programa que pida al usuario dos números enteros y muestre en
pantalla su cociente y su resto.
"""
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
cociente = num1 // num2
resto = num1 % num2
print(f"El cociente de los numeros ingresados es: {cociente} y el resto: {resto}")

"""
DETALLES DEL CODIGO:

1_ La línea num1 = int(input("Ingrese un numero: ")) solicita al usuario que ingrese un número y lo guarda en la variable num1. 
El int alrededor de input se utiliza para convertir la entrada del usuario en un número entero.
2_ La línea num2 = int(input("Ingrese otro numero: ")) solicita al usuario que ingrese otro número y lo guarda en la variable num2. 
Al igual que en el paso anterior, int se utiliza para convertir la entrada en un número entero.
3_ La línea cociente = num1 // num2 calcula la división entera de num1 entre num2 y guarda el resultado en la variable cociente. 
La división entera devuelve la parte entera del resultado de la división.
4_ La línea resto = num1 % num2 calcula el resto de la división de num1 entre num2 y guarda el resultado en la variable resto. El operador % devuelve el resto de una división.
5_ La última línea, print(f"El cociente de los números ingresados es: {cociente} y el resto: {resto}"), imprime en la pantalla un mensaje que muestra el cociente y el resto de la división. 
Los valores de las variables cociente y resto se interpolan en el mensaje utilizando la f-string.

En resumen, el programa solicita al usuario que ingrese dos números, calcula el cociente y el resto de la división entre esos números, y muestra los resultados en la pantalla.
"""