from gurobipy import GRB, Model
import csv
from pprint import pprint
from time import time

ti = time()
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
z = model.addVars(range(15), vtype=GRB.CONTINUOUS, name="z_i")

model.update()

# Parametros
x = {(i, r): float(values[r][i]) for i in range(15)
      for r in range(100)}

y = {r: float(list(map(lambda value: value[15], values))[r])
      for r in range(100)}

lamdba = 0

# Restricciones
model.addConstrs(-z[i] <= w[i] for i in range(15))

model.addConstrs(z[i] >= w[i] for i in range(15))

# Funcion objetivo
model.setObjective(
    sum(
        (b + sum(
            w[i] * x[i, r] - y[r]
        for i in range(15))) ** 2
        for r in range(100)
    ) + lamdba * sum(z[i] for i in range(15))
)

model.optimize()


### Resultados

pesos = [w[i].x for i in range(15)]

def contador(lista):
    c = 0
    e = set()
    for i in range(len(lista)):
        if lista[i] > 1e-11:
            c += 1
            e.add(i)
    return c, e

while contador(pesos)[0] != 5:
    model = Model()

    # Variables
    w = model.addVars(range(100), vtype=GRB.CONTINUOUS, name="w_i")
    b = model.addVar(vtype=GRB.CONTINUOUS, name="b")
    z = model.addVars(range(15), vtype=GRB.CONTINUOUS, name="z_i")

    model.update()

    # Parametros
    x = {(i, r): float(values[r][i]) for i in range(15)
          for r in range(100)}

    y = {r: float(list(map(lambda value: value[15], values))[r])
          for r in range(100)}

    lamdba +=1

    # Restricciones
    model.addConstrs(-z[i] <= w[i] for i in range(15))

    model.addConstrs(z[i] >= w[i] for i in range(15))

    # Funcion objetivo
    model.setObjective(
        sum(
            (b + sum(
                w[i] * x[i, r] - y[r]
            for i in range(15))) ** 2
            for r in range(100)
        ) + lamdba * sum(z[i] for i in range(15))
    )

    model.optimize()
    pesos = [w[i].x for i in range(15)]

    print(f"Con un lambda de {lamdba}, el numero de caracteristicas importantes es de {contador(pesos)[0]}")


### Resultados
for i in range(14):
    print(f"La caracteristica {headers[i]} tiene un peso de {w[i].x} en la funcion.")
print(f"La constante de {headers[15]} tiene un valor de {b.x} gramos.")

pesos = [w[i].x for i in range(15)]

def contador(lista):
    c = 0
    e = set()
    for i in range(len(lista)):
        if lista[i] > 1e-11:
            c += 1
            e.add(i)
    return c, e

print("\n")
print(f"Con un lambda de {lamdba}, el numero de caracteristicas importantes es de {contador(pesos)[0]}")
print(f"El conjunto E es {contador(pesos)[1]}")

tf = time()

print(f"Tiempo total: {tf-ti}")