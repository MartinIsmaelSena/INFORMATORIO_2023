"""
SEMANA 1 EJERCICIO N° 18

18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de
residencia, y lo muestre en pantalla Utilizando una sola línea de código.
*Recuerda el print() del ejercicio anterior
"""
nombre = input("Ingresa tu 'Nombre': ")
edad = input("Ingresa tu 'Edad': ")
ciudad = input("Ingresa tu 'Ciudad': ")
print(f"DATOS INGRESADOS: \nNombre:{nombre}\nEdad:{edad}\nCiudad:{ciudad}")

"""
DETALLES DEL CODIGO:

1_ La línea nombre = input("Ingresa tu 'Nombre': ") solicita al usuario que ingrese su nombre y lo guarda en la variable nombre.
2_ La línea edad = input("Ingresa tu 'Edad': ") solicita al usuario que ingrese su edad y la guarda en la variable edad.
3_ La línea ciudad = input("Ingresa tu 'Ciudad': ") solicita al usuario que ingrese su ciudad y la guarda en la variable ciudad.
4_ La línea print(f"DATOS INGRESADOS: \nNombre:{nombre}\nEdad:{edad}\nCiudad:{ciudad}") utiliza una f-string para imprimir en la pantalla un mensaje 
que muestra los datos ingresados por el usuario. Cada dato se muestra en una línea separada utilizando el carácter de escape \n para crear saltos de línea.

En resumen, el programa solicita al usuario que ingrese su nombre, edad y ciudad, y luego muestra los datos ingresados en la pantalla en un formato legible.
"""