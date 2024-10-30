# Solicitar al usuario las notas de los dos primeros certámenes y la nota de laboratorio
C1 = float(input("Ingrese nota certamen 1: "))
C2 = float(input("Ingrese nota certamen 2: "))
Nl= float(input("Ingrese nota laboratorio: "))

NC=(59.5-(0.3*Nl)) / 0.7
C3=(((3*NC)-(C1+C2))+1)

#Resultado de C3
print(round(C3))