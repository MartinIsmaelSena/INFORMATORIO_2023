"""
SEMANA 2 GUIA N° 2 EJERCICIO N° 14

14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los
elementos de la tupla.
"""

mi_tupla = (1,2,3,4,5)
suma_tupla = sum(mi_tupla)
print(f"La suma de la tupla es: {suma_tupla}")

"""
DETALLES DEL CODIGO:

1_ Se define una tupla llamada mi_tupla que contiene los valores numéricos del 1 al 5.

2_ Se utiliza la función sum() para sumar los elementos de la tupla mi_tupla. La función sum() toma como argumento un iterable, en este caso, la tupla mi_tupla. 
Suma todos los valores de la tupla y devuelve el resultado, que se guarda en la variable suma_tupla.

3_ Se utiliza la función print() junto con una f-string para mostrar en la consola el resultado de la suma. La f-string permite incluir el valor de la variable 
suma_tupla directamente en el mensaje a través de {}. El mensaje que se muestra es "La suma de la tupla es:" seguido del valor de suma_tupla.

En resumen, este código define una tupla llamada mi_tupla con los valores del 1 al 5, calcula la suma de los elementos de la tupla utilizando la función sum(), y 
luego muestra en la consola el resultado de la suma.
"""