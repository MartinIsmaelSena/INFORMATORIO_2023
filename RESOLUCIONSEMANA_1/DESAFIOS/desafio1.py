"""
SEMANA 1 DESAFIO N° 1

Desafío 1:
Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
sus ventas totales y el departamento comercial te solicita que ayudes a los
vendedores a calcular sus comisiones creando un programa que les pregunte su
nombre y cuánto han vendido en éste mes.
Tu programa le va a responder con una frase que incluya su nombre y el monto
que le corresponde por las comisiones
"""

nombre_empleado = input("Ingrese su nombre: ")
venta_total = float(input("Ingrese el monto total de ventas del mes: "))
comision = (venta_total / 100) * 6

print(f"El empleado {nombre_empleado}, con el total de venta ${venta_total} le corresponde:\nComisión: ${comision}")

"""
DETALLES DEL CODIGO:

1_ La línea nombre_empleado = input("Ingrese su nombre: ") solicita al usuario que ingrese su nombre y lo guarda en la variable nombre_empleado.
2_ La línea venta_total = float(input("Ingrese el monto total de ventas del mes: ")) solicita al usuario que ingrese el monto total de ventas del mes 
y lo convierte en un número decimal utilizando la función float(). El resultado se guarda en la variable venta_total.
3_ La línea comision = (venta_total / 100) * 6 calcula la comisión correspondiente al empleado. Divide el monto total de ventas entre 100 para obtener 
el 1%, y luego multiplica ese valor por 6 para obtener el 6% de comisión. El resultado se guarda en la variable comision.
4_ La línea print(f"El empleado {nombre_empleado}, con el total de venta ${venta_total} le corresponde:\nComisión: ${comision}") utiliza una f-string para 
imprimir en la pantalla un mensaje que muestra el nombre del empleado, el monto total de ventas ingresado y la comisión correspondiente.

En resumen, el programa solicita al usuario que ingrese su nombre y el monto total de ventas del mes. Luego, calcula la comisión (el 6% del monto total de ventas) 
y muestra el nombre del empleado, el monto total de ventas y la comisión correspondiente en la pantalla.
"""