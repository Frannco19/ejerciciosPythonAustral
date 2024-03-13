#Veamos algunos de los métodos más comunes para manipular listas
#Pongamos una lista de ejemplo

una_lista = [10, 3, "Hola", 8.5]
print("Ésta es la lista original: ", una_lista)

#Si quiero agregar un elemento al final de la lista voy a utilizar el método
#apend() colocando entre los paréntesis el elemento que quiero agregar
#veamos un ejemplo

una_lista.append(1980)
#Para llamar a un método lo que tengo que hacer es escribir la variable (el nombre de la lista)
#y seguido poner un punto, luego indico el método que quiero aplicar a dicha lista

print(una_lista)
#imprimo la lista con el dato agregado al final

#Qué sucede si quiero agregar varios elementos a una lista o los elementos de una lista en otra
#voy a usar el método extend()
#Tomando de ejemplo la lista anterior le voy a agregar los elementos de otra lista

otra_lista = ["Esta es otra lista"]

una_lista.extend(otra_lista)

print(una_lista)

#puedo agregarle elementos que no se encuentren en una variable

una_lista.extend([7,10])

print(una_lista)

#Todos los métodos que vimos anteriormente agregan elementos al final de la lista, pero qué sucede
#si yo quiero agregarlos en un determinado lugar, para eso puedo utilizar el método
#insert() donde debo indicar el índice en el que quiero agregar el elemento y el elemento a agregar
#veamos un ejemplo tomando la lista anterior

una_lista.insert(1, "Elemento insertado")

print(una_lista)

#Por ahora solo vimos métodos para insertar elementos, veamos ahora métodos para remover
#Uno de ellos es el método remove() donde entre paréntesis le voy a indicar el elemento
#que quiero remover, se va a recorrer la lista y el primero que coincida se elimina
#veamos un ejemplo si quiero remover el "Hola" de la lista que tengo

una_lista.remove("Hola")

print(una_lista)

#Otro método para eliminar, en este caso, un elemento de una determinada posición 
# es pop() debo indicar entre paréntesis el índice del elemento a eliminar 
# éste método además me devuelve el elemento eliminado
#veamos un ejemplo

elemento_eliminado = una_lista.pop(1)

print("éste es el elemento eliminado: ", elemento_eliminado)
print(una_lista)

#Si no conozco el índice del elemento puedo conocerlo con el método
#index() indicando entre paréntesis cuál es el elemento del cual quiero conocer
#el índice en la lista, para luego poder por ejemplo eliminarlo

indice = una_lista.index('Esta es otra lista')
eliminar_elemento = una_lista.pop(indice)
print("El elemento con índice: ", indice, " fué eliminado")

#Otro método que puede resultar útil es el método count()
#éste método me cuenta la cantidad de veces que un elemento aparece en la lista

conteo = una_lista.count(10)

print("La cantidad de veces que aparece el número 10 es: ", conteo)

#Si quisiera conocer el largo de una lista utilizo la función len()
#colocando dentro de los paréntesis la lista que quiero contar

largo_de_lista = len(una_lista)

print("La cantidad de elementos en la lista es de: ", largo_de_lista)

#Puedo también ordenar los elementos de una lista utilizando el método sort()
#los ordena de forma ascendente

una_lista.sort()
print(una_lista)

#Si quiero invertir ese orden, entonces uso el método reverse()

una_lista.reverse()
print(una_lista)

#Ejercicio: Dada la siguiente lista de números, utilizando los métodos anteriores
# contar cuántos elementos hay en la lista
# agregar el número 24.9 en el índice 4
# contar cuántas veces aparece el número 2038
# eliminar el número 5769
# obtener el número más pequeño y el más grande 
# imprimir todos los resultado obtenidos

lista_numeros = [1957, 2038, 5769, 45.98, 38.5, 3789, 2038, 23.09, 6589, 1897, 38.5, 2038]
