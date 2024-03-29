"""
Ejercicio 11

Dada una lista de números y un número, determine en qué posición se encuentra el número en la lista.
Si no se encuentra, que el programa muestre -1. Utilice break al encontrar el número.

"""

""" numbers = [11, 25, 5, -4, 95]
n = 3
bandera = False
for i in range(len(numbers)):
    if numbers[i] == n:
        print("El número se encontró en la posición:", i)
        bandera = True
        break

if not bandera:
    print("El número no se encontró en la lista .")

"""

"""
Ejercicio 12

Dada una lista de números al azar, encuentre la primer aparición del número 0.
Asegúrese de detener el ciclo una vez que se encuentre el número,
pues no hacerlo hará que el programa tarde mucho tiempo en ejecutarse.

import random

numbers = [random.randint(0, 100) for i in range(1_000_000)]
"""


"""
Ejercicio 13

Dada la lista inicial [0, 1], agregue 100 veces la suma de los dos últimos números de la lista.
Detenga el programa si la suma de los dos últimos números es mayor a 1000.
Esta es una forma de generar la secuencia de Fibonacci.

numbers = [0, 1]
"""

"""
Ejercicio 14

Dada una lista de palabras que comienzan con 'a', muestre cada una en una línea.
Cuando encuentre una palabra que comienza con 'b', detenga el programa.

import random

words = ['apple', 'avocado', 'blueberry', 'apricot']

random.shuffle(words)
"""

"""
Ejercicio 15

Procese una lista de tuplas (actividad, edad), donde se pide se muestren
los siguientes mensajes debido a las siguientes condiciones:

- Si la edad es 65+ y la actividad es "trabajar", muestre "jubilado que trabaja".
- Si la edad es 65+ y la actividad es "descansar", muestre "jubilado retirado".
- Si la edad es 18+ y la actividad es "estudiar", muestre "mayor de edad que estudia".
- Si la edad es 18+ y la actividad es "trabajar", muestre "mayor de edad que trabaja".
- Si la actividad no es ninguna de las mencionadas detenga el programa mostrando un error.
- Si la edad es menor que 5, no muestre nada
- En cualquier otro caso, muestre "nada interesante".

Utilice continue para evitar anidar condicionales,
asegúrese de ordenar las condiciones de manera conveniente.
"""