# Pedir al usuario las notas de los dos primeros certámenes y la nota de laboratorio
c1 = float(input("Ingrese nota certamen 1: "))
c2 = float(input("Ingrese nota certamen 2: "))
nl = float(input("Ingrese nota laboratorio: "))

# Nota final deseada
nf_deseada = 60

# Calcular el promedio de los certámenes y la nota final
# Primero calculamos el promedio del laboratorio
promedio_lab = nl * 0.3

# Ahora despejamos NC para encontrar lo que necesitamos
nc_necesario = (nf_deseada - promedio_lab) / 0.7

# Ahora, calculamos la nota necesaria en el tercer certamen
c3_necesario = (nc_necesario * 3) - (c1 + c2)

# Mostramos la nota necesaria en el tercer certamen
print(f"Necesita nota {c3_necesario:.2f} en el certamen 3")