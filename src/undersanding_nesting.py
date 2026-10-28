#nesting

#listas de diccionarios

covenant_elite = {'color':'azul','points':'10', 'shield':True}
covenant_jackal = {'color':'verde','points':'6', 'shield':True}
covenant_grunts = {'color':'orange','points':'3', 'shield':False}

#nesting de lista de diccionarios
covenants = []
covenants.append(covenant_elite)
covenants.append(covenant_jackal)
covenants.append(covenant_grunts)
print(covenants)

print('looping')
#looping though the list
for covenant in covenants:
    print(covenant)

# vamos a crear una flotilla de eneigos (covenant)
covenants_fleet = []
for _ in range (2):
    covenants_fleet.append(covenant_elite)

for _ in range (5):
    covenants_fleet.append(covenant_jackal)

for _ in range (20):
    covenants_fleet.append(covenant_grunts)


print('\n flotilla')
print(covenants_fleet)

'''
# nesting: una lista en un diccionario
# menu
print('\n nesting: listas en dicccionaios')
tacos = {
    'tortillas':



}

print(f'tu has ordenado unos tacos de {tacos['guisos'][0]}')
print(f'en tortillas de {tacos['tortillas'][1]}')
'''



# nesting: diccionarios en diccionarios
#meu de usuarios
user = {
    'charly': {
        'firstname': 'carlos',
        'middlename': 'antonio',
        'lastname': 'tovar garcia',
        'location': 'mexioco',
        'age': 34,
    },

    'mrred': {
        'firstname': 'jose',
        'middlename': 'lisandro',
        'lastname': 'villareal martinez',
        'location': 'mexioco',
        'age': 18,
    }
}

# looping de diccionarios en diccionarios
for use, user_info in user.items():
    fullname = f'{user_info['firstname']} {user_info['middlename']} {user_info['lastname']}'
    location = user_info['location']
    age = user_info['age']
    print(f'\n\n el nombre completo de (user) es:')
    print(fullname)
    print(f'\n la ubicacion de (user) es:')
    print(location)
    print(f'\n la edad de (user) es:')
    print(age)



