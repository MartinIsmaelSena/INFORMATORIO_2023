"""
SEMANA 1 EJERCICIO N° 15

15-Escribe un programa que solicite al usuario una temperatura en grados
Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.
"""

temp_c = float(input("Ingrese la temperatura en grados Celsius: "))
calc_fah = (temp_c * 1.8) + 32
print(f"El valor ingresado en Celsius {temp_c} es equivalente en grados Fahrenheit: {calc_fah}")

"""
DETALLES DEL CODIGO:

1_ La línea temp_c = float(input("Ingrese la temperatura en grados Celsius: ")) solicita al usuario que ingrese una temperatura en grados Celsius y la convierte 
en un número decimal utilizando la función float(). El resultado se guarda en la variable temp_c.
2_ La línea calc_fah = (temp_c * 1.8) + 32 realiza el cálculo de conversión de grados Celsius a grados Fahrenheit. 
Multiplica la temperatura en grados Celsius por 1.8 y luego le suma 32. El resultado se guarda en la variable calc_fah.
3_ La línea print(f"El valor ingresado en Celsius {temp_c} es equivalente en grados Fahrenheit: {calc_fah}") utiliza una f-string para imprimir en la pantalla un 
mensaje que muestra el valor ingresado por el usuario en grados Celsius y su equivalente en grados Fahrenheit, que se calculó previamente.

En resumen, el programa solicita al usuario que ingrese una temperatura en grados Celsius, realiza la conversión a grados Fahrenheit utilizando la fórmula correspondiente 
y muestra el resultado en la pantalla junto con el valor ingresado en Celsius.
"""