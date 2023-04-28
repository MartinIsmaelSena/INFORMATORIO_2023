"""
SEMANA 1 EJERCICIO N° 17

17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
en orden inverso.
Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
"mundo hola".
Importante!!! Utiliza un solo print() 😈.
"""

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese una segunda palabra: ")

print(palabra2 + " " + palabra1)

"""
DETALLES DEL CODIGO:

1_ La línea palabra1 = input("Ingrese una palabra: ") solicita al usuario que ingrese una palabra y la guarda en la variable palabra1.
2_ La línea palabra2 = input("Ingrese una segunda palabra: ") solicita al usuario que ingrese una segunda palabra y la guarda en la variable palabra2.
3_ La línea print(palabra2 + " " + palabra1) concatena las palabras ingresadas por el usuario en el orden inverso, separadas por un espacio en blanco. 
Luego, muestra el resultado en la pantalla utilizando la función print().

En resumen, el programa solicita al usuario que ingrese dos palabras, las concatena en el orden inverso y muestra el resultado en la pantalla.
"""