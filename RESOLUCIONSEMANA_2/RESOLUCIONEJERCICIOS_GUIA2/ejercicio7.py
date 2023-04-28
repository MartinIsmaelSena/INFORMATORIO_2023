"""
SEMANA 2 GUIA N° 2 EJERCICIO N° 7

7-Crear un diccionario con los nombres de tres ciudades y sus respectivas
poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva
población. Mostrar el diccionario resultante.

"""

ciudad_poblacion = {'Neuquen': 726590, 'Cordoba': 2420052, 'El Calafate': 125000}
ciudad_poblacion.update({'Posadas': 379000})

print(f"Ciudades con sus respectivas poblaciones: {ciudad_poblacion}")

"""
DETALLES DEL CODIGO:

1_ Se define un diccionario llamado ciudad_poblacion que contiene información sobre la población de diferentes ciudades. Cada ciudad se representa como una clave y 
su respectiva población se representa como el valor asociado a esa clave. En este caso, las ciudades son 'Neuquen', 'Cordoba' y 'El Calafate', y sus poblaciones respectivas 
son 726590, 2420052 y 125000.

2_ Se utiliza el método update() para agregar una nueva entrada al diccionario ciudad_poblacion. En este caso, se agrega la ciudad 'Posadas' con su respectiva población de 379000. 
La función update() toma como argumento otro diccionario que contiene las nuevas claves y valores a agregar al diccionario existente.

3_ Se utiliza la función print() junto con una f-string para mostrar en la consola el diccionario ciudad_poblacion completo. La f-string permite incluir el diccionario directamente 
en el mensaje a través de {}. El mensaje que se muestra es "Ciudades con sus respectivas poblaciones:" seguido del contenido actualizado del diccionario ciudad_poblacion.

En resumen, este código crea un diccionario llamado ciudad_poblacion con información sobre la población de diferentes ciudades, agrega una nueva ciudad y su población utilizando el 
método update(), y luego muestra el diccionario completo en la consola.
"""