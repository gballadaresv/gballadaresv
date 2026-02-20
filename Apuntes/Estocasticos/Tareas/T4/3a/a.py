from numpy import random
from pprint import pprint

random.seed(2123)

lambda_b = 12.0
lambda_p = 0.1
lista_general = []

bombones_total = 0

# 30 simulaciones
""" for s in range(30):
    tiempo_sim = 0.0
    lista_sim = []

    # para cada intervalo
    for i in range(1200):
        tiempo_intervalo = 0.0
        bombones_intervalo = 0
        lista_intervalo = []

        # mientras el tiempo este dentro del intervalo
        while tiempo_intervalo <= 5:
            tiempo_bombon = random.exponential(1 / lambda_b, 1)
            peso_bombon = random.exponential(1 / lambda_p, 1)
            tiempo_intervalo += tiempo_bombon[0]
            tiempo_sim += tiempo_bombon[0]
            bombones_intervalo += 1
            bombones_total += 1
            if tiempo_intervalo <= 5:
                lista_intervalo.append((i, tiempo_bombon[0], peso_bombon[0]))
        if tiempo_intervalo > 5:
            tiempo_intervalo -= tiempo_bombon[0]
        lista_sim.append(lista_intervalo)
    lista_general.append(lista_sim) """

# 1 simulacion
# para cada intervalo
for i in range(1200):
    tiempo_intervalo = 0.0
    bombones_intervalo = 0
    lista_intervalo = []

    # mientras el tiempo este dentro del intervalo
    while tiempo_intervalo <= 5:
        tiempo_bombon = random.exponential(1 / lambda_b, 1)
        peso_bombon = random.exponential(1 / lambda_p, 1)
        tiempo_intervalo += tiempo_bombon[0]
        bombones_intervalo += 1
        bombones_total += 1
        if tiempo_intervalo <= 5:
            lista_intervalo.append((i, tiempo_intervalo, peso_bombon[0]))
    if tiempo_intervalo > 5:
        tiempo_intervalo -= tiempo_bombon[0]
    print(f"Intervalo {i+1}: Bombones {bombones_intervalo}, Tiempo en intervalo: {tiempo_intervalo:.2f} segundos, "
        f"Tiempo total: {(tiempo_intervalo + i*5):.2f} segundos")