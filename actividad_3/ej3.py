# 3. Escribir un programa que solicite un entero X, introducido por el usuario y después
# muestre en pantalla la suma de todos los enteros desde 1 hasta X

# solicitar el numero entero "x"
X = int(input("Ingrese un número entero: "))

# ahora  calculamos la suma de 1 hasta X
suma = sum(range(1, X + 1))

# Imprimir la suma
print("La suma de todos los enteros desde 1 hasta", X, "es:", suma)