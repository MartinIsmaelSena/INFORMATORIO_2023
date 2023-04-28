"""
SEMANA 2 GUIA N° 2 EJERCICIO N° 13

13-Crear una lista con los nombres de tres colores y agregar dos colores más al
final de la lista. Mostrar la lista resultante.
"""

lista_colores = ['Rojo', 'Blanco', 'Verde']
#nueva_lista = lista_colores + ['Violeta', 'Amarillo']
lista_colores.append('Violeta')
lista_colores.append('Amarillo')
print(f"La lista con los nuevos ingresos queda asi: {lista_colores}")

"""
DETALLES DEL CODIGO:

1_ Se define una lista llamada lista_colores que contiene diferentes nombres de colores.

2_ Se utiliza el método append() sobre la lista lista_colores dos veces para agregar nuevos elementos al final de la lista. El método append() se utiliza para añadir un elemento 
al final de una lista.

3_ Luego se utiliza la función print() junto con una f-string para mostrar en la consola el contenido de la lista lista_colores después de haber agregado los nuevos elementos. 
La f-string permite incluir la lista directamente en el mensaje a través de {}. El mensaje que se muestra es "La lista con los nuevos ingresos queda así:" seguido de los elementos 
de la lista lista_colores actualizada.

En resumen, este código crea una lista llamada lista_colores con diferentes nombres de colores, agrega los elementos 'Violeta' y 'Amarillo' al final de la lista utilizando el método 
append(), y luego muestra en la consola la lista actualizada con los nuevos elementos. La lista original lista_colores se modifica en el proceso y se agregan 'Violeta' y 'Amarillo' al 
final de la lista.
"""