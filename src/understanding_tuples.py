"""
Tuplas 

las tuplas son lista de elementos que no cambian de tamaño.
es decir las tuplas son listas inmutables

se utilizan () para definir una tupla.
 
   ejemplo:

    si tenemos un rectangulo (largo, ancho)que siempre va 
    a tener cierto tamaño, podemos asegurar que sus dimenciones
    no va a cambiar si colocamos sus valores en una tabla.

"""

dimensions = (200,50)#200 de largo x 50 de ancho
print("tupla original:",dimensions)

# vamos a imprimir elementos de una tupla
#se realiza de la misma forma que con una 
print(dimensions[0])
print(dimensions[1])

# vamos a modificar el valor de una lista
names = ["carlos", "charly", "juan", "wendy"]
#names[0] = "gonza" 
print(names)

#dimensions[0] = 500 # esta operacion no esta permitida
#looping throgh a tuple
for dimension in dimensions:
    print(dimensions)

"""
no podemos modificar una tupla lo que si podemos hacer es 
cambiar es la asignasion de una variable que almacena una tupla

"""
dimensions = (500, 1000, 20)
print("tupla re-definida:",dimensions)

"""
numbers = "gon"
print(dir(numbers))
"""


#tipos de datos booleanos
answer = True
print(answer)
#print(dir(answer))
