import sys
import csv
from gurobipy import Model, GRB, quicksum
from PyQt6.QtWidgets import QWidget, QGridLayout, QApplication, QLabel
##### Este código requiere de PyQt6 para funcionar,
##### si no lo tiene instalado, deberá hacerlo según OS.

### Manejo de archivos
with open("capacidad_por_saco.csv", "r") as file:
    csv_reader = csv.reader(file)
    capacidadxsaco = [int(i[0]) for i in csv_reader]

with open("costo_saco.csv", "r") as file:
    costoxsaco = list(csv.reader(file))
    for i in range(len(costoxsaco)):
        for j in range(len(costoxsaco[i])):
            costoxsaco[i][j] = int(costoxsaco[i][j])
    semillas = range(len(costoxsaco))
    tiempos = range(len(costoxsaco[0]))

with open("tiempo_demora.csv", "r") as file:
    csv_reader = csv.reader(file)
    tiemposdemora = [int(i[0]) for i in csv_reader]

with open("kilos_fruta.csv", "r") as file:
    csv_reader = csv.reader(file)
    kilosfruta = [int(i[0]) for i in csv_reader]

with open("precio_venta.csv", "r") as file:
    precios = list(csv.reader(file))
    for i in range(len(precios)):
        for j in range(len(precios[i])):
            precios[i][j] = int(precios[i][j])

with open("capital_inicial.csv", "r") as file:
    capital = (list(map(lambda x: int(x[0]), csv.reader(file))))[0]
    

with open("cantidad_cuadrantes.csv", "r") as file:
    cuadrantes = range((list(map(lambda x: int(x[0]), csv.reader(file))))[0])

### Modelo
model = Model()

# Variables
x = model.addVars(semillas, cuadrantes, tiempos, vtype=GRB.BINARY, name="x_jkt")
y = model.addVars(semillas, cuadrantes, tiempos, vtype=GRB.BINARY, name="y_jkt")
i = model.addVars(tiempos, vtype=GRB.CONTINUOUS, name="I_t")
u = model.addVars(semillas, tiempos, vtype=GRB.INTEGER, name="u_tj")
w = model.addVars(semillas, tiempos, vtype=GRB.INTEGER, name="w_jt")

model.update()

# Parámetros
alpha = {j: capacidadxsaco[j] for j in semillas}
tetha = {j: tiemposdemora[j] for j in semillas}
lamdba = {j: kilosfruta[j] for j in semillas}
beta = {(j,t): precios[j][t] for j in semillas for t in tiempos}
c = {(j, t): costoxsaco[j][t] for j in semillas for t in tiempos}

# Restricciones
model.addConstrs(
    (quicksum(y[j, k, l] for l in range(
        t, min(t+tetha[j], len(tiempos)-1))) >= tetha[j] * x[j, k, t]
        for j in semillas for k in cuadrantes for t in tiempos),
        name = "Activación sembrado"
)

model.addConstrs(
    (quicksum(y[j, k, t] for j in semillas) <= 1 
    for k in cuadrantes for t in tiempos), 
    name="Solo 1 sembrado por cuadrante"
)

model.addConstrs(
    (i[t] == i[t-1] - quicksum((c[j, t] * w[j, t] for j in semillas)) 
     + quicksum(quicksum(
         x[j, k, t-tetha[j]] * lamdba[j] * beta[j, t] for k in cuadrantes
         ) 
                for j in semillas if t-tetha[j]>=0) for t in tiempos if t>=1),
    name="Inventario de dinero"
)

model.addConstr(
    (i[0] == capital - quicksum(c[j,0] * w[j,0] for j in semillas)), 
    name="Condicion borde inventario dinero"
)

model.addConstrs(
    (u[j, t] == u[j, t-1] + alpha[j] * w[j, t] - quicksum(
        x[j, k, t] for k in cuadrantes) 
        for j in semillas for t in tiempos[1:]), name="Inventario semillas"
)

model.addConstrs(
    (u[j, 0] == alpha[j] * w[j, 0] - quicksum(
        x[j, k, 0] for k in cuadrantes) for j in semillas),
          name="Condicion borde semillas"
)

model.addConstrs(
    (1 - x[j, k, t] >= quicksum(x[j, k, l] for l in range(
        t+1, min(t+tetha[j], len(tiempos))
        ))
    for j in semillas for k in cuadrantes for t in range(len(tiempos)-1)),
    name = "Terminar cosecha antes de volver a cosechar"
)

# Función objetivo
model.setObjective(i[len(tiempos)-1], GRB.MAXIMIZE)

model.optimize()

### Manejo de resultados
# Impresión en consola
print("\n"+"-"*25+"Manejo de resultados"+"-"*25+"\n")

print(f"El valor óptimo del problema es de ${model.objVal}\n")

for k in cuadrantes:
    contador = 0
    for j in semillas:
        for t in tiempos:
            contador += x[j, k, t].x
    print(
        f"En el cuadrante {k+1} se plantaron {int(contador)} "
        f"semillas en un plazo de {len(tiempos)} meses."
    )


# Función auxiliar para mostrar el número de semilla en la tabla
def printeador(k, t):
    for j in semillas:
        if x[j, k, t].x:
            return j+1
    return 0

# Estilizado de la tabla
STYLE = "font-size: 12px; color: #000000; font-weight: 600; border: 1px solid #000000"

# La tabla se realizó fuera de la consola según pedido, para ello
# se crea una ventana con la tabla cuando se ejecuta el código.
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(300, 100, 700, 125)
        self.setWindowTitle(
            "Ocupación de los cuadrantes en el tiempo según tipo de semilla"
            )
        
        grid = QGridLayout()
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)

        posiciones = [(i,j) for i in range(1, len(cuadrantes)+1)
                       for j in range(1, len(tiempos)+1)]
        valores = [(k, t) for k in cuadrantes for t in tiempos]


        meses = QLabel("Meses:")
        meses.setStyleSheet(STYLE)
        grid.addWidget(meses, 0, 0)

        for k in cuadrantes:
            cuadrante = QLabel(f"Cuadrante {k+1}:")
            cuadrante.setStyleSheet(STYLE)
            grid.addWidget(cuadrante, k+1, 0)

        for m in tiempos:
            mes = QLabel(f"{m}")
            mes.setStyleSheet(STYLE)
            grid.addWidget(mes, 0, m+1)
            
        for posicion, valor in zip(posiciones, valores):
            cuadro = QLabel(f"{printeador(valor[0], valor[1])}")
            cuadro.setStyleSheet(STYLE)
            grid.addWidget(cuadro, *posicion)

        self.setLayout(grid)

# Una vez se crea la ventana, se debe mostrar al ejecutar el código,
# y cerrarse cuando se aprete el botón de cerrar ventana.
if __name__ == "__main__":
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())