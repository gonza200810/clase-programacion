"""
las listas nos permiten almacenar informacion en un lugar 
la cantidad que se desee: ya sean pocos elementos 
o millones de elementos.

una lista es una coleccion de items (elementos) que tiene un orden particular, 
se pueden creear listas que incluyan strings, enteros, floats, los nombres de las personas de tu familia, etc, 
podemos almacenar (los tipos de datos almacenados en python) lo que queremos en una lista.

son elementos mutables: puede modiificarse el tamaño de la lista

se recomienda nombrar una variable del tipo lista en plural.

en python los corchetes [] indican una lista, 
sus elementos se separan por comas.

ejemplo: 
"""
bicycles = ['trek', "cannondale", 'redine', 'sepcialized', 'giant']
print(bicycles)
# bicycles = "" es de tipo string
# ¿como podemos acceder alos elementos de una lista?

"""
las listas son colecciones ordenadas. se puede acceder a un elemento de la lista diciendole a python 
la psision o indice del elemento deseado.

para obtener el valor deseado, se debe escribir  el nombre 
de la lista , seguido del indice (posision) del elemento 

"""

print(bicycles[2], bicycles[0], bicycles[1])

print(bicycles[0].upper())
# los indices comiensan en 0, no en 1
# bicycles = ['trek', "cannondale", 'redine', 'sepcialized']
# ejemplo
print(bicycles[1]) # cannondale

# acendiendo al ultimo elemento de la lista
print(bicycles[-1])
print(bicycles[-2])

"""
Una lista en Python es una colección ordenada y mutable de elementos, 
creada con corchetes [], que puede contener datos de cualquier tipo, 
como números, textos o incluso otras listas.

"""



# primer metodo de las listas append() agrega un elemento al final de la lista
