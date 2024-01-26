# 1. Crea un programa que pregunte al usuario por el número de horas trabajadas y el
# coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

# Solicitamos las horas chambeadas
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))

# solicitamos el costo por hora
costo_por_hora = float(input("Ingrese el costo por hora: "))

# calcular la lana
paga = horas_trabajadas * costo_por_hora

# Imprimir la nomina
print("La paga que le corresponde es: ", paga)