from gurobipy import Model, GRB, quicksum
import csv

### Obtenemos loa datos de los archivos
# Creamos una lista con los costos y un conjunto cereales
with open("costos.csv") as file:
    csvreader = csv.reader(file)
    next(csvreader)
    costos = [float(fila[0]) for fila in csvreader]
    cereales = range(len(costos))

# Creamos listas con los límites superior e inferios, y un conjunto nutrientes
with open("limites.csv") as file:
    csvreader = csv.reader(file)
    next(csvreader)
    limites = [fila for fila in csvreader]
    lim_inf = [float(nut[0]) for nut in limites]
    lim_sup = [float(nut[1]) for nut in limites]
    nutrientes = range(len(limites))

# Creamos una lista de listas con los las cantidades de nutrientes por tipo de cereal
with open("contenidos_nutricionales.csv") as file:
    csvreader = csv.reader(file)
    next(csvreader)
    nuts_x_cereal = [i for i in csvreader]
    for nut in range(len(nuts_x_cereal)):
        for cereal in range(len(nuts_x_cereal[nut])):
            nuts_x_cereal[nut][cereal] = float(nuts_x_cereal[nut][cereal])


### Creamos el modelo
model = Model()

# Creamos las variables
x = model.addVars(cereales, vtype=GRB.CONTINUOUS, name="x")
model.update()

# Definimos los parámetros
a = {(i,j): nuts_x_cereal[i][j] for i in nutrientes for j in cereales}
b = {i: lim_inf[i] for i in nutrientes}
l = {i: lim_sup[i] for i in nutrientes}
c = {j: costos[j] for j in cereales}

### Definimos las restricciones
# Las proporciones tienen que sumar 1
model.addConstr(
    quicksum(x[j] for j in cereales) == 1,
    name="R1"
)
# Cantidad mínima de nutrientes
model.addConstrs(
    (quicksum(a[i, j] * x[j] for j in cereales) >= b[i] for i in nutrientes),
    name="R2"
)
# Cantidad máxima de nutrientes
model.addConstrs(
    (quicksum(a[i, j] * x[j] for j in cereales) <= l[i] for i in nutrientes),
    name="R3"
)

### Función objetivo
model.setObjective(
    (quicksum(c[j] * x[j] for j in cereales)),
    GRB.MINIMIZE
)

model.optimize()

### Manejo de resultados
valor_objetivo = model.ObjVal

print("\n"+"-"*10+"Manejo de resultados"+"-"*10+"\n")
print(f"El valor óptimo es un costo de ${valor_objetivo} por kg de comida\n")
for j in cereales:
    print(f"La proporción del cereal {j+1} en la mezcla es de {x[j].x}")
