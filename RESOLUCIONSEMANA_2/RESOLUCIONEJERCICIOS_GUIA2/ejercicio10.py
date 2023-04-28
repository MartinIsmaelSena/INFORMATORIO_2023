"""
SEMANA 2 GUIA N° 2 EJERCICIO N° 10

10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la
lista. Mostrar la lista resultante.
"""

lista_frutas = ['Manzana', 'Naranja', 'Sandia']
print(f"La lista sin el elmento eliminado es: {lista_frutas}")
lista_frutas.pop(1)
print(f"La lista 'con' el elmento eliminado es: {lista_frutas}")

"""
DETALLES DEL CODIGO:

1_ Se define una lista llamada lista_frutas que contiene diferentes nombres de frutas.

2_ Se utiliza la función print() junto con una f-string para mostrar en la consola el contenido de la lista lista_frutas antes de eliminar un elemento. 
La f-string permite incluir la lista directamente en el mensaje a través de {}. El mensaje que se muestra es "La lista sin el elemento eliminado es:" seguido 
de los elementos de la lista lista_frutas.

3_ Se utiliza el método pop() sobre la lista lista_frutas para eliminar el elemento en el índice 1. En este caso, el elemento 'Naranja' es eliminado de la lista. 
El método pop() también devuelve el elemento eliminado, pero en este caso no se almacena en ninguna variable.

4_ Se utiliza nuevamente la función print() junto con una f-string para mostrar en la consola el contenido de la lista lista_frutas después de haber eliminado el elemento. 
El mensaje que se muestra es "La lista 'con' el elemento eliminado es:" seguido de los elementos de la lista lista_frutas actualizada.

En resumen, este código crea una lista llamada lista_frutas con diferentes nombres de frutas, muestra en la consola la lista original, elimina el elemento en el índice 1 utilizando 
el método pop(), y luego muestra en la consola la lista actualizada después de haber eliminado el elemento. La lista original lista_frutas se modifica en el proceso y el elemento 'Naranja' 
es eliminado de la lista.
"""