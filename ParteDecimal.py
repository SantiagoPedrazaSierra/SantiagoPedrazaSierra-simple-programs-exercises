#Solicitar primer numero al usuario
numero=float(input("Ingrese un numero: "))

#Separacion parte decimal
entero=int(numero)
decimal=abs(numero-entero)

#Resultado de separar decimal primer numero 
print (decimal)

#Solicitar segundo numero al usuario
numero=float(input("Ingrese un numero: "))

#Separacion parte decimal
entero=int(numero)
decimal=abs(numero-entero)

#Resultado de separar decimal psegundo numero 
print (f"{decimal:.2f}")
