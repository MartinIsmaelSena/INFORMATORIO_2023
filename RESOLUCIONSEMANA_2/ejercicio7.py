"""
SEMANA 2 EJERCICIO N° 7

7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, un número o un carácter especial.
"""

caracter = input("Ingrese el caracter para verificación: ")

if caracter[0].isnumeric():
    print(f"El caracter ingresado {caracter} es 'Numerico: 1, 2, 3..'.")
elif caracter[0].islower():
    print(f"El caracter ingresado {caracter} esta en 'minusculas'.")
elif caracter[0].isupper():
    print(f"El caracter ingresado {caracter} esta en 'MAYUSCULA'.")
else:
    print(f"El caracter ingresado {caracter} es 'especial'.")


"""
DETALLES DEL CODIGO:

1_ La línea caracter = input("Ingrese el carácter para verificación: ") solicita al usuario que ingrese un carácter y lo guarda en la variable caracter.
2_ La primera condición if caracter[0].isnumeric(): verifica si el primer carácter del input es numérico utilizando el método isnumeric(). Si el carácter 
es numérico, se ejecuta la línea print(f"El carácter ingresado {caracter} es 'Numérico: 1, 2, 3...'.")., que muestra en la pantalla un mensaje indicando que el carácter es numérico.
3_ Si la primera condición no se cumple, se pasa a la siguiente condición elif caracter[0].islower():. Esta condición verifica si el primer carácter del input 
está en minúscula utilizando el método islower(). Si es verdadera, se ejecuta la línea print(f"El carácter ingresado {caracter} está en 'minúsculas'."), que muestra en la pantalla 
un mensaje indicando que el carácter está en minúscula.
4_ Si ninguna de las dos condiciones anteriores se cumple, se pasa a la siguiente condición elif caracter[0].isupper():. Esta condición verifica si el primer carácter del input 
está en mayúscula utilizando el método isupper(). Si es verdadera, se ejecuta la línea print(f"El carácter ingresado {caracter} está en 'MAYÚSCULA'."), que muestra en la pantalla 
un mensaje indicando que el carácter está en mayúscula.
5_ Si ninguna de las tres condiciones anteriores se cumple, se ejecuta la línea else:, lo que significa que el carácter no es numérico, ni minúscula, ni mayúscula. En este caso, 
se muestra en la pantalla el mensaje print(f"El carácter ingresado {caracter} es 'especial'.").

En resumen, el programa solicita al usuario que ingrese un carácter y determina si es numérico, minúscula, mayúscula o especial utilizando los métodos isnumeric(), islower() e isupper(). 
Dependiendo de la condición cumplida, se mostrará un mensaje correspondiente en la pantalla.
"""