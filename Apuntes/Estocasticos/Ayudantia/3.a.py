import numpy as np
from scipy.stats import expon

# Configuración de tasas
lambda_d = 100
lambda_m = 87
lambda_r = 60

# Cálculo de probabilidad teórica
probabilidad_teorica = (lambda_d / (lambda_d + lambda_m) -
                        lambda_d / (lambda_d + lambda_m + lambda_r) +
                        lambda_r / (lambda_r + lambda_m) -
                        lambda_r / (lambda_d + lambda_m + lambda_r))

# Cálculo de probabilidad experimental
muestra_d = expon.rvs(scale=1/lambda_d, size=10000)
muestra_m = expon.rvs(scale=1/lambda_m, size=10000)
muestra_r = expon.rvs(scale=1/lambda_r, size=10000)

contador = np.sum((muestra_m > muestra_d) & (muestra_m > muestra_r))
probabilidad_simulacion = contador / 10000

# Resultados
print(f"La probabilidad P(T_m > T_r > T_d) teórica es: {probabilidad_teorica}")
print(f"La probabilidad experimental es: {probabilidad_simulacion}")