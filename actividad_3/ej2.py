# 2. Codifica un programa que pregunte el nombre completo del usuario en la consola y
# después muestre por pantalla el nombre completo del usuario tres veces, una con
# todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
# primera letra del nombre y de los apellidos en mayúscula. El usuario puede
# introducir su nombre combinando mayúsculas y minúsculas como quiera.

# solicitamos el nombre
nombre = input("Ingrese nombre completo: ")
apellido = input("Ingrese apellido completo: ")

# nombre  en minus
print(nombre.lower(), apellido.lower())

#nombre en mayus
print(nombre.upper(), apellido.upper())

# Mostrar el nombre completo con la primera letra de cada palabra en mayúsculas
print(nombre.title(), apellido.upper())