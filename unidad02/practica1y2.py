"""
Ejercicio 1

Pruebe las siguientes expresiones en Python. Observe qué resultados obtiene.
Verifique, usando `type()` el tipo de la expresión.

a) 0
b) 1.5 * 0
c) 11 / 2
d) 11 // 2
e) 11.0 // 2.0
f) 2 ** 2
g) "a" + "b"
h) "a" * 0

"""
a = 0
print(a)
print(type(a))

"""
Ejercicio 2

Poner paréntesis en las siguientes expresiones de acuerdo a las reglas de precedencia y asociatividad de los operadores.
Si no conoce la precedencia de algún operador, se aconseja probarla primero en el intérprete.
Una vez hecho esto, determinar el tipo de cada subexpresión entre paréntesis hasta determinar el tipo de la expresión completa.

a) 3 * 5 - 7 * 4 / 14 + 3 / 1
b) 2 ** 1 + 3 / 5 // 4
c) 8 / 4 / 2 ** 2 ** 2
"""

"""
Ejercicio 3

Encontrar el resultado que devuelven las siguientes expresiones

a) (4 >= 40 and 8 <= 10) or (2 < 20 or 10 > 100)
b) 5 <= 10 or (2 / 0) == 1
c) (8 >= 10 or 4 <= 8) and (3 != 10 or 10 >= 4)
d) (50 > 49 and 7 == 5) or (15 <= 14 or 10 > 100)
e) not(not(10 >= 8) and 1 > 3) or (2 != 3 and 2 < 8)
f) (4 > 2 or 7 > 6) and not(3 < 6 or 2 > 0)
g) not(0)
h) not(1)
i) not(8)
j) not('a')
k) not([])
l) not('') or not(' ')
"""

"""
Ejercicio 4

Considerar los siguientes fragmentos de código, y verificar si son correctos o no. En caso de no serlo, proponer un cambio para arreglarlo.
"""
# a)
"print(saludo + " " + destino + puntuacion)"
saludo = "Hola"
destino = "Mundo"
puntuacion = "!"

# b)
cateto1 = 3
cateto2 = 4
hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
del cateto1
del cateto2
print(hipotenusa)

# c)
del "tengo_hambre"
tengo_hambre = False
del tengo_hambre
tengo_hambre = True

"""
Ejercicio 5

Obtener los números pares y el cero usando slicing en la siguiente cadena.

Ayuda: investigue qué es el slicing y las diferentes formas de usarlo.
"""
numeros = "0123456789"

"""
Ejercicio 6

Proponga un método en papel para resolver cada uno de los siguientes problemas.

a) Dada la base y altura de un rectángulo, determinar su área y su perímetro.
b) Calcular la nota final de un alumno que se obtiene de promediar las 3 notas de sus parciales.
c) Calcular la distancia entre dos puntos en el plano, usando pitágoras (a^2 + b^2 = c^2)

Ahora, con ayuda de su docente, empezaremos a ver cómo escribir estos algoritmos como programas en Python.
"""

"""
Ejercicio 7

Conocido el número en matemática PI, pedir al usuario que ingrese el valor del radio de una circunferencia y calcular y mostrar por pantalla el área y perí́metro. Recuerde que para calcular el área y el perí́metro se utilizan las siguientes fórmulas:

Area = π * radio^2
Perimetro = 2 * π * radio
"""

"""
Ejercicio 8

Escribir un programa que calcule cuántos litros de combustible consumió un automóvil. El usuario debe
ingresar una cantidad de litros de combustible cargados en la estación y una cantidad de kilómetros
recorridos. Después, el programa calculará el consumo (km/lt) y se lo mostrará al usuario.
"""

"""
Ejercicio 9

Escriba un programa que permita al usuario ingresar el valor de dos variables numéricas de tipo entero.
Posteriormente, el programa debe intercambiar los valores de ambas variables y mostrar el resultado
final por pantalla. Por ejemplo, si el usuario ingresa los valores num1 = 9 y num2 = 3, la salida del programa deberá mostrar: num1 = 3 y num2 = 9.

Ayuda: Para intercambiar los valores de dos variables se debe utilizar una variable auxiliar.
"""

"""
Ejercicio 10

Modelar los siguientes problemas, nombrando los datos relevantes de entrada y salida, junto con los tipos de datos
que se usarán para representarlos dentro de Python. Luego programar la solución.

a) Se tienen dos habitaciones dentro de un hogar, cada una con una temperatura ambiente posiblemente distinta.
Se quiere saber a qué temperatura estarán las habitaciones, dado suficiente tiempo para que se transmita
el calor de una a la otra.

b) Se tiene una multitud afuera, cada persona le dirá su nombre a cada otra persona en la multitud.
Se quiere saber cuánto tiempo llevará hacer esto, dado que decir una vez tu nombre lleva aproximadamente 4 segundos y medio.

c) Hay dos personas con nombres muy largos, pero similares.
Se quiere conocer, por un lado, si tienen el mismo tamaño, y por otro lado si son iguales.

Ayuda para el programa: investigar la función `len`.
"""

###
# Ejercicio: Elabore un script en Python que solcite al usuario el ingreso 
# de 2 números (pueden contener decimales). Sume ambos números y muestre por
# consola el resultado como entero.

numeroUno = input("Ingrese un número decimal: ")
numeroDos = input("Ingrese otro número decimal: ")
numeroUnoFloat = float(numeroUno)
numeroDosFloat = float(numeroDos)
resultado = numeroUnoFloat + numeroDosFloat
print("resultado casteado a entero:  ", int(resultado))
print("resultado sin castear a entero: ", resultado)
print(type(resultado))