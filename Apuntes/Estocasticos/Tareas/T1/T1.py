import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import comb

def simular_experimento():
    conteo = 0
    caras = 0
    sellos = 0
    while True:
        conteo += 1
        lanzamiento = random.choice(["C", "S"])
        if lanzamiento == "C":
            caras += 1
        elif lanzamiento == "S":
            sellos +=1
        if caras >= 1 and sellos >= 1:
            return conteo

# Realizar 1000 simulaciones
n_experimentos = 1000
resultados = [simular_experimento() for _ in range(n_experimentos)]

# Determinar el rango de lanzamientos observados
n_min = 2
n_max = max(resultados)
n_values = np.arange(n_min, n_max + 1)

# Calcular la probabilidad teórica usando la distribución negativa binomial:
# P(N=n) = comb(n-1, 2) / 2^n  para n >= 3
probs_teoricas = [1/2**(n-1) for n in n_values]
"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Cambiar la distribución teórica
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

# Calcular el promedio de lanzamientos obtenidos en la simulación
avg_resultado = np.mean(resultados)

# Configurar el gráfico usando Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(resultados, bins=np.arange(n_min - 0.5, n_max + 1.5, 1),
            stat="density", color="skyblue", edgecolor="black", label="Simulación")

# Superponer la curva teórica
plt.plot(n_values, probs_teoricas, marker='o', linestyle='-', color='darkred',
        linewidth=2, markersize=6, label=r'Teórico: $P(N=n)=1/2**(n-1)$')

plt.xlabel('Número de lanzamientos', fontsize=12)
plt.ylabel('Probabilidad', fontsize=12)
plt.title('Experimento: Lanzar una moneda hasta obtener 3 caras', fontsize=14, fontweight='bold')
plt.xticks(n_values)
plt.grid(True, linestyle='--', alpha=0.7)

# Anotar el promedio obtenido en la simulación
plt.text(0.95, 0.95, f'Promedio simulación: {avg_resultado:.2f}',
        horizontalalignment='right', verticalalignment='top',
        transform=plt.gca().transAxes, fontsize=12,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

plt.legend(fontsize=12)
plt.tight_layout()

# Guardar la imagen (opcional)
plt.savefig('Grafico_1cara_1sello.png')
plt.show()