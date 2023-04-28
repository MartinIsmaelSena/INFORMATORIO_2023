"""
SEMANA 1 EJERCICIO N° 10

10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
euros.
Supón que el tipo de cambio es de 0.84 euros por dólar.
"""
dolar = float(input("Ingrese la cantidad de dolares para el cambio: "))
euro = 0.84
print(f"Con {dolar} USD, usted recibiria un total en Euros:  {dolar * euro}€")

"""
DETALLES DEL CODIGO:

1_ La línea dolar = float(input("Ingrese la cantidad de dólares para el cambio: ")) solicita al usuario que ingrese la cantidad de dólares que desea convertir y la guarda en la variable dolar. 
El float alrededor de input se utiliza para convertir la entrada del usuario en un número decimal.
2_ La línea euro = 0.84 define la variable euro y le asigna el valor de 0.84. Este valor representa el factor de conversión de dólares a euros.
3_ La línea print(f"Con {dolar} USD, usted recibiría un total en Euros: {dolar * euro}€") utiliza una f-string para imprimir en la pantalla un mensaje que muestra 
la cantidad de dólares ingresados por el usuario y el equivalente en euros. La cantidad de dólares se multiplica por el factor de conversión euro, y el resultado se muestra en el mensaje.

En resumen, el programa solicita al usuario que ingrese una cantidad de dólares, realiza la conversión a euros utilizando un factor de conversión específico y 
muestra el resultado en la pantalla.
"""