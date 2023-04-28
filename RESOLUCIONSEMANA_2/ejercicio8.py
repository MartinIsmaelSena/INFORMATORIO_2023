"""
SEMANA 2 EJERCICIO N° 8

8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
por pantalla si contiene la letra "a".
"""

palabra = input("Ingrese una palabra o frase: ")
caracter = input("Ingresa que caracter queres buscar: ")


if caracter in palabra:
    print(f"El caracter {caracter} se encuentra en la palabra ingresada")
else:
    print(f"No esta el caracter '{caracter}' en la palabra")


"""
DETALLES DEL CODIGO:

1_ La línea palabra = input("Ingrese una palabra o frase: ") solicita al usuario que ingrese una palabra o frase y la guarda en la variable palabra.
2_ La línea caracter = input("Ingresa qué carácter quieres buscar: ") solicita al usuario que ingrese el carácter que desea buscar en la palabra y lo guarda en la variable caracter.
3_ La condición if caracter in palabra: verifica si el carácter está presente en la palabra utilizando el operador in. Si el carácter se encuentra en la palabra, se ejecuta la línea 
print(f"El carácter {caracter} se encuentra en la palabra ingresada."), que muestra en la pantalla un mensaje indicando que el carácter se encuentra en la palabra ingresada.
4_ Si la condición no se cumple, se ejecuta la línea else:, lo que significa que el carácter no está presente en la palabra. En este caso, se muestra en la pantalla el mensaje 
print(f"No está el carácter '{caracter}' en la palabra.").

En resumen, el programa permite al usuario ingresar una palabra o frase y un carácter, y luego verifica si ese carácter está presente en la palabra. Dependiendo del resultado de 
la verificación, se muestra un mensaje apropiado en la pantalla.
"""