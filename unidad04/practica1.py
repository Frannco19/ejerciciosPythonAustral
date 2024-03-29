"""
Ejercicio 1

De todos los números entre el 1 y el 100 inclusive, imprima los números que son múltiplos de 3 y de 5.
Recuerde que para verificar divisibilidad puede utilizar el operador % (módulo) que devuelve el resto de la división entre dos números.

Opcional: resuelva el problema Fizz Buzz tradicional de las entrevistas de programación:
https://en.wikipedia.org/wiki/Fizz_buzz
"""


""" for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
"""

"""
Ejercicio 2
Sume todos los números pares entre el 1 y el 100 inclusive. El resultado esperado es 2550.
"""

""" sumaNumPar = 0

for num in range(1,101):
    if num % 2 == 0:
        sumaNumPar = num + sumaNumPar
        
print("suma de numeros pares :", sumaNumPar) 
"""

"""
Ejercicio 3

Imprima una cuenta regresiva, comenzando en 10 y terminando en 0, pero que en vez de imprimir el 0, imprima "¡Feliz Año Nuevo!".
"""

""" for num in range(10,-1,-1):
    if num == 0:
        print("Feliz año nuevo !!")
    else:
        print(num)
"""
 
"""
Ejercicio 4

Dado un string cualquiera, cree otro string nuevo dado vuelta, sin utilizar el método reverse.

word = "Python"

# El resultado esperado es "nohtyP"
"""
""" 
palabra = "Python"
reversa = ""


for i in range(len(palabra) - 1, -1, -1):
    reversa += palabra[i]

print(reversa) """

"""
Ejercicio 5

Determine si un número ingresado es primo o no. Un número es primo si es divisible únicamente por 1 y por sí mismo.

Opcional: determine todos los números primos entre el 1 y el 100 inclusive. Se puede lograr con un for dentro de otro.
"""

         

"""
Ejercicio 6

Genere una lista con todas las tripletas pitagóricas (a, b, c) donde a, b y c son números enteros positivos
que cumplen con el teorema de Pitágoras, es decir, a^2 + b^2 = c^2. O sea que forman un triángulo rectángulo.

Para ello, genere todas las combinaciones posibles de a, b y c entre 1 y 100 con tres for anidados.
"""



"""
Ejercicio 7

Dado un texto cualquiera, determine cuántas veces aparece cada vocal en el texto. No distinga entre mayúsculas y minúsculas.
Recuerde que puede iterar por sobre las letras de un texto utilizando el for solamente. Recuerde el método lower.

Comience con el siguiente diccionario:

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

Opcional: comience con un diccionario vacío y cuente cualquier letra. A medida que aparezcan nuevas, agréguelas.
"""


"""
Ejercicio 8

Calcular el promedio el promedio de las calificaciones de los estudiantes.
Los estudiantes serán cargados por el usuario en un diccionario "Nombre: Calificación".

Para ello pídale que primero ingrese la CANTIDAD de estudiantes que se ingresarán,
para luego ingresar el NOMBRE y la CALIFICACIÓN de cada uno esa cantidad de veces.

Una vez terminado este proceso, que se calcule el promedio y se muestre por pantalla.

students = {}
"""

"""
Ejercicio 9

Escriba los siguientes programas sin utilizar métodos de lista.

a. Dada una lista de números, calcule el mínimo y el máximo de la lista. Nota: es posible hacerlo
recorriendo una única vez la lista o recorriéndola dos veces. Piense las ventajas y desventajas de
ambos métodos.

numbers = [11, 25, 3, -4, 95]

# El programa debería mostrar -4 y 95

b. Dada una lista palabras, cree una nueva lista formada sólo por aquellas que comienzan con "a".

words = ["arbol", "barco", "artificial", "casa", "dado", "a"]

# El programa debería mostrar
["arbol" , "artificial" , "a"]
"""

"""
Ejercicio 10

Un investigador de historia de la informática encontró un documento sin membrete, que data de
mitad de siglo XX, e incluye un mensaje en código morse que sospecha explicaría importantes sucesos
históricos de la posteridad. Por lo tanto, para avanzar en su investigación es necesario descifrarlo, pero
no sabe el código. Dado el siguiente diccionario que explica la codificación del código morse, ayude al
investigador en su tarea mediante un programa que le permita decodificar el mensaje.

El diccionario es útil para codificar, pero no para decodificar, intente crear un diccionario de traducción inversa.

morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.',
    'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
}

code = ['.--.', '-.--', '-', '....', '---', '-.']
"""