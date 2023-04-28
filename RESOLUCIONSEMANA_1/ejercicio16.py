"""
SEMANA 1 EJERCICIO N° 16

16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
e imprima su índice de masa corporal (IMC).
La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).
"""

peso = float(input("Ingrese su peso actual: "))
altura = float(input("Ingrese su altura: "))
imc = peso / (altura **2)
print(f"Su masa corporal actual es de:  {imc}")

"""
DETALLES DEL CODIGO:

1_ La línea peso = float(input("Ingrese su peso actual: ")) solicita al usuario que ingrese su peso actual y lo convierte en un número decimal utilizando la función float(). 
El resultado se guarda en la variable peso.
2_ La línea altura = float(input("Ingrese su altura: ")) solicita al usuario que ingrese su altura y lo convierte en un número decimal utilizando la función float(). 
El resultado se guarda en la variable altura.
3_ La línea imc = peso / (altura ** 2) calcula el índice de masa corporal (IMC) dividiendo el peso por el cuadrado de la altura. El resultado se guarda en la variable imc.
4_ La línea print(f"Su masa corporal actual es de: {imc}") utiliza una f-string para imprimir en la pantalla un mensaje que muestra el valor del IMC calculado.

En resumen, el programa solicita al usuario que ingrese su peso actual y altura, calcula el índice de masa corporal utilizando la fórmula y muestra el resultado en la pantalla.
"""