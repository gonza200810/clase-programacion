"""
Un string es de manera sencilla una serie de caracteres


En python todo lo que se encuentre dentro de comillas
simples '' o dobles comillas "" es considerado un string.

"Esto es un string"
'Esto tambien es un strimg'
'Le dije a un amigo, "python es mi lenguaje favoriyo"'


incorrecto
"'
'"


"""

name = "clase de progRamación"
print(name)

print(name.title())
print(name)

name = name.title()
print(name)

"""
un método es una acción que
python puede realizar rn un 
fragmento de datos sobre una variable. El punto (.) despues 
de una variable, seguido del metodo title() dice que tiene que ejecutar
title() de la variable name.

Todos los metodos van seguidos de parentesis 
porque en ocaciones necesitan informacion
adicional para funcionar, lo cual iria dentro
de los parentesis. En esta ocacion el metodo
.title() no requiere informacion adicional
para funcionar.

"""

# Otros Metodos
print(name.upper())
print(name.lower())