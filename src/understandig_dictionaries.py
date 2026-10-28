# dicionario simple
alien_0 = {'color': 'green', 'points': 5}

# dici0nario vacio
alien_1 = {}

# diccionario mas simple
alien_2 = {'color': 'verde'}

# accesar a los elementos de un diccionario
print(f'\n tu alien 0 es de color: {alien_0['color'].upper()}')
print(f'\n si matas al alien 0 obtienes: {alien_0["points"]}')

# agregar elementos a un diccionario
print(f'\n agregando elementos a un diccionario'.upper())
alien_0["x_positions"] = 25
alien_0['y_positions'] = 0

print(alien_0)

#modificando el valor en un diccionario
print(f'\n modificando el valor de un diccionario'.upper())
alien_0['y_positions'] = 80
print(alien_0)

#eliminando un elemento de un diccionario
print(f'\n eliminiando elementos al diccionario'.upper())
del alien_0['points']
print(alien_0)

#diccionarios para objetos (elementos) similares
favorite_lenguajes = {
    'gen': 'python',
    'sarah': 'c',
    'eduard': 'ruby',
    'phill': 'python'
}

#print(f'\n lenguaje favorito:{favorite_lenguajes["phill"]}')

#looping though all key-values pairs
#looping a traves de todos los pares llave-valor
user_0 = {
    'username': 'jose',
    'firstname': 'reyna',
    'lastname': 'perez',
    'age': '17',
    'birthday': '8-10'
}

print(f'\n looping a traves de las llaves \n')
for key  in user_0.items():
    print('key:',key)

print(f'\n looping a traves de los valores \n')
for value in user_0.values():
    print('values:',value)
    