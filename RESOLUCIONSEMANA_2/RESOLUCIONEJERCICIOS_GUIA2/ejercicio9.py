"""
SEMANA 2 GUIA N° 2 EJERCICIO N° 9

9-Crear una lista con los nombres de tres países y ordenar la lista en orden
alfabético. Mostrar la lista resultante.
"""

lista_paises = ['Uruguay', 'España', 'Argentina']
listapaises_ordenada = sorted(lista_paises)

print(f"La lista en orden alfabetico es: {listapaises_ordenada}")

"""
DETALLES DEL CODIGO:

1_ Se define una lista llamada lista_paises que contiene los nombres de diferentes países.

2_ Se utiliza la función sorted() para crear una nueva lista llamada listapaises_ordenada. La función sorted() toma la lista original lista_paises como argumento y 
devuelve una nueva lista con los elementos ordenados alfabéticamente. La lista original lista_paises no se modifica.

3_ Se utiliza la función print() junto con una f-string para mostrar en la consola el contenido de la lista listapaises_ordenada. La f-string permite incluir la lista 
directamente en el mensaje a través de {}. El mensaje que se muestra es "La lista en orden alfabético es:" seguido de los elementos de la lista listapaises_ordenada en su orden alfabético.

En resumen, este código crea una lista llamada lista_paises con los nombres de diferentes países, crea una nueva lista llamada listapaises_ordenada utilizando la función sorted() 
para ordenar alfabéticamente los elementos de la lista original, y luego muestra en la consola la lista listapaises_ordenada con los países ordenados alfabéticamente. 
La lista original lista_paises no se modifica en este proceso.
"""