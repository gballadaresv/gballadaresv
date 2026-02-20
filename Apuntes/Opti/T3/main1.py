from gurobipy import GRB, Model
import csv

### Manejo de archivos
with open("muestras.csv", "r") as file:
    reader = list(csv.reader(file))
    headers = reader[0]
    values = reader[1:]

### Modelo
model = Model()

# Variables
w = model.addVars(range(100), vtype=GRB.CONTINUOUS, name="w_i")
b = model.addVar(vtype=GRB.CONTINUOUS, name="b")

model.update()

# Parametros
x = {(i, r): float(values[r][i]) for i in range(15)
      for r in range(100)}

y = {r: float(list(map(lambda value: value[15], values))[r])
      for r in range(100)}

# Funcion objetivo
model.setObjective(
    sum(
        (b + sum(
            w[i] * x[i, r] - y[r]
        for i in range(15))) ** 2
        for r in range(100)
    )
)

model.optimize()

### Resultados
for i in range(14):
    print(f"La caracteristica {headers[i]} tiene un peso de {w[i].x} en la funcion.")
print(f"La constante de {headers[15]} tiene un valor de {b.x} gramos.")
