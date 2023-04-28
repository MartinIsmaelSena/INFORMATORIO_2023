"""
SEMANA 1 EJERCICIO N° 11

11-Crea un programa que pida al usuario una palabra y muestre en pantalla
cuántas letras tiene.
Pss psssss toma... .len()
"""

palabra = input("Ingrese una palabra o frase: ")
print(f"La palabra o frase ingresada tiene una longitud de: ", len(palabra))

"""
DETALLES DEL CODIGO:

1_ La línea palabra = input("Ingrese una palabra o frase: ") solicita al usuario que ingrese una palabra o frase y la guarda en la variable palabra.
2_ La línea print(f"La palabra o frase ingresada tiene una longitud de: ", len(palabra)) utiliza una f-string para imprimir en la pantalla un mensaje 
que muestra la longitud de la palabra o frase ingresada. La función len(palabra) devuelve la cantidad de caracteres en la palabra o frase y ese valor se muestra en el mensaje.

En resumen, el programa solicita al usuario que ingrese una palabra o frase, calcula su longitud utilizando la función len(), y muestra la cantidad de caracteres en la pantalla.
"""