# 5. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
# paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
# cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
# programa que lea el número de payasos y muñecas vendidos en el último pedido y
# calcule el peso total del paquete que será enviado.

# promt para numero de payasos
payasos = int(input("Ingrese el número de payasos: "))

# promt para el numero de muñecas
muñecas = int(input("Ingrese el número de muñecas: "))

# calculamos el peso total del paquete
peso_total = payasos * 112 + muñecas * 75

# imprimimos el peso total del paquete
print("El peso total del paquete es:", peso_total, "gramos")

