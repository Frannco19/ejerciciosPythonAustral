# Dada una lista imprimir: 
# El elemento "banana" con índice positivo
# El elemento "piña" con índice negativo
# Utilizando slicing los elementos "banana", "piña" y "kiwi"
# Con slicing los elementos "manzana" y "naranja"
# También con slicing "kiwi" y "cereza"
# La lista actualizando el elemento "naranja" por "mandarina" suponiendo que no 
# conocemos su índice
# La lista agregando el elemento "durazno" al final de la lista
# La lista eliminando el elemento "banana" suponiendo que no conocemos su índice
# Si una fruta ingresada por un usuario se encuentra en la lista, dar una respuesta
# de que se encuentra dicha fruta en la lista, de lo contrario decir que no se encuentra
mi_lista = ["manzana", "naranja", "banana", "piña", "kiwi", "cereza"]
print(mi_lista[2])
print(mi_lista[-3])
elementosslicing1 = mi_lista[2:5]
print(elementosslicing1)
elementosslicing2 = mi_lista[0:2]
print(elementosslicing2)
elementosslicing3 = mi_lista[4:-1]
print(elementosslicing3)
mi_lista[1] = "mandarina"
print(mi_lista)
mi_lista.append("durazno")
print(mi_lista)
mi_lista.pop(2)
print(mi_lista)
""" buscarFruta = input("ingrese la fruta a buscar :")
if buscarFruta in mi_lista:
    print("La fruta se encuentra en la lista! :)")
else:
    print("La fruta no se encuentra! :(") """

# Dada una lista anidada, imprimir el elemento 6
# Reemplazar el elemento 7 por 10
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])
matriz[2][0] = 10
print(matriz)

# Dado un diccionario:
# Imprimir el nombre de la persona y su edad
# Imprimirlo agregando un elemento al diccionario 
# con key "profesión" y valor "ingeniero"
# Actualizar la edad a 35 e imprimir el resultado
# Renombrar la key "ciudad" por "localidad"
# Eliminar el elemento "ciudad" del diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"} 
print(mi_diccionario.get("nombre"), (mi_diccionario.get("edad")))
mi_diccionario.update({"profesion":"ingeniero"})
print(mi_diccionario)
mi_diccionario.update({"edad":35})
print(mi_diccionario)
#mi_diccionario["localidad"] = mi_diccionario.pop("ciudad")
#print(mi_diccionario)
mi_diccionario.pop("ciudad")
print(mi_diccionario)


# Dado un diccionario anidado
# Cambiar el valor del salario de Juan a 18000.
# Imprimir el salario de Lucas

empleados = {
    'emp1': {'name': 'Sol', 'salary': 17500},
    'emp2': {'name': 'Lucas', 'salary': 18500},
    'emp3': {'name': 'Juan', 'salary': 17500}
}

empleados["emp3"]["salary"] = 18000
#print(empleados)
print(empleados["emp2"]["salary"])

# Listas = [son modificables]
# tuplas = (no son modificables)
# diccionarios = {"clave": valor, .............}
# sets = {no posee elementos duplicados, son modificables}