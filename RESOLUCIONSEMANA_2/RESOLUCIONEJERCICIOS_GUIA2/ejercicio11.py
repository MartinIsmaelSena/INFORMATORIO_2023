"""
SEMANA 2 GUIA N° 2 EJERCICIO N° 11

11-Crear una lista con los nombres de tres animales y agregar una cuarta animal
al principio de la lista. Mostrar la lista resultante.
"""

lista_animales = ['Caballo', 'Gato', 'Perro']
lista_animales.insert(0, 'Oveja')
print(f"La lista con el elemento ingresado: {lista_animales}")

"""
DETALLES DEL CODIGO:

1_ Se define una lista llamada lista_animales que contiene diferentes nombres de animales.

2_ Se utiliza el método insert() sobre la lista lista_animales. El método insert() se utiliza para insertar un elemento en una posición específica de la lista. 
En este caso, se inserta el elemento 'Oveja' en la posición 0, es decir, al principio de la lista.

3_ Se utiliza la función print() junto con una f-string para mostrar en la consola el contenido de la lista lista_animales después de haber insertado el nuevo elemento. 
La f-string permite incluir la lista directamente en el mensaje a través de {}. El mensaje que se muestra es "La lista con el elemento ingresado:" seguido de los elementos 
de la lista lista_animales actualizada.

En resumen, este código crea una lista llamada lista_animales con diferentes nombres de animales, inserta el elemento 'Oveja' al principio de la lista utilizando el método 
insert(), y luego muestra en la consola la lista actualizada con el nuevo elemento. La lista original lista_animales se modifica en el proceso y el elemento 'Oveja' se agrega 
al principio de la lista.
"""