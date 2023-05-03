"""
Desafío 2: Analizador de textos
Requisitos técnicos:
Se te pide crear un programa que le pida al usuario que ingresar un texto
cualquiera, por ejemplo, un artículo o una frase.
Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
elección.
Nuestro código va a procesar esa información para realizar los análisis
necesarios para devolverle al usuario la siguiente información:
1- Cantidad de veces que aparece cada una de letras que eligió.
Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
string
Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
minúscula.
2- Cuantas palabras hay en total en todo el texto.
Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
3- Cual es la primera letra y cuál es la última. (Indexación)
4- Mostrar el texto en orden inverso.
5- Decir si la palabra "python" aparece en el texto.
Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
string para mostrar al usuario

"""
#PRIMERA PARTE
print("==============================")
print("DESAFIO 2: ANALIZADOR DE TEXTO")
print("==============================")

texto = input("Ingrese el texto para analizar: ")
print("A continuación, ingrese 3 letras para su análisis")
letras = []
letras.append(input("Ingrese letra 1: ".lower()))
letras.append(input("Ingrese letra 2: ".lower()))
letras.append(input("Ingrese letra 3: ".lower()))
print("\n")

#SEGUNDA PARTE
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print("CANTIDAD DE LETRAS")
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")
print("\n")

#TERCERA PARTE
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")
print("\n")

#CUARTA PARTE
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")
print("\n")

#QUINTA PARTE
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")
print("\n")

#SEXTA PARTE
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")

print("===================================================")
print("MUCHAS GRACIAS POR USAR NUESTRO ANALIZADOR DE TEXTO")
print("===================================================")

"""
DETALLES DEL CODIGO:

#PRIMERA PARTE
Estas líneas imprimen utilizando -print()- una línea de igualdad y luego el título "DESAFÍO 2: ANALIZADOR DE TEXTO" rodeado por líneas de igualdad para crear un encabezado visualmente atractivo.
Luego, a traves de un -imput()- se solicita al usuario que ingrese el texto que desea analizar y lo guarda en la variable texto.
En las lineas del 33 al 36 se solicitan al usuario que ingrese tres letras para analizar. Cada letra ingresada se convierte a minúsculas utilizando el método lower() y se agrega a la lista letras 
que en primera instancia se encuentra vacia. También se imprime un salto de línea para separar visualmente las secciones del análisis.

#SEGUNDA PARTE
En las lineas 39 al 41 cuentan la cantidad de veces que aparece cada letra ingresada en el texto utilizando el método count(). Los resultados se guardan en las variables cantidad_letras1, cantidad_letras2 
y cantidad_letras3.
Despues las mismas se imprimen linea 43 a 45 la cantidad de veces que se encontraron las letras ingresadas en el texto, utilizando f-strings para formatear la salida. También se imprime un salto de línea 
para separar visualmente las secciones del análisis.

#TERCERA PARTE
Estas líneas cuentan la cantidad de palabras en el texto. Primero, el texto se divide en palabras utilizando el método split(), que divide el texto en cada espacio en blanco. Luego, se utiliza la 
función len() para obtener la longitud de la lista de palabras y se imprime el resultado. También se imprime un salto de línea para separar visualmente las secciones del análisis.

#CUARTA PARTE
Estas líneas obtienen la primera letra y la última letra del texto utilizando el indexado de cadena. La primera letra se obtiene utilizando texto[0] y la última letra se obtiene utilizando 
texto[-1]. Luego, se imprimen las letras inicial y final

#QUINTA PARTE
Estas líneas imprimen el encabezado "TEXTO INVERTIDO". Luego, se invierte el orden de las palabras en la lista palabras utilizando el método reverse(). Después, se utiliza el método join() 
para unir las palabras de la lista en una sola cadena, separadas por un espacio en blanco. La cadena resultante se guarda en la variable texto_invertido. Finalmente, se imprime un mensaje 
que muestra el texto invertido.

#SEXTA PARTE
Estas líneas imprimen el encabezado "BUSCANDO LA PALABRA PYTHON". Luego, se verifica si la palabra "python" está presente en el texto utilizando el operador in. El resultado de esta verificación 
(True o False) se guarda en la variable buscar_python. Después, se crea un diccionario llamado dic que tiene como clave True y False y como valor las cadenas "sí" y "no", respectivamente. 
Finalmente, se imprime un mensaje indicando si la palabra "Python" se encuentra en el texto, utilizando el diccionario dic para mostrar el resultado correspondiente.
"""