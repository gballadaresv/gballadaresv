from gurobipy import GRB, Model, quicksum
# quicksum es apra las sumatorias

##### Crear modelo
model = Model()
model.setParam("TimeLimit", 60) # Si se acaba el tiempo, devuelve la mejor sol q alcanzó a encontrar.

### Crear variables
# Crear variable
x = model.addVar(vtype = GRB.INTEGER, name = "x") # Variable discreta
x = model.addVar(vtype = GRB.CONTINUOUS, name = "x") # Variable continua, son >= 0
x = model.addVar(vtype = GRB.BINARY, name = "x") # Variable binaria

# Crear variables con subíndice
y = model.addVars({"conjunto"}, vtype = GRB.INTEGER, name = "y_i") #Se podría hacer con un for i in conjunto

# Varaiables con varios subíndices
y = model.addVars({"conjunto1"}, {"conjunto2"}, vtype = GRB.INTEGER, name = "y_ij") #Se podría hacer con un for i in conjunto


#Luego de crear las variables, hay que añadirlas al modelo
model.update()


### Agregar restricciones
# Agregar UNA restricción
model.addConstr({"restriccion"}, name="R1")

# Agregar VARIAS restricciones (Para todo)
model.addContrs(({"Restr"} for i in {"conjunto"}), name="R2")

## Sumatorias
suma = quicksum({"var"} for i in {"I"} for j in {"J"}) # Cada for es una sumatoria, doble sumatoria, dos for

### Función objetivo
model.setObjective({"funcion_objetivo"}, GRB.MAXIMIZE) # O GRB.MINIMIZE, por defecto se minimiza

# Resolver modelo
model.optimize()


### Manejo de variables
# Valor objetivo
valor_objetivo = model.ObjVal

# Valores de variables
print({x.x}) # x es la var, x.x es su valor

# Valores de variables con subíndice
for i in {"conjunto"}:
    print({y[i].x}) # Y sub i es la variable, .x para su valor

# Valor de todas lass variables no 0
model.printAttr("X") 


# Holguras
for constr in model.getConstrs():
    print(constr, constr.getAttr("slack")) #Imprime las holguras, si es 0 significa que es activa

