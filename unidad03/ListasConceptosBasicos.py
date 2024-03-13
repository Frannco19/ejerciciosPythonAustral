#Vamos a crear una lista
una_lista = ["Ana", 1984, "Pez", 34, 28]

#Los datos alojados en la lista tienen un orden, para conocer la ubicación
#debemos conocer su índice. Los índices de una lista, si leemos la lista
#de izquierda a derche comienzan por el 0, lo que significa que
#el primer elemento de una lista siempre se encuentra en el índice 0.
#Entonces si vemos nuestra lista, el dato "Ana" se encuentra en el índice 0, 
#el dato 1984 se encuentra en el índice 1, el dato "Pez" se encuentra en el índice 2
#el dato 34 en el índice 3 y el dato 28 en el índice 4.

#Si yo quiero obtener el primer dato que se encuentra en la lista, debo utilizar
#el operador [] colocando adentro el índice del dato que quiero obtener.
#Veamos un ejemplo
#Voy a crear una variable "primer_elemento" para alojar el primer dato de la lista "una_lista"

primer_elemento = una_lista[0]

print(primer_elemento)
#Si hacemos correr el programa, vamos a ver que en la terminal se imprime el primer elemento
#de la lista "una_lista" alojado en la variable "primer_elemento"

#Ejercicio: imprimir en la terminal el segundo y el cuarto elemento
#alojados en variables que indiquen que son el segundo y cuarto elemento.

#Existe otra forma de recorrer la lista, yo puedo comenzar a contar los elementos
#de derecha a izquierda pero en ese caso el índice se vuelve negativo, comenzando
#con el -1, es decir, el último elemento de la lista va a tener siempre el índice -1.
#Veamos un ejemplo.

ultimo_elemento = una_lista[-1]

print(ultimo_elemento)
#Si hacemos correr el programa, vamos a ver que en la terminal se imprime el último
#elemento de la lista "una_lista" alojado en la variable "ultimo_elemento"

#Ejercicio: imprimir en la terminal el primer y segundo elemento de la lista utilizando
#los índices negativos, alojados en unas variables que indiquen que son el primer y segundo
#elemento.

#En el caso de que quisiera obtener varios datos de una lista, en vez de buscarlos índice por índice
#puedo hacer uso del operador : el cual me permite indicar el índice de inicio y el índice de fin
#para poder recorrer la lista y obtener los resultados comprendidos entre ellos
#sin contar el último elemento indicado. Veamos un ejemplo, para ello voy a crear otra lista.

lista = ["Pera", "Zapallo", "Banana", "Zanahoria", "Ciruela", "Papa", "Acelga"]

#si yo quiero obtener el tercero "Banana", cuarto "Zanahoria" y quinto "Ciruela" dato voy a hacer lo siguiente

seleccion345 = lista[2:5]
#Entre corchetes [] yo indico el índice del primer elemento que quiero seleccionar
#coloco el operador dos puntos : y luego indico el índice del elemento en el cual quiero que 
#finalice la selección, ese último elemento no se selecciona! 

print(seleccion345)
#Vemos el resultado impreso por terminal

#Ejercicio: imprimir el penúltimo "Papa" y antepenúltimo "Ciruela" elemento
#de la lista, utilizando índices negativos.

#Si quiero imprimir todos los elementos desde el inicio hasta uno determinado,
#no es necesario que coloque el índice 0, solo basta con colocar el fin.

lista_numeros = [0,1,2,3,4,5,6,7,8,9]

numeros_hasta_5 = lista_numeros[:6]

print(numeros_hasta_5)

#Ocurre lo mismo si quiero imprimir la lista hasta el fin empezando desde un
#determinado elemento.

numeros_desde_6 = lista_numeros[6:]

print(numeros_desde_6)

#Ejercicio: Aplicando lo que vimos hasta acá
#y tomando lista_numeros, crear variables e imprimir de forma que el resultado sea:
#[0,1,2,3]
#[4,5,6]
#[7,8,9]

#Podemos, además de  seleccionar los elementos desde un inicio a un fin
#indicar que se haga un salto para saltear algunos elementos. Veamos un ejemplo
#si seguimos con la lista "lista_numeros" y yo quiero obtener los número pares
#podemos hacer lo siguiente
#voy a recorrer de inicio a fin la lista, por eso dejo vacíos los dos primeros espacios
#el de inicio y fin y en el último espacio indico el salto, qué significa,
#al colocar el número dos yo estoy indicando que quiero que seleccione los elementos
#con una separación de dos
numero_pares = lista_numeros[::2]

print(numero_pares)
#Podemos ver que se imprime el número 0 salta el 1, toma el 2, salta el 3 elige el 4 y así,
#saltando siempre el segundo

#Ejercicio: tomando lista_numeros imprimir en la terminal los múltiplos de 3 guardados en
#una variable que así lo especifique.

