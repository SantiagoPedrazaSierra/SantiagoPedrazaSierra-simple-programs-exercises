
import math
#Solicitar radio al usuario
radio= float(input("Ingrese el radio del circulo: "))

#Calcular el perimetro
perimetro= 2* math.pi* radio

#Calcular el area 
area= math.pi*(radio ** 2)
 
 #Mostrar resultados
print(f"El perimetro del circulo es: {perimetro:.2f}")
print(f"El area del circulo es: {area:.2f}")
