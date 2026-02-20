from gurobipy import Model, GRB

model = Model()

x = model.addVar(vtype=GRB.CONTINUOUS, name="X") 
y = model.addVar(vtype=GRB.CONTINUOUS, name="y") 
z = model.addVar(vtype=GRB.CONTINUOUS, name="z") 

model.update()

model.addConstr(3*x + y + 2*z <= 8, name="R1")
model.addConstr(x + 2*y + z <= 10, name="R2")
model.addConstr(-x - y - 3*z >= -14, name="R3")

obj = 2*x + 4*y + 5*z
model.setObjective(obj, GRB.MAXIMIZE)

model.optimize()


print(f"El valor objetivo es de {model.ObjVal}")
print(f"La variable x toma el valor de {x.x}")
print(f"La variable y toma el valor de {y.x}")
print(f"La variable z toma el valor de {z.x}")

for constr in model.getConstrs():
    print(constr, constr.getAttr("slack"))
    if constr.getAttr("slack") == 0:
        print(f"Restricción {constr} está activa)")