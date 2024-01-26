# 4. Codifica un programa que pregunte el nombre del usuario y después de que el
# usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde
# <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
# que tienen el nombre.

# solicitamos el nombre
nombre = input("Ingrese nombre: ")

# nombre a mayúsculas
nombre_mayus = nombre.upper()

# calcular cant de letras en el nombre
cant_letras = len(nombre)

# nombre en mayus y el numero de letras
print(nombre_mayus, "tiene", cant_letras, "letras")