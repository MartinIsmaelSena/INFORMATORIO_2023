"""
SEMANA 2 EJERCICIO N° 10

10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
una vocal o una consonante.

"""

letra_ingresada = input("Ingrese una sola letra: ")
letra_minuscula = letra_ingresada.lower()
if letra_minuscula in ['a', 'e', 'i', 'o', 'u']:
    print(f"La letra ingresada {letra_minuscula} es una vocal.")
else:
    print(f"La letra ingresada {letra_minuscula} es una consonante.")


"""
DETALLES DEL CODIGO:

1_ La línea letra_ingresada = input("Ingrese una sola letra: ") solicita al usuario que ingrese una letra y la guarda en la variable letra_ingresada.
2_ La línea letra_minuscula = letra_ingresada.lower() convierte la letra ingresada a minúscula utilizando el método lower(). Esto se hace para simplificar 
la verificación, ya que se comparará con letras minúsculas.
3_ La condición if letra_minuscula in ['a', 'e', 'i', 'o', 'u']: verifica si la letra ingresada se encuentra en la lista de vocales. La lista contiene las 
letras 'a', 'e', 'i', 'o' y 'u'. Si la letra ingresada está en la lista, significa que es una vocal.
4_ Si la condición se cumple, se ejecuta la línea print(f"La letra ingresada {letra_minuscula} es una vocal."), que muestra en la pantalla el mensaje indicando 
que la letra ingresada es una vocal.
5_ Si la condición no se cumple, es decir, la letra ingresada no está en la lista de vocales, se ejecuta el bloque else:. Esto significa que la letra ingresada 
es una consonante. En este caso, se ejecuta la línea print(f"La letra ingresada {letra_minuscula} es una consonante."), que muestra en la pantalla el mensaje 
indicando que la letra ingresada es una consonante.

En resumen, el programa permite al usuario ingresar una letra y luego verifica si es una vocal o una consonante. Dependiendo del resultado de la verificación, 
se muestra un mensaje apropiado en la pantalla.
"""