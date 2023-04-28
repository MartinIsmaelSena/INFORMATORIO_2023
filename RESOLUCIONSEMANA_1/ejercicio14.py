"""
SEMANA 1 EJERCICIO N° 14

14-Escribe un programa que solicite al usuario un número entero y luego
imprima el doble y el triple de ese número.
"""

numero = int(input("Ingrese un numero: "))
print(f"El doble del numero ingresado '{numero}' es: {numero*2} y el triple: {numero * 3}")

"""
DETALLES DEL CODIGO:

1_ La línea numero = int(input("Ingrese un número: ")) solicita al usuario que ingrese un número y lo convierte en un entero utilizando la función int(). 
El resultado se guarda en la variable numero.
2_ La línea print(f"El doble del número ingresado '{numero}' es: {numero*2} y el triple: {numero * 3}") utiliza una f-string para imprimir en la pantalla 
un mensaje que muestra el número ingresado por el usuario, el doble de ese número y el triple de ese número. Los cálculos se realizan utilizando las operaciones de multiplicación *.

En resumen, el programa solicita al usuario que ingrese un número, calcula su doble y triple, y muestra los resultados en la pantalla junto con el número ingresado.
"""