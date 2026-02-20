import numpy as np
import matplotlib.pyplot as plt

Personas = ["Dani", "Marce", "Rai"]

# Puntajes Teóricos
Ptj_teo = [[34.0, 68.0, 102.0, 136.0, 170.0],
           [15.0, 30.0, 45.0, 60.0, 75.0],
           [32.0, 64.0, 96.0, 128.0, 160.0]]


# Definir las tasas de llegadas
lambda_l = 17.0
lambda_c = 0.5
lambda_t = 40.0
tasas = [lambda_l, lambda_c, lambda_t*0.8]

# Inicializar Ptj_exp
Ptj_exp = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Puntos de multiplicación
puntos = [2.0, 30.0, 1.0]

# Simular la distribución de Poisson para cada tasa
for i in range(5):
    for l in range(3):
        llegadas = 0
        puntaje = 0
        for ll in range(1000):
            tiempo_simu = 0.0
            while tiempo_simu <= i+1:
                muestras = np.random.exponential(1 / tasas[l], 1)
                tiempo_simu += muestras[0]
                if tiempo_simu <= i+1:
                    llegadas += 1
        llegadas /= 1000
        puntaje = llegadas * puntos[l]
        Ptj_exp[l][i] = puntaje
        print(Ptj_exp)

# Imprimir resultados
for i in range(len(Ptj_exp)):
    print(f"Puntaje Teo {Personas[i]} = {Ptj_teo[i]}")
    print(f"Puntaje Exp {Personas[i]} = {Ptj_exp[i]}")
    print("---------------")


# Graficar
x = np.arange(1, 6)

# Graficar con líneas sólidas y líneas punteadas
plt.scatter(x, Ptj_teo[0], label="Ptj Daniel Teórico", linestyle='-', color='blue')
plt.scatter(x, Ptj_exp[0], label="Ptj Daniel Experimental", linestyle='--', color='red')
plt.scatter(x, Ptj_teo[1], label="Ptj Marcelo Teórico", linestyle='-', color='green')
plt.scatter(x, Ptj_exp[1], label="Ptj Marcelo Experimental", linestyle='--', color='brown')
plt.scatter(x, Ptj_teo[2], label="Ptj Raimundo Teórico", linestyle='-', color='black')
plt.scatter(x, Ptj_exp[2], label="Ptj Raimundo Experimental", linestyle='--', color='orange')

# Añadir etiquetas y leyenda
plt.xlabel("Hora")
plt.ylabel("Puntaje")
plt.title("Puntaje por hora")
plt.legend()

# Mostrar la gráfica
plt.show()
