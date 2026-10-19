# primer metodo de las listas append() agrega un elemento al final de la lista
"""
motorcycles = ['honda', 'mortalica', 'yamaha']
print(motorcycles) # ['honda', 'mortalica', 'yamaha']

 # metodo append() agrega un elemento al final de la lista

motorcycles.append('kawasaki')
print(motorcycles) # ['honda', 'mortalica', 'yamaha', 'kawasaki']
"""
"""
el metodo append ayuda a crear listas 
facilmente de manera dinamica

"""
"""
motorcycles_2 = [] # lista vacia
print(motorcycles_2)

motorcycle = 'ducati'
motorcycles_2.append(motorcycle) # 1 elemento
motorcycles_2.append('yamaha') # 2 elemento
motorcycles_2.append('suzuki') # 3 elemento
print(motorcycles_2)
motorcycles = "gonzalo"
print(motorcycles_2)
motorcycles_2.append(motorcycles)

# el metodo insert() permite agregar un elemento en una posicion especifica de la lista
motorcycles_3 = ['honda', 'yamaha', 'suzuki']
print("\nlista original")
print(motorcycles_3)
motorcycles_3.insert(3, "ducati") 
print("lista despues del metodo insert")
print(motorcycles_3)
"""
"""
# metodo pop() permite eliminar el ultimo elemento de la lista 
# pero nos permite utilizar el elemento despues de eliminarlo
motorcycle_4 = ['honda', 'susuki', 'hd', 'mortalica']
print(motorcycle_4)
motorcycle_4.pop()
print(motorcycle_4)
# deleted_motorcycle = motorcycles_4.pop()


# se puede utilizar tambien para eliminar un elemento especifico
print(motorcycle_4)
motorcycle_4.pop(2)
print(motorcycle_4)
"""

# metodo remove permite elementos por su valor
