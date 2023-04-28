"""
SEMANA 1 DESAFIO N° 2

Desafío 2:
Escribe un programa que solicite al usuario su información personal, incluyendo
su nombre completo, edad, estatura, peso, dirección y número de teléfono.
A continuación, el programa deberá imprimir un mensaje con los datos
ingresados por el usuario en el siguiente formato:
La información ingresada es la siguiente:
Nombre completo: [nombre completo]
Edad: [edad]
Estatura: [estatura] cm
Peso: [peso] kg
Dirección: [dirección]
Número de teléfono: [número de teléfono]
"""

print("INGRESA LOS SIGUIENTES DATOS SOLICITADOS: ")
nombre_completo = input("Nombre y apellido completo: ")
edad = input("Ingresa edad actual: ")
estatura = input("Ingresa tu estatura: ")
peso = input("Ingresa tu peso actual: ")
direcc = input("Ingresa tu direccion: ")
num_tel = input("Ingresa tu numero de telefono: ")

print("\nDATOS INGRESADOS: ")
print(f"Nombre completo: [{nombre_completo}]\nEdad: [{edad}]\nEstatura: [{estatura}]\nPeso: [{peso}]\nDirección: [{direcc}]\nNumero de telefono: [{num_tel}]")

"""
DETALLES DEL CODIGO:

1_ La línea print("INGRESA LOS SIGUIENTES DATOS SOLICITADOS: ") muestra en la pantalla un mensaje indicando al usuario que ingrese los datos solicitados.
2_ La línea nombre_completo = input("Nombre y apellido completo: ") solicita al usuario que ingrese su nombre y apellido completo y lo guarda en la variable nombre_completo.
3_ La línea edad = input("Ingresa edad actual: ") solicita al usuario que ingrese su edad actual y la guarda en la variable edad.
4_ La línea estatura = input("Ingresa tu estatura: ") solicita al usuario que ingrese su estatura y la guarda en la variable estatura.
5_ La línea peso = input("Ingresa tu peso actual: ") solicita al usuario que ingrese su peso actual y lo guarda en la variable peso.
6_ La línea direcc = input("Ingresa tu dirección: ") solicita al usuario que ingrese su dirección y la guarda en la variable direcc.
7_ La línea num_tel = input("Ingresa tu número de teléfono: ") solicita al usuario que ingrese su número de teléfono y lo guarda en la variable num_tel.
8_ La línea print("\nDATOS INGRESADOS: ") muestra en la pantalla un mensaje indicando que se mostrarán los datos ingresados por el usuario.
9_ La línea print(f"Nombre completo: [{nombre_completo}]\nEdad: [{edad}]\nEstatura: [{estatura}]\nPeso: [{peso}]\nDirección: [{direcc}]\nNumero de telefono: [{num_tel}]") 
utiliza f-strings para imprimir en la pantalla los datos ingresados por el usuario. Cada dato se muestra en una línea separada y se muestra entre corchetes para resaltar su valor.

En resumen, el programa solicita al usuario que ingrese varios datos personales y luego muestra los datos ingresados en la pantalla en un formato legible.
"""
