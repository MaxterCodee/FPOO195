# 1. Escribir un programa que almacene la cadena de caracteres una contraseña en
# una variable, después que solicite al usuario una contraseña e imprima en
# pantalla si la contraseña introducida por el usuario coincide con la guardada en
# la variable sin tener en cuenta mayúscula y minúscula.

# variable contraseña guardada
contra = "Portal 32"

# solicitamos contraseña
contrasena_usuario = input("Introduce una contraseña: ")

# comparamos en minuscula
if contra.lower() == contrasena_usuario.lower():
    print("Las contraseñas coinciden.")
else:
    print("Las contraseñas no coinciden.")