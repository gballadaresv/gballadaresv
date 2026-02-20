from gurobipy import *
from matplotlib import pylpot as plt

# Código incompleto
# X defecto guroby minimiza
N = None
a = None
b = None
j = None

tsp = Model() # Genera un objeto de modelado
#tsp.Paramos.OutputFlag = 0

#Crear vars
x = tsp.addVars(N, N, vtypre=GRB.BINARY) # Añadimos variables binarias de NxN
f = tsp.addVars(N, N) # Si no se ponen params adicionales las vars son cont no neg x defecto

#Crear restricciones de salida
tsp.addConstr(sum(x[i,j] for j in N if j != 1) == 1 for i in N)

#Crear restricciones de entrada
tsp.addConstr(sum(x[j,i] for j in N if j != 1) == 1 for i in N)

#Eliminiación de sub-tours
tsp.addConstr(sum(f[i,j] for j in N if j != i) - sum(f[j,i] for j in N if j != i) == -1)
tsp.addConstr(sum(f[0,j] for j in N if j != 0) - sum(f[j,0] ))

tsp.addConstr(f[i,j] <= (N-1)*x[i,j] for i in N for j in N)

#Función objetivo
tsp.setObjective()

#Resultados
print("Valor optimo =")

#graficar ##Falta el módulo para graficar
#fig, ax = plt.subplots()
#ax.scatter(a, b)
"""""
for i in N:
    for j in N:
        if i != j and x[i,j].x > 0.9: #NUNCA preguntar == 1 #Si el arco (i,j) es utilizado:
            #print(i,j) ##Imprime el arco
            ax.plot((a[i]), a[j])
"""""
