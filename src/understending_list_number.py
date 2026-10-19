# listas de numeros 
"""
las listas tambien pueden almacenar numeros. python
ofrece varias herramientas para trabajar eficientemente con listas de numeros.

"""


# metodo build-in range()

"""
el metodo range () nos ayuda a creear facilmente 
series de numeros 

Crea una secuencia denumeros, especialmente para repetir un for cierta cantidad de veces

ejemplo
"""

for value in range(1, 5):
    print(value)

# crtear una lista de numeros utilizando metodo range() 
numbers = list(range(0,10))
print(numbers)

# lista de numeros pares
even_numbers = list(range(0, 11, 2))
# que pasa con un paso negativo? o si empieza de mayor a menor 
print(even_numbers)

