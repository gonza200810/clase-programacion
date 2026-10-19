"""
crear una lista con 
los primeros 10 numeros cuadranticos

"""

squares = [] # crear una lista vacia
for value in range(0,11): # usamos for para repetir una accion
    squares.append(value ** 2) # value **2 significa elevar al cuadrado y .append() sirve para agregar un elemento al final de la lista
    # enonces va agregando los cuadrados a squares
print(squares)# muestra la lista con los cuadrados de los numeros del 0 al 10