from numpy import random, var, mean
from pprint import pprint

random.seed(2123)

lambda_b = 12.0  # 12 bombones per minute
mean_weight = 10.0  # 10 grams mean weight
bombones_total = 0

PROMEDIO_TEORICO = 600
VARIANZA_TEORICA = 12000

lista_general = []
for s in range(10):
    lista_sim = []
    for i in range(1200):
        tiempo_intervalo = 0.0
        bombones_intervalo = 0
        peso_intervalo = 0

        # mientras el tiempo este dentro del intervalo
        while True:
            tiempo_bombon = random.exponential(1 / lambda_b)  # time until next bombon
            nuevo_tiempo = tiempo_intervalo + tiempo_bombon
        
            if nuevo_tiempo > 5:  # check if next bombon arrives after 5 minutes
                break
            
            peso_bombon = random.exponential(mean_weight)  # weight in grams
            tiempo_intervalo = nuevo_tiempo
            bombones_intervalo += 1
            bombones_total += 1
            peso_intervalo += peso_bombon
        lista_sim.append(peso_intervalo)

    peso_promedio = mean(lista_sim)
    varianza_bombon = var(lista_sim)
    lista_general.append([peso_promedio, varianza_bombon])

print("Resumen de las simulaciones:")
for i, sim in enumerate(lista_general):
    error_absoluto = abs(PROMEDIO_TEORICO - sim[0])
    error_relativo = error_absoluto / PROMEDIO_TEORICO * 100
    print(f"Simulación {i+1}: Peso promedio = {sim[0]:.2f} [gramos], Varianza = {sim[1]:.2f} [gramos²], error absoluto = {error_absoluto:.2f} [gramos], error relativo = {error_relativo:.2f}%")
