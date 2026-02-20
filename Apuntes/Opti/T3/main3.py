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

e = [0, 1, 6, 10, 12]

# Funcion objetivo
model.setObjective(
    sum(
        (b + sum(
            w[i] * x[i, r] - y[r]
        for i in e)) ** 2
        for r in range(100)
    )
)

model.optimize()

print("La formula que debe seguir la empresa es de:\n")
string = f"Y = {round(w[1].x, 5)}*X_1 +"

for i in e[1:]:
    string += f"{round(w[i].x, 5)}*X_{i} +"
string += f" {b.x}"
print(string)
print("\n")
print("Donde:\n")
print(f"Y representa {headers[15]}")
for i in e:
    print(f"X_{i} representa {headers[i]}")