"""
SEMANA 2 EJERCICIO N° 1

1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es
mayor de edad (18 años o más) o no.
"""
edad = int(input("Ingres su edad: "))

if edad >= 18:
    print(f"Usted con {edad} años de edad ya es mayor")
else:
    print(f"Usted con la edad de {edad} años aún es menor")

"""
DETALLES DEL CODIGO:

1_ La línea edad = int(input("Ingresa tu edad: ")) solicita al usuario que ingrese su edad y la convierte en un número entero utilizando la función int(). 
El resultado se guarda en la variable edad.
2_ La línea if edad >= 18: inicia una estructura condicional if que verifica si la edad ingresada es mayor o igual a 18.
3_ Si la condición es verdadera (es decir, si la edad es mayor o igual a 18), se ejecuta la línea print(f"Usted con {edad} años de edad ya es mayor"), que muestra 
en la pantalla un mensaje indicando que la persona es mayor de edad y muestra la edad ingresada.
4_ Si la condición es falsa (es decir, si la edad es menor a 18), se ejecuta la línea print(f"Usted con la edad de {edad} años aún es menor"), que muestra en la 
pantalla un mensaje indicando que la persona es menor de edad y muestra la edad ingresada.

En resumen, el programa solicita al usuario que ingrese su edad y luego muestra un mensaje en la pantalla indicando si la persona es mayor de edad o menor de edad, según la edad ingresada.
"""