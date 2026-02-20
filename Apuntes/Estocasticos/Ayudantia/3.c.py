import numpy as np

# Definir las tasas
lagartija = 17
carpintero = 0.5
tabano = 40 * 0.8
tasas = [lagartija, carpintero, tabano]

# Simulación
llegaron_menos100 = 0
for i in range(10000):
    llegadas_inicial = [0, 0, 0]
    for animal in range(3):
        tiempo = 0.0
        while tiempo <= 3:
            tiempo += np.random.exponential(1 / tasas[animal])
            if tiempo <= 3:
                llegadas_inicial[animal] += 1
    if llegadas_inicial[0] < 50 and llegadas_inicial[1] < 4 and llegadas_inicial[2] < 100:
        llegaron_menos100 += 1


probabilidad = llegaron_menos100/10000
print(probabilidad)

