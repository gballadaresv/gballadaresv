from numpy import random, var, mean
from pprint import pprint

random.seed(2123)

lambda_b = 12.0  # 12 bombones per minute
mean_weight = 10.0  # 10 grams mean weight
bombones_total = 0
lista_general = []

VALOR_TEORICO = 0.259123

for s in range(10):
    lista_sim = []
    bombones_acumulados = []  # Store all bombones weights for this simulation
    
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
            bombones_acumulados.append(peso_bombon)  # Store individual bombon weight
    
    # Group bombones in sets of 65 and check if total weight > 700g
    grupos_exceden_700 = 0
    total_grupos = len(bombones_acumulados) // 65
    
    for grupo in range(total_grupos):
        inicio = grupo * 65
        fin = inicio + 65
        peso_grupo = sum(bombones_acumulados[inicio:fin])
        if peso_grupo > 700:
            grupos_exceden_700 += 1
    
    proporcion = grupos_exceden_700 / total_grupos if total_grupos > 0 else 0
    lista_general.append([grupos_exceden_700, total_grupos, proporcion])

print("Resumen de las simulaciones:")
for i, sim in enumerate(lista_general):
    error_absoluto = abs(VALOR_TEORICO - sim[2])
    error_relativo = error_absoluto / VALOR_TEORICO * 100
    print(f"Simulación {i+1}: Grupos que exceden 700g = {sim[0]}, Total grupos = {sim[1]}, Proporción = {sim[2]:.4f}, error absoluto = {error_absoluto:.4f}, error relativo = {error_relativo:.2f}")