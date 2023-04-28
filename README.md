<p align="center">
  <img src="https://media.giphy.com/media/iIqmM5tTjmpOB9mpbn/giphy.gif" />
</p>
<h1 align="center"><b>ETAPA2: DESARROLLO WEB</b></h1>
<p align="center">
  <a href="http://example.net/](https://empleo.chaco.gob.ar/cenit#/">INFORMATORIO</a> 
</p>

<h1 align="center">Semana 1: Introducción a Python</h1>
<p>La programación en Python es una forma de comunicación con una computadora utilizando un lenguaje de programación llamado Python. Python es un lenguaje de programación poderoso y versátil que es ampliamente utilizado en el campo de la programación debido a su simplicidad y legibilidad.

Una de las características distintivas de Python es su sintaxis clara y concisa, lo que lo hace ideal tanto para principiantes como para programadores experimentados. Con Python, puedes escribir programas que realicen una amplia variedad de tareas, desde simples cálculos matemáticos hasta el desarrollo de aplicaciones web complejas.

Python es un lenguaje interpretado, lo que significa que no es necesario compilar el código antes de ejecutarlo. Esto facilita mucho el proceso de desarrollo, ya que puedes probar y depurar tu código de forma rápida y sencilla.

Además, Python cuenta con una amplia gama de bibliotecas y módulos que puedes utilizar para ampliar las funcionalidades del lenguaje. Estas bibliotecas te permiten realizar tareas específicas sin tener que escribir todo el código desde cero, lo que acelera el desarrollo de tus proyectos.

Python se utiliza en diversos campos, como el desarrollo de aplicaciones, el análisis de datos, la inteligencia artificial y la ciencia de datos. Su popularidad se debe en parte a su enfoque en la legibilidad del código, lo que facilita la colaboración y el mantenimiento de proyectos a largo plazo.</p>
**libro:** [**Python Crash Course**](https://www.amazon.com/Python-Crash-Course-2nd-Edition/dp/1593279280) ***Eric Matthes*** 

---

<h2>Variables y tipos de datos</h2>
<p>En Python, una variable es un contenedor que almacena valores. Puedes asignar diferentes tipos de datos a las variables en Python. Aquí tienes algunos ejemplos de variables y los tipos de datos que pueden contener:</p>

```
# Variables numéricas
edad = 25                # Entero (int)
altura = 1.75            # Flotante (float)

# Variables de texto
nombre = "Juan"          # Cadena de caracteres (str)
apellido = 'Pérez'       # Cadena de caracteres (str)

# Variables booleanas
es_estudiante = True     # Booleano (bool)
tiene_licencia = False   # Booleano (bool)

# Variables de lista
numeros = [1, 2, 3, 4]              # Lista (list)
nombres = ['Juan', 'María', 'Pedro'] # Lista (list)

# Variables de tupla
coordenadas = (10, 20)               # Tupla (tuple)
colores = ('rojo', 'verde', 'azul')  # Tupla (tuple)

# Variables de conjunto
frutas = {'manzana', 'banana', 'naranja'}   # Conjunto (set)
vocales = {'a', 'e', 'i', 'o', 'u'}          # Conjunto (set)

# Variables de diccionario
persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}   # Diccionario (dict)
producto = {'nombre': 'Camisa', 'precio': 25.99, 'stock': 10}  # Diccionario (dict)

```

* Convertir a int()
<p>En Python, puedes convertir un valor a tipo entero utilizando la función int(). Esta función toma como argumento un valor y lo convierte a un entero si es posible. Aquí tienes algunos ejemplos de cómo convertir valores a tipo entero:</p>

```
# Convertir un número en formato de cadena a entero
numero_cadena = "25"
numero_entero = int(numero_cadena)
print(numero_entero)  # Resultado: 25

# Convertir un número en formato de punto flotante a entero
numero_flotante = 3.14
numero_entero = int(numero_flotante)
print(numero_entero)  # Resultado: 3

# Convertir una cadena que representa un número octal a entero
numero_octal = "0o10"
numero_entero = int(numero_octal, 8)
print(numero_entero)  # Resultado: 8

# Convertir una cadena que representa un número binario a entero
numero_binario = "0b1010"
numero_entero = int(numero_binario, 2)
print(numero_entero)  # Resultado: 10

# Convertir un valor booleano a entero
valor_booleano = True
numero_entero = int(valor_booleano)
print(numero_entero)  # Resultado: 1
```
* Float()
<p>En Python, el tipo de dato float se utiliza para representar números de punto flotante, es decir, números con decimales. Estos números se almacenan internamente en formato de coma flotante de acuerdo con el estándar IEEE 754.
Aquí tienes algunos ejemplos de cómo trabajar con el tipo de dato float en Python:</p>

```
# Declarar variables float
pi = 3.14159
precio = 9.99
temperatura = -10.5

# Realizar operaciones con números float
suma = 2.5 + 3.7
resta = 10.0 - 4.2
multiplicacion = 5.3 * 2.0
division = 9.8 / 2.5

# Imprimir resultados
print(suma)             # Resultado: 6.2
print(resta)            # Resultado: 5.8
print(multiplicacion)   # Resultado: 10.6
print(division)         # Resultado: 3.92

# Redondear números float
numero = 3.14159
numero_redondeado = round(numero, 2)
print(numero_redondeado)  # Resultado: 3.14

# Convertir un número entero a float
numero_entero = 10
numero_float = float(numero_entero)
print(numero_float)  # Resultado: 10.0
```

* Booleanos

<p>En Python, el tipo de dato booleano (bool) se utiliza para representar valores lógicos. Puede tener dos posibles valores: True (verdadero) o False (falso). Los booleanos son fundamentales en la programación, ya que se utilizan en estructuras de control como condicionales y bucles para la toma de decisiones.
Aquí hay algunos aspectos importantes sobre los booleanos en Python:</p>

1. Valores **True** y **False**: Los booleanos **True** y **False** representan los dos únicos valores posibles de un objeto booleano. True indica que una condición es verdadera y False indica que una condición es falsa.
2. Operadores de comparación: Puedes utilizar operadores de comparación para evaluar expresiones y obtener un valor booleano como resultado. Algunos operadores de comparación comunes son:
* '==' (igual a): verifica si dos valores son iguales.
* '!=' (diferente de): verifica si dos valores no son iguales.
* '>' (mayor que): verifica si un valor es mayor que otro.
* '<' (menor que): verifica si un valor es menor que otro.
* '>=' (mayor o igual que): verifica si un valor es mayor o igual que otro.
* '<=' (menor o igual que): verifica si un valor es menor o igual que otro.
3. Operadores lógicos: Los operadores lógicos se utilizan para combinar expresiones booleanas y obtener un nuevo valor booleano. Los operadores lógicos más comunes son:
* 'and' (y): devuelve True si ambas expresiones son verdaderas.
* 'or' (o): devuelve True si al menos una de las expresiones es verdadera.
* 'not' (no): invierte el valor booleano de una expresión.
4. Valores booleanos en condiciones: Los booleanos son comúnmente utilizados en condiciones, como en los bloques if, elif y while, para ejecutar o saltar secciones de código según el valor de verdad de una expresión booleana.

Aquí unos ejemplos del uso de booleanos en Python:

```
# Declarar variables booleanas
es_estudiante = True
tiene_licencia = False

# Utilizar operadores de comparación
edad = 18
es_mayor_de_edad = edad >= 18

# Utilizar operadores lógicos
puede_conducir = es_estudiante and tiene_licencia
puede_votar = es_mayor_de_edad or tiene_licencia
no_es_estudiante = not es_estudiante

# Utilizar booleanos en condiciones
if es_estudiante:
    print("El usuario es estudiante")
elif no_es_estudiante:
    print("El usuario no es estudiante")
else:
    print("No se tiene información sobre si el usuario es estudiante")

```

* Cadena de caracteres o Strings

<p>En Python, una cadena de caracteres (string) es una secuencia de caracteres encerrados entre comillas simples ('') o comillas dobles (""). Las cadenas de caracteres se utilizan para representar texto y se pueden manipular de varias formas.
Aquí hay algunos aspectos importantes sobre las cadenas de caracteres en Python según Eric Matthes:</p>

1. Declaración de cadenas de caracteres: Puedes declarar una cadena de caracteres asignando un valor entre comillas a una variable. Por ejemplo:

```
mensaje = "Hola, Python!"

```
2. Acceso a caracteres: Puedes acceder a caracteres individuales en una cadena utilizando índices. Los índices en Python comienzan desde 0. Por ejemplo:

```
mensaje = "Hola, Python!"
primer_caracter = mensaje[0]  # 'H'

```
3. Concatenación de cadenas: Puedes combinar dos o más cadenas utilizando el operador de suma (+). Esto se conoce como concatenación de cadenas. Por ejemplo:

```
saludo = "Hola"
nombre = "Juan"
mensaje = saludo + " " + nombre  # "Hola Juan"

```
4. Métodos de cadenas: Python proporciona varios métodos incorporados para manipular cadenas. Algunos métodos comunes son:
* **upper()**: Convierte la cadena a mayúsculas.
* **lower()**: Convierte la cadena a minúsculas.
* **len()**: Devuelve la longitud de la cadena.
* **split()**: Divide la cadena en una lista de subcadenas según un delimitador.c
* **split()**: Divide la cadena en una lista de subcadenas según un delimitador.

5. Formateo de cadenas: Puedes utilizar el método format() o las f-strings (cadenas literales formateadas) para insertar valores variables en una cadena. Por ejemplo:

```
nombre = "Juan"
edad = 25
mensaje = "Hola, mi nombre es {} y tengo {} años".format(nombre, edad)
mensaje_fstring = f"Hola, mi nombre es {nombre} y tengo {edad} años"

```

Aquí tienes más ejemplos que muestran algunos conceptos de las cadenas de caracteres en Python:

```
# Declarar una cadena de caracteres
mensaje = "Hola, Python!"

# Acceder a caracteres individuales
primer_caracter = mensaje[0]  # 'H'

# Concatenar cadenas
nombre = "Juan"
saludo = "¡Hola, " + nombre + "!"

# Utilizar métodos de cadenas
mensaje = "   Hola, Python!   "
longitud = len(mensaje)  # 17
mensaje_mayusculas = mensaje.upper()  # "   HOLA, PYTHON!   "
mensaje_minusculas = mensaje.lower()  # "   hola, python!   "
palabras = mensaje.split()  # ['Hola,', 'Python!']
mensaje_sin_espacios = mensaje.strip()  # "Hola, Python!"

# Formateo de cadenas
nombre = "Juan"
edad = 25
mensaje = "Hola, mi nombre es {} y tengo {} años".format(nombre, edad)

```

* Datos mutables e inmutables

<p>En Python, los objetos se clasifican en dos categorías: mutables e inmutables. Esta clasificación se refiere a la capacidad de un objeto para cambiar después de haber sido creado.</p>

1. Datos inmutables: Los objetos inmutables son aquellos cuyo valor no puede ser modificado una vez que han sido creados. Cada vez que realizas una operación que parece modificar un objeto inmutable, en realidad estás creando un nuevo objeto. Algunos ejemplos de datos inmutables en Python son:

* Números enteros (int), números de punto flotante (float), números complejos (complex).
* Valores booleanos (bool), como **True** y **False**.
* Cadenas de caracteres (str).
* Tuplas (tuple).

2. Datos mutables: Los objetos mutables son aquellos que pueden cambiar su valor o contenido después de haber sido creados. Esto significa que puedes modificar directamente el objeto sin necesidad de crear uno nuevo. Algunos ejemplos de datos mutables en Python son:

* Listas (list).
* Conjuntos (set).
* Diccionarios (dict).

Aquí tienes unos ejemplos que muestran la diferencia entre datos mutables e inmutables:

```
# Datos inmutables
nombre = "Juan"   # Cadena de caracteres (str)
edad = 30         # Entero (int)

nombre = "María"  # Se crea un nuevo objeto de cadena (str)
edad = edad + 1   # Se crea un nuevo objeto de entero (int)

# Datos mutables
lista = [1, 2, 3]     # Lista (list)
diccionario = {'a': 1, 'b': 2}   # Diccionario (dict)

lista.append(4)     # Modifica la lista existente
diccionario['c'] = 3   # Modifica el diccionario existente

```

<p>En el ejemplo anterior, cuando modificamos los datos inmutables, como cambiar el valor de nombre o incrementar edad, se crean nuevos objetos en lugar de modificar los objetos originales. En cambio, cuando modificamos los datos mutables, como agregar un elemento a la lista lista o modificar un valor en el diccionario diccionario, el objeto existente se modifica directamente.
Es importante tener en cuenta la distinción entre datos mutables e inmutables, ya que puede afectar el comportamiento de tu código y la forma en que manipulas y pasas datos entre variables y funciones.</p>

**EJERCICIOS Y DESAFIOS:** [**SEMANA 1 -Resultos paso a paso-**](https://github.com/MartinIsmaelSena/INFORMATORIO_2023/tree/master/RESOLUCIONSEMANA_1) 
*by: Martin Ismael Sena*


---

<h1 align="center">Semana 2: Estructuras de Control de Flujo y Estructuras de datos</h1>

<p>Las estructuras de control son fundamentales en la programación, ya que nos permiten tomar decisiones y ejecutar diferentes acciones en función de ciertas condiciones. Estas estructuras son herramientas poderosas que nos permiten crear programas más dinámicos e interactivos.</p>

<h2>Condicionales</h2>

<p>Eric Matthes resalta la importancia de entender y crear condiciones lógicas para que los condicionales funcionen correctamente. Explica cómo combinar operadores lógicos, como "and" (y), "or" (o) y "not" (no), para formar expresiones condicionales más complejas. Además, Matthes enfatiza la importancia de la indentación y el uso adecuado de los bloques de código dentro de las estructuras condicionales, lo que ayuda a mantener la legibilidad y comprensión del código.</p>

* Condicionale simple: IF(SI)

<p>Una estructura de control simple que podemos explorar, tomando como referencia a Eric Matthes, es la instrucción "if". Esta estructura permite ejecutar un bloque de código si una condición dada es verdadera. Eric Matthes, en su enfoque didáctico, ha explicado esta estructura de manera clara y accesible.
La instrucción "if" se compone de la palabra clave "if", seguida de una expresión condicional entre paréntesis y un bloque de código que se ejecutará si la condición es verdadera. En caso de que la condición sea falsa, se puede proporcionar una cláusula "else" opcional con otro bloque de código a ejecutar.</p>

<p>A continuación, te presento un ejemplo de estructura de control "if": </p>

```
edad = 17

if edad >= 18:
    print("Eres mayor de edad. Puedes ingresar al club.")
else:
    print("Eres menor de edad. No puedes ingresar al club.")

```

<p>En este ejemplo, se verifica si la variable "edad" es mayor o igual a 18. Si la condición es verdadera, se imprimirá el mensaje "Eres mayor de edad. Puedes ingresar al club." De lo contrario, si la condición es falsa, se imprimirá el mensaje "Eres menor de edad. No puedes ingresar al club."
Eric Matthes también ha enfatizado la importancia de la indentación adecuada para delimitar los bloques de código dentro de las estructuras condicionales. En el ejemplo anterior, el bloque de código que se ejecuta en caso de que la condición sea verdadera está indentado con cuatro espacios o una tabulación. Esto asegura que el código se ejecute de manera apropiada y legible.</p>

* Anidados

<p>Una estructura de control que podemos explorar, tomando como referencia a Eric Matthes, es la anidación de instrucciones "if". Esta estructura nos permite evaluar múltiples condiciones y ejecutar bloques de código en función de ellas. Eric Matthes, reconocido autor y educador en programación, ha abordado este tema en sus obras de manera clara y accesible.
La anidación de instrucciones "if" implica colocar una instrucción "if" dentro de otra instrucción "if", permitiendo una mayor flexibilidad en la toma de decisiones. Esto nos permite evaluar diferentes condiciones de manera secuencial y ejecutar diferentes bloques de código en función de esas condiciones.</p>

<p>A continuación, te presento un ejemplo de estructura anidada de instrucciones "if":</p>

```
edad = 17
altura = 150

if edad >= 18:
    if altura >= 160:
        print("Eres mayor de edad y tienes la altura suficiente. Puedes ingresar al parque de atracciones.")
    else:
        print("Eres mayor de edad, pero no cumples con la altura mínima requerida.")
else:
    print("Eres menor de edad. No puedes ingresar al parque de atracciones.")

```
<p>En este ejemplo, se evalúan dos condiciones: la edad y la altura. Si la edad es mayor o igual a 18, se evalúa la siguiente condición: si la altura es mayor o igual a 160. Dependiendo del resultado de ambas condiciones, se ejecutarán diferentes bloques de código.
Eric Matthes destaca la importancia de mantener una adecuada indentación para delimitar los bloques de código anidados. En el ejemplo anterior, los bloques de código anidados están indentados con una mayor cantidad de espacios para indicar su jerarquía dentro de la estructura anidada de instrucciones "if".</p>

* Multiples condiciones IF()

<p>La evaluación de múltiples condiciones en un "if" se puede lograr utilizando operadores lógicos, como "and" (y) y "or" (o), para combinar diferentes expresiones condicionales. Estos operadores permiten crear condiciones más complejas que deben cumplirse para que se ejecute un bloque de código.</p>

<p>A continuación, te presento un ejemplo de evaluación de múltiples condiciones en un "if":</p>

```
edad = 25
ciudad = "Nueva York"

if edad >= 18 and ciudad == "Nueva York":
    print("Eres mayor de edad y vives en Nueva York.")
else:
    print("No cumples con las condiciones necesarias.")

```

<p>En este ejemplo, se evalúan dos condiciones en la instrucción "if": si la edad es mayor o igual a 18 y si la ciudad es igual a "Nueva York". Ambas condiciones deben ser verdaderas para que se ejecute el bloque de código dentro del "if". En caso contrario, se ejecutará el bloque de código dentro del "else".
Eric Matthes ha enfatizado la importancia de utilizar correctamente los operadores lógicos y mantener una buena estructura de código, incluyendo la indentación adecuada, para mejorar la legibilidad y comprensión del programa.
Es importante tener en cuenta que se pueden evaluar múltiples condiciones en un "if" utilizando tanto el operador "and" como el operador "or", dependiendo de los requisitos específicos del programa.</p>

* Condicional alternativo o doble: Sentencia else(sino)

<p>La sentencia "else" se utiliza en conjunto con la instrucción "if" para ejecutar un bloque de código cuando la condición del "if" es falsa. Esto permite establecer una alternativa o ramificación en el flujo de ejecución del programa.</p>

<p>Tomando como referencia el codigo anterior ↑</p>

<p>En ese ejemplo, se evalúa si la variable "edad" es mayor o igual a 18. Si la condición es verdadera, se ejecuta el bloque de código dentro del "if" y se imprime el mensaje "Eres mayor de edad. Puedes ingresar al club.". Sin embargo, si la condición es falsa, se ejecuta el bloque de código dentro del "else" y se imprime el mensaje "Eres menor de edad. No puedes ingresar al club.".
Es importante tener en cuenta que la sentencia "else" se ejecuta solo si la condición del "if" es falsa. En caso contrario, si la condición del "if" es verdadera, el bloque de código del "else" se omitirá.</p>

* Condicional multiple: sentencia elif(sino si)

<p>En muchos lenguajes de programación, como Python, se utiliza la instrucción "if-elif-else" para implementar un condicional múltiple. La instrucción "elif" es una combinación de las palabras "else" e "if", y se utiliza para evaluar condiciones adicionales después de un "if" inicial.</p>

<p>A continuación, te presento un ejemplo de un condicional múltiple utilizando la instrucción "if-elif-else":</p>

```
dia_de_la_semana = "martes"

if dia_de_la_semana == "lunes":
    print("Es el primer día de la semana.")
elif dia_de_la_semana == "martes":
    print("Es el segundo día de la semana.")
elif dia_de_la_semana == "miércoles":
    print("Es el tercer día de la semana.")
elif dia_de_la_semana == "jueves":
    print("Es el cuarto día de la semana.")
elif dia_de_la_semana == "viernes":
    print("Es el quinto día de la semana.")
else:
    print("Es un día del fin de semana.")

```

<p>En este ejemplo, se evalúa el valor de la variable "dia_de_la_semana" y se ejecuta el bloque de código correspondiente al caso específico. Si el valor es "lunes", "martes", "miércoles", "jueves" o "viernes", se imprimirá un mensaje indicando el número del día de la semana. Si el valor no coincide con ninguno de los casos anteriores, se ejecutará el bloque de código dentro del "else" y se imprimirá el mensaje "Es un día del fin de semana".
Es importante tener en cuenta que en un condicional múltiple, una vez que se encuentra una condición verdadera y se ejecuta su bloque de código correspondiente, el resto de los bloques se omiten.</p>

**EJERCICIOS Y DESAFIOS:** [**SEMANA 2 -Resultos paso a paso-**](https://github.com/MartinIsmaelSena/INFORMATORIO_2023/tree/master/RESOLUCIONSEMANA_2) 
*by: Martin Ismael Sena*

---
