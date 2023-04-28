"""
SEMANA 1 EJERCICIO N° 8

8-Crea un programa que pida al usuario el radio de un círculo y muestre su
diámetro, su circunferencia y su área.
Supón que pi es aproximadamente 3.14159.
"""

radio = float(input("Ingrese el radio del circulo: "))
pi = 3.1416
diametro = radio * 2
circunf = pi * diametro
area = pi * radio**2

print(f"Con el radio ingresado: {radio}, calculamos su diametro que es: {diametro},\n su circunferencia: {circunf}\n y el valor de su area: {area} ")

"""
DETALLES DEL CODIGO:

1_ La línea radio = float(input("Ingrese el radio del círculo: ")) solicita al usuario que ingrese el valor del radio del círculo y lo guarda en la variable radio. 
El float alrededor de input se utiliza para convertir la entrada del usuario en un número decimal.
2_ La línea pi = 3.1416 define la variable pi y le asigna el valor de aproximadamente 3.1416. 
Esta es una aproximación del número pi, que se utiliza para los cálculos relacionados con el círculo.
3_ La línea diametro = radio * 2 calcula el diámetro del círculo multiplicando el valor del radio por 2. El diámetro de un círculo es el doble de su radio.
4_ La línea circunf = pi * diametro calcula la circunferencia del círculo utilizando la fórmula: circunferencia = pi * diámetro. 
En este caso, el valor del diámetro se guarda en la variable diametro y el resultado se guarda en la variable circunf.
5_ La línea area = pi * radio**2 calcula el área del círculo utilizando la fórmula: área = pi * radio al cuadrado. 
En este caso, el valor del radio se guarda en la variable radio y el resultado se guarda en la variable area.
6_ La última línea utiliza una f-string para imprimir en la pantalla un mensaje que muestra el radio ingresado por el usuario, el diámetro calculado, la circunferencia y el área del círculo. 
Los valores de las variables se interpolan en el mensaje.

En resumen, el programa solicita al usuario que ingrese el valor del radio de un círculo, calcula su diámetro, circunferencia y área, y muestra los resultados en la pantalla.
"""