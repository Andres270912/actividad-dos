#Developer Harrinson Andres Martinez Leon <3
# Conversión de tipos de datos
x = int(input("Ingresar un número entero: "))
y = float(x)
print(f"Tu numero en formato decial es: {y}")

## Enteros a Decimales
x = 10
y = float(x)
print(y)






## Decimales a Enteros
a = 3.14
b = int(a)
print(b)






## Cadenas a Enteros
s1 = "42"
c = int(s1)
print(c)





## Cadenas a Decimales
s2 = "3.14"
d = float(s2)
print(d)





#Multilíneas de cadenas.
text = "¡Hola, mundo!"
length = len(text)
print(length)





#Funcion Len
text = "¡Hola, mundo!"
length = len(text)
print(length)




#Subcadenas
message = "¡Bienvenido a Python!"




# Obtener los primeros n caracteres
first_5 = message[:5]
print(first_5)





# Obtener los caracteres de en medio
middle_chars = message[5:11]
print(middle_chars)





# Obtener los últimos n caracteres
last_6 = message[-6:]
print(last_6)





#Función upper().
#Convierte los caracteres de una cadena en mayusculas
text = "¡Hola!"
uppercase_text = text.upper()
print(uppercase_text)






#Función lower()
#Convertir todos los caracteres de una cadena en minúsculas.
text = "¡HOLA!"
lowercase_text = text.lower()
print(lowercase_text)





#Función strip()
#Elimina los espacios en blanco al principio y al final de una cadena.
text = "   ¡Hola, mundo!   "
stripped_text = text.strip()
print(stripped_text)





#Función replace()
#Reemplace todas las ocurrencias de una subcadena por otra.
text = "Me gusta Python. Aprendo Python."
new_text = text.replace("Python", "Java")
print(new_text)







#Función split()
#Divida una cadena en una lista de cadenas subsiguientes.
text = "Hola,mundo,¿cómo,estás?"
words = text.split(",")
print(words)





## Formato de cadenas F-String
name = input("Ingresar nombre: ")
age = int(input("Ingresar edad: "))
message = f"Holi, mi nombre es {name} y tengo {age} años."
print(message)