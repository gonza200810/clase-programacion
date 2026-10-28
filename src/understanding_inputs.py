# input - sirve para realizar entradas de usuario
'''
Metodos build-in input

intput(argumentos) - argumento (str): mensaje al usuario

input retorna un string



'''
firstname = input('escrive tu primer nombre: ')
middlename = input('escribe tu segundo nombre: ')
lastname = input('escribe tu apellido (paterno y materno): ')

fullname = f'{firstname} {middlename} {lastname}'
print(fullname)