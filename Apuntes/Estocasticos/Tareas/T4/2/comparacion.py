import numpy as np
import math

# Parámetros estimados (ajusta estos valores según tus resultados)
lambd = 0.269    # tasa de llegada estimada (autos/minuto)
mu_total = 0.3073  # tasa de atención total del sistema (autos/minuto)
c = 3           # número de servidores

# Para el modelo M/M/c, la tasa por servidor es:
mu = mu_total / c

# Fórmulas M/M/c
def mmc_metrics(lambd, mu, c):
    rho = lambd / (c * mu)
    # Probabilidad de 0 en sistema (P0)
    sum_terms = sum([(c * rho) ** n / math.factorial(n) for n in range(c)])
    last_term = ((c * rho) ** c) / (math.factorial(c) * (1 - rho)) if rho < 1 else np.inf
    P0 = 1 / (sum_terms + last_term)
    # Lq: promedio en cola
    Lq = (P0 * ((c * rho) ** c) * rho) / (math.factorial(c) * (1 - rho) ** 2) if rho < 1 else np.inf
    # L: promedio en sistema
    L = Lq + lambd / mu
    # Wq: tiempo promedio en cola
    Wq = Lq / lambd if lambd > 0 else np.inf
    # W: tiempo promedio en sistema
    W = Wq + 1 / mu
    return {
        'rho': rho,
        'P0': P0,
        'Lq': Lq,
        'L': L,
        'Wq': Wq,
        'W': W
    }

mmc = mmc_metrics(lambd, mu, c)

print("=== PARÁMETROS TEÓRICOS M/M/c ===")
print(f"Tasa de atención por servidor (mu): {mu:.4f} autos/minuto")
print(f"Tasa de atención total del sistema: {mu_total:.4f} autos/minuto")
print(f"Utilización del sistema (rho): {mmc['rho']:.3f}")
print(f"Promedio de autos en cola (Lq): {mmc['Lq']:.3f}")
print(f"Promedio de autos en el sistema (L): {mmc['L']:.3f}")
print(f"Tiempo promedio en cola (Wq): {mmc['Wq']:.3f} min")
print(f"Tiempo promedio en el sistema (W): {mmc['W']:.3f} min")
print(f"Probabilidad de sistema vacío (P0): {mmc['P0']:.3f}")

# Puedes copiar aquí los valores reales calculados en fitdistr.py para comparar
# Ejemplo:
# print("\n=== VALORES REALES OBSERVADOS ===")
# print(f"Promedio de autos en cola (real): ...")
# print(f"Promedio de autos en el sistema (real): ...")
# print(f"Tiempo promedio en cola (real): ...")
# print(f"Tiempo promedio en el sistema (real): ...")

