guisos = ['salsa verde ', 'deshebrada', 'nopales']

if "salsa verde" in guisos:
    print('hay salsa verde')
elif 'deshebrada' in guisos:
    print('hay deshebrada')
elif 'guisio especial' in guisos:
    print('hay guiso especial')


# lista vacia
guisos_2 = ['salsa verde', 'picadillo', 'asado']

if guisos_2:
    for guiso in guisos_2:
        print(guisos)
else:
    print('no hay guisos')


#
guisos_disponibles = ['salsa', 'deshebrada', 'picadillo', 'asado']
guisos_a_ordenar = ['barbacoa', 'deshebrada', 'cabrito']

for guisos in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print('si hay de ese guiso')
    else:
        print('una disculpa, no tenemos ese guiso')

print('final')