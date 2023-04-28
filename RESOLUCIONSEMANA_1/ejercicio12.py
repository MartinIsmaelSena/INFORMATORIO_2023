"""
SEMANA 1 EJERCICIO N° 12

12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
dd/mm/aaaa y luego imprima su edad en años.
Utiliza la función .split()
"""
fecha_cumpleanio = input("Ingrese su fecha de cumpleaños separado por '/': ")
dia, mes, anio = fecha_cumpleanio.split("/")
edad_actual = 2023 - int(anio)
print(f"Su edad actual es: {edad_actual} años")

"""
DETALLES DEL CODIGO:

1_ La línea fecha_cumpleanio = input("Ingrese su fecha de cumpleaños separado por '/': ") solicita al usuario que ingrese su fecha de cumpleaños y la guarda en la variable fecha_cumpleanio.
2_ La línea dia, mes, anio = fecha_cumpleanio.split("/") divide la cadena fecha_cumpleanio en tres partes utilizando el carácter '/' como separador. 
Luego, asigna cada parte a las variables dia, mes y anio, respectivamente.
3_ La línea edad_actual = 2023 - int(anio) calcula la edad actual del usuario restando el año de nacimiento (convertido a un número entero utilizando int()) del año actual, 
que es 2023 en este caso. El resultado se guarda en la variable edad_actual.
4_ La línea print(f"Su edad actual es: {edad_actual} años") utiliza una f-string para imprimir en la pantalla un mensaje que muestra la edad actual del usuario en años. 
El valor de la variable edad_actual se interpola en el mensaje.

En resumen, el programa solicita al usuario que ingrese su fecha de cumpleaños, calcula su edad actual en años y muestra el resultado en la pantalla.
"""