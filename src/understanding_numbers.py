# Numeros
# Enteros

"""
los numeros enteros  los podemos sumar, restar, multiplicar y dividir

"""

print(2+3)
print(3-2)
print(2*3)
print(4/2)

# enteros
# sumar +
# restar -
# multipilcar *
# dividir /
## divicion entera //
# potencias **n
print(3**2) # 3^2
print(3**3) # 3^3
print(10%2) # modulo (mod)
age = 34
print(age)
name = "gonzalo perez"
print(name, age)

# floats
"""
python llama floats a cualquier numero con punto decimal

"""
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)

# imprimir la edad de alguien

age = 34 # variable tipo int
message = "Gonzalo tiene " + str(age) + " años. "
print(message)
message_f = f"gonzalo tiene {age} años. "
print(message_f)


"""

typeError: python no puede reconocer el tipo de informacion que se esta utilizando.
 
en este caso no se puede concatenar
ints a sring

"""

print(type(age))
print(type(0.1))
print(type(message_f), type(2+3))