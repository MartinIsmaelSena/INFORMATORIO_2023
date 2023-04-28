"""
SEMANA 2 GUIA N° 2 EJERCICIO N° 8

8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.
"""

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_num.reverse()
print(f"Mi lista al reverso es: {lista_num}")

"""
DETALLES DEL CODIGO:

1_ Se define una lista llamada lista_num que contiene los números del 1 al 10 en orden ascendente.

2_ Se utiliza el método reverse() sobre la lista lista_num. Este método invierte el orden de los elementos en la lista, modificándola directamente.

3_ Se utiliza la función print() junto con una f-string para mostrar en la consola el contenido de la lista lista_num después de haber aplicado el 
método reverse(). La f-string permite incluir la lista directamente en el mensaje a través de {}. El mensaje que se muestra es "Mi lista al reverso es:" 
seguido de los elementos de la lista lista_num en su nuevo orden invertido.

En resumen, este código crea una lista llamada lista_num con los números del 1 al 10 en orden ascendente, invierte el orden de los elementos en la lista 
utilizando el método reverse(), y luego muestra en la consola la lista resultante en su nuevo orden invertido.
"""