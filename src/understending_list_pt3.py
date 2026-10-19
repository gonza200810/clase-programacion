# trabajando con las listas
print("\n\tel dia de hoy aprendere a trabajar con las listas en python\n" .upper())
magicians = ['harry', 'hermione', 'ron']
print(magicians)

print(magicians[0], magicians[1], magicians[2])

# ciclo for
for magician in magicians:
    print(magician)

# a esto se le conoce como lopping
    for magician in magicians:
        print(f"{magician.title()}, ese fue un gran echizo!")
        print(f"Gracias a todos por participar en el show!")
