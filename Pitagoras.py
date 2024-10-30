import math

#Solicitud datos A y B para hallar hipotenusa
print("Ingrese cateto a y b para realizar el teorema de pitagoras")
A=float(input("Ingrese cateto a: "))
B=float(input("Ingrese cateto b: "))

#Formula hipotenusa
P=math.sqrt(A**2 +B**2)

#Mostrar resulto hipotenusa 
print(("El valor de la hipotenusa es:"),P)