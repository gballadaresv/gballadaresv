from numpy import random, var, mean
from pprint import pprint

random.seed(2123)

lambda_b = 12.0  # 12 bombones per minute
mean_weight = 10.0  # 10 grams mean weight
lista_general = []

VALOR_TEORICO = 0.259123

# Fixed number of bombones to create exactly 1102 groups of 65 bombones each
# Using 1102 because that's approximately what we got in c.py simulations
BOMBONES_FIJOS = 1108 * 65  # 71630 bombones total

for s in range(10):
    bombones_acumulados = []  # Store all bombones weights for this simulation
    
    # Generate exactly BOMBONES_FIJOS bombones with random weights
    for i in range(BOMBONES_FIJOS):
        peso_bombon = random.exponential(mean_weight)  # weight in grams
        bombones_acumulados.append(peso_bombon)
    
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

print("Resumen de las simulaciones (bombones fijos):")
for i, sim in enumerate(lista_general):
    error_absoluto = abs(VALOR_TEORICO - sim[2])
    error_relativo = error_absoluto / VALOR_TEORICO * 100
    print(f"Simulación {i+1}: Grupos que exceden 700g = {sim[0]}, Total grupos = {sim[1]}, Proporción = {sim[2]:.4f}, error absoluto = {error_absoluto:.4f}, error relativo = {error_relativo:.2f}%")

# Calculate overall statistics
proporciones = [sim[2] for sim in lista_general]
media_proporcion = mean(proporciones)
varianza_proporcion = var(proporciones)
print(f"\nEstadísticas generales:")
print(f"Media de proporciones: {media_proporcion:.4f}")
print(f"Varianza de proporciones: {varianza_proporcion:.6f}")
print(f"Desviación estándar: {varianza_proporcion**0.5:.6f}")