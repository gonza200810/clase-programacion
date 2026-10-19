# if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'subaru':
        print(car.upper())
    else:
        print(car)


# el condicional o condition
# el condicional es el corazon del if

#condicional verdadero
# condicional true
truck = "ford"
print(truck == "ford") 

# condicional falso
# conditional false
print(truck == "audi")


print(truck == 'Ford'.lower())


# condicional de desigualdades !=
print(truck != 'audi')# true
print(truck != 'ford') # false


# comparaciones numericas
print("comparaciones numericas")
age = 34
print(age == 34)  # true


answer = 17
if answer != 24:
    print(" esano es la respuesta correcta")


number = 20
print(number <= 21)


#multiple conditions
age_0 = 22
age_1 = 18
print("multiple conditions")
print(age_0 >= 21 and age_1 >= 21) # false
print(age_0 >= 21 and age_1 >= 18) # true


print("operacion or") 
print(age_0 >= 21 or age_1 >= 21) # true
print(age_0 >= 23 or age_1 >= 21) # false


food = ["chilaquiles", 'flautas', "gorditas", "tamales"]
print("\n ¿nopales esta en la lista?")
print("nopales"in food) # false
print("¿gorditas esta en la lista?")
print("gorditas" in food) # true



#¿como preguntarce si un elemento NO esta en la lista?
banned_user = ['andrew', 'carolina', 'david']
user = 'marie'
print(user not in banned_user) # true