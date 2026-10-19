# identacion

"""
python utiliza la identacion para determinar 
cuando una linea esta conectada a la linea de codigo anterior.

basicamente se utilizan 4 espacios en blanco para obligarnos a escribir codigo ordenado y estructurado

"""
# no olvidemos identar
magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#print(magician) # identation error

# error de logica identation error
for magician in magicians:
    print(magician) 
print(f"no puedo esperar a ver tu proximo echizo, {magician}")

#  identacion inecesaria IndentationError: unexpected indent
message = "hello python world"
#    print(message)

# no olvidar las 2 puntos (:) SyntaxError: expected ':'
for magician in magicians:
    print(magician)