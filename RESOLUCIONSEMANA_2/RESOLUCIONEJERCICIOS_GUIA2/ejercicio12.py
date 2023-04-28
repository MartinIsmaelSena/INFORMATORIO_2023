"""
SEMANA 2 GUIA N° 2 EJERCICIO N° 12

12-Crear una lista con los nombres de tres países y reemplazar el segundo país de
la lista por otro país. Mostrar la lista resultante.
"""

lista_paises = ['Uruguay', 'España', 'Argentina']
print(f"La lista sin actualizar: {lista_paises}")
lista_paises.pop(1)
lista_paises.insert(1, 'Brazil')

print(f"La lista actualizada: {lista_paises}")

"""
DETALLES DEL CODIGO:

1_ Se define una lista llamada lista_paises que contiene diferentes nombres de países.

2_ Se utiliza la función print() junto con una f-string para mostrar en la consola el contenido de la lista lista_paises antes de realizar ninguna modificación. 
La f-string permite incluir la lista directamente en el mensaje a través de {}. El mensaje que se muestra es "La lista sin actualizar:" seguido de los elementos de la lista lista_paises.

3_ Se utiliza el método pop() sobre la lista lista_paises para eliminar el elemento en el índice 1, que es 'España'. El método pop() también devuelve el elemento eliminado, 
pero en este caso no se almacena en ninguna variable.

4_ Se utiliza el método insert() sobre la lista lista_paises para insertar el elemento 'Brazil' en la posición 1, que corresponde al índice que había quedado vacío tras la eliminación de 'España'.

5_ Se utiliza nuevamente la función print() junto con una f-string para mostrar en la consola el contenido de la lista lista_paises después de haber realizado las modificaciones. 
El mensaje que se muestra es "La lista actualizada:" seguido de los elementos de la lista lista_paises actualizada.

En resumen, este código crea una lista llamada lista_paises con diferentes nombres de países, muestra en la consola la lista original, elimina el elemento en el índice 1 utilizando 
el método pop(), inserta el elemento 'Brazil' en la posición 1 utilizando el método insert(), y luego muestra en la consola la lista actualizada. La lista original lista_paises se 
modifica en el proceso, se elimina 'España' y se agrega 'Brazil' en su lugar.
"""