import math

def tiempo_para_huevo_a_la_copa(To):
    # Constantes
    M = 67  # masa del huevo en gramos
    rho = 1.038  # densidad en g/cm^3
    c = 3.7  # capacidad calorífica específica en J/(g*K)
    K = 5.4e-3  # conductividad térmica en W/(cm*K)
    Tw = 100  # temperatura de ebullición del agua en °C
    Ty = 70  # temperatura máxima de la yema en °C

    # Calcular el tiempo usando la fórmula corregida
    t = ((M**(2/3) * c * rho**(1/3)) / 
         (K * math.pi**2 * (4 * math.pi / 3)**(2/3))) * \
        math.log(0.76 * (To - Tw) / (Ty - Tw))

    return t

# Solicitar la temperatura original del huevo al usuario
temperatura_original = float(input("Ingrese la temperatura original del huevo (°C): "))

# Calcular el tiempo
tiempo = tiempo_para_huevo_a_la_copa(temperatura_original)

# Mostrar el tiempo en segundos
print(f"El tiempo que toma alcanzar la temperatura máxima para preparar el huevo a la copa es: {tiempo:.2f} segundos")
