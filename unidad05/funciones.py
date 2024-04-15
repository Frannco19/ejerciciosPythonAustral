"""
A lo largo de esta práctica trabajamos con funciones, así que a menos que se explicite otra cosa,
lo que pide el ejercicio es una o múltiples funciones, no necesariamente llamarlas es parte del resultado.

Escribir funciones, a pesar de que por su cuenta no hagan nada, es la esencia de programar módulos.
"""

"""
Ejercicio 1

Escribir una función que altera un string agregándole un
saludo y un signo de exclamación al final, llámela con diferentes valores

No imprima dentro de la función, imprima sus resultados
"""

""" palabra = input("Ingrese la palabra : ")

def funcionSaludo(palabra):
    return print(palabra, "Hola !")

funcionSaludo(palabra) """

"""
Ejercicio 2

Defina una función con tres parámetros, el primero es un string (txt),
el segundo es un int (n), y el tercero otro string (sep). Haga que retorne
un string que sea la repetición de txt, n veces, cada uno separado del siguiente usando sep.

Ejemplo: "Hola" 3 "," --> "Hola,Hola,Hola"
"""
def funcionPalabra(palabra, numero, comas):
    print()

"""
Ejercicio 3

Defina una función que dada una edad y un límite de edad (que por defecto debe ser 18)
Determine si la edad es mayor al límite o no, devolviendo True o False indicando este hecho.

Recordar que los argumentos con valores por defecto van al final, y se escriben arg = valor

Opcional: escriba la función de la forma más simplificada posible
(que retorne el resultado inmediatamente) y re-escríbala como un lambda
"""

"""
Ejercicio 4

Complete la función parcialmente definida debajo, que toma precios
como primer argumento y un precio como segundo argumento.

La función retorna True o False de acuerdo a si
el menor precio de la lista es más chico que precioOferta
y además retorna el menor precio de la lista.

Recuerde que para devolver múltiples valores hacemos return v1, v2, v3 ...
y se entiende que es una tupla de valores. Utilice el siguiente encabezado

precios: list[float] = [4.04, 5.37, 7.77, 0.09, 9.11, 4.96, 9.12, 2.28, 8.09, 7.36]

def hay_oferta(precios: list[float], precioOferta: float) -> tuple[bool, float]:
    ...
"""

"""
Ejercicio 5

Diseñe e implemente un par de funciones que permitan calcular el área de un círculo y un rectángulo.
Luego escriba código que pida al usuario de qué tipo de figura quiere calcular el área y, de acuerdo
a la respuesta, pida los datos necesarios y muestre el resultado.
"""

"""
Ejercicio 6

Escriba una función, dada una lista de enteros, retorne una nueva lista sin números duplicados.

Ayuda: puede usar un diccionario para revisar si los números ya han sido vistos.
"""

"""
Ejercicio 7

Escriba una función de ingreso de datos que resuelva los errores. La función debe pedir una fruta
al usuario, y si el usuario no ingresa una de "frutilla", "banana", "pera", debe volver a pedirle hasta que lo haga.
La función siempre retorna una de estas frutas, no retorna hasta que lo logre.

Usarla para pedir 3 frutas e imprimir si hay al menos una frutilla.
"""

"""
Ejercicio 8

Mantener un diccionario global { fruta: cantidad } que comience vacío, donde la cantidad está en kilogramos.
Implementar la función que agrega una fruta al diccionario,
teniendo cuidado de no sobreescribir la cantidad si la fruta ya existe.

Además escribir fuera de la función el programa principal que pide al usuario frutas hasta que ingrese '*'.

Al terminar muestre el diccionario completo.

frutas = {}
"""

"""
Ejercicio 9

Implementar funciones nuevas, basadas en el ejercicio anterior
- actualizar_fruta(): actualiza la cantidad de una fruta, si ya existe
- ver_lista_total(): muestra el diccionario de forma legible
- ver_peso_total(): muestra los kilogramos totales de mercancia
- ver_ganancia_estimada(precio_promedio_kg): muestra la ganancia estimada
dado el precio promedio por kilogramo de fruta, de entre todas las frutas.

Llamar las funciones al terminar de ingresar frutas en el ejercicio anterior
"""

"""
Ejercicio 10

Para terminar de implementar el sistema de stock de frutas, agregar al siguiente menu
de opciones las llamadas a las funciones correspondientes, y si faltan datos
realizar los inputs correspondientes. Estos pueden estar dentro de las funciones.
"""

# while True:
#     print("\n¿Qué desea hacer?")
#     print("1. Agregar una fruta")
#     print("2. Actualizar una fruta")
#     print("3. Ver la lista completa de frutas")
#     print("4. Ver el peso total")
#     print("5. Ver la ganancia estimada")
#     print("6. Salir")
#
#     option = int(input("Ingrese una opción: "))
#     ...