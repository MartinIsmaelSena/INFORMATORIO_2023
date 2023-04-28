"""
SEMANA 1 EJERCICIO N° 19

19-Escribe un programa que solicite al usuario un número decimal y luego
imprima la parte entera y decimal por separado.
"""
numero = float(input("Ingresa un numero con decimal: "))
numero_entero = int(numero)
numero_decimal = round(numero - numero_entero, 2)
print(f"La parte entera del numero ingresado es: {numero_entero}")
print(f"La parte decimal del numero ingresado es: {numero_decimal}")

"""
DETALLES DEL CODIGO:

1_ La línea numero = float(input("Ingresa un número con decimal: ")) solicita al usuario que ingrese un número con decimal y lo convierte en un número decimal utilizando la función float(). 
El resultado se guarda en la variable numero.
2_ La línea numero_entero = int(numero) convierte el número decimal en un número entero utilizando la función int(). Esto extrae la parte entera del número. 
El resultado se guarda en la variable numero_entero.
3_ La línea numero_decimal = round(numero - numero_entero, 2) calcula la parte decimal del número restando la parte entera del número original. 
La función round() se utiliza para redondear el resultado a 2 decimales. El resultado se guarda en la variable numero_decimal.
4_ La línea print(f"La parte entera del número ingresado es: {numero_entero}") utiliza una f-string para imprimir en la pantalla un mensaje que muestra la parte entera del número 
ingresado por el usuario.
5_ La línea print(f"La parte decimal del número ingresado es: {numero_decimal}") utiliza una f-string para imprimir en la pantalla un mensaje que muestra la parte decimal del 
número ingresado por el usuario.

En resumen, el programa solicita al usuario que ingrese un número decimal, extrae la parte entera y la parte decimal del número y las muestra en la pantalla en mensajes separados.
"""