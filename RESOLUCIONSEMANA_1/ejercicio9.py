"""
SEMANA 1 EJERCICIO N° 9

9-Escribe un programa que solicite al usuario dos números y luego imprima la
suma, la resta, la multiplicación y la división de los dos números.
"""

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un segundo numero: "))
print(f"El resultado de las operaciones es:\nSuma:{num1+num2}\nResta: {num1-num2}\nMultiplicación:{num1*num2}\nDivisión:{num1/num2} ")

"""
DETALLES DEL CODIGO:

1_ La línea num1 = float(input("Ingrese un número: ")) solicita al usuario que ingrese un número y lo guarda en la variable num1. 
El float alrededor de input se utiliza para convertir la entrada del usuario en un número decimal.
2_ La línea num2 = float(input("Ingrese un segundo número: ")) solicita al usuario que ingrese un segundo número y lo guarda en la variable num2. 
Al igual que en el paso anterior, float se utiliza para convertir la entrada en un número decimal.
3_ La línea print(f"El resultado de las operaciones es:\nSuma: {num1+num2}\nResta: {num1-num2}\nMultiplicación: {num1*num2}\nDivisión: {num1/num2}") 
utiliza una f-string para imprimir en la pantalla un mensaje que muestra el resultado de varias operaciones aritméticas con los números ingresados. 
Se realiza la suma, resta, multiplicación y división de num1 y num2, y los resultados se interpolan en el mensaje.

En resumen, el programa solicita al usuario que ingrese dos números, realiza operaciones aritméticas básicas con ellos y muestra los resultados en la pantalla.
"""