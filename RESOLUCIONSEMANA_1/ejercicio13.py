"""
SEMANA 1 EJERCICIO N° 13

13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
print(f"{nombre} en 10 años mas tendras la edad de: {edad + 10} años.")

"""
DETALLES DEL CODIGO:

1_ La línea nombre = input("Ingrese su nombre: ") solicita al usuario que ingrese su nombre y lo guarda en la variable nombre.
2_ La línea edad = int(input("Ingrese su edad: ")) solicita al usuario que ingrese su edad y lo convierte en un número entero utilizando la función int(). 
El resultado se guarda en la variable edad.
3_ La línea print(f"{nombre} en 10 años más tendrás la edad de: {edad + 10} años.") utiliza una f-string para imprimir en la pantalla un mensaje que muestra 
el nombre del usuario y su edad actual, y calcula la edad que tendrán en 10 años más. El resultado se muestra en el mensaje.

En resumen, el programa solicita al usuario que ingrese su nombre y edad, calcula la edad que tendrán en 10 años más y muestra el resultado en la pantalla junto con el nombre del usuario.
"""