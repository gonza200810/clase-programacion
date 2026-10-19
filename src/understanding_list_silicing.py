# silicing
players = ["charly", "juan", "iancarlos", "lisandro"]
print("lista original",players)
print(players[0:2])

#El silicing me permite trabajar con un grupo 
#especifico de una lista: al resultado se le conoce  como
# "un slice"

print("1:4", players[1:4]) # ['juan', 'iancarlos', 'lisandro']
print(":3", players[:3]) # ['charly', 'juan', 'iancarlos']
print("2:", players[2:]) #  ['iancarlos', 'lisandro']
print("[-3:]", players[-3:]) # ['juan', 'iancarlos', 'lisandro']

#players = ["charly", "juan", "iancarlos", "lisandro"]
# casos especiales del slicing
print(players[1:6]) # ['juan', 'iancarlos', 'lisandro']
print(players[6:1])

#looping trhough a slice

students = ["raul", "charly", "juan", "iancarlos", "lisandro"]
for student in students[0:3]:
   print(f"el estudiante {student}, va a pasar la materia.")

print(students)




# ¿como podemos copiar una lista?
my_food = ["pizza", "tacos", 'flautas']
my_friend_food = my_food #manera erronea de copiar una lista

#tres maneras de copiar una lista
#metodo 1 utilizando slicing
my_friend_food_2 = my_food[:]

#metodo 2 utilizando el metodo de las listas .copy()
my_friend_food_3 = my_food.copy()

#metodo 3 utilizando el metodo build-in list()
my_friend_food_4 = my_food(my_food)



