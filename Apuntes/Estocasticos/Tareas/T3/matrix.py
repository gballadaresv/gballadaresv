import numpy as np
import sympy as sp

# Parámetros simbólicos
p, lmbda, mu = sp.symbols('p lambda mu')

# List of states (must match your graph)
#Orden de estados según tu imagen (sin espacios)
states = [
    "(0,0,0,0)",
    "(A,0,0,0)",
    "(B,0,0,0)",
    "(A,A,0,0)",
    "(A,B,0,0)",
    "(B,B,0,0)",
    "(A,A,A,0)",
    "(A,A,B,0)",
    "(A,B,A,0)",
    "(A,B,B,0)",
    "(B,B,A,0)",
    "(B,B,B,0)",
    "(A,A,A,B)",
    "(A,A,B,B)",
    "(A,B,A,B)",
    "(A,B,B,B)",
    "(B,B,A,B)",
    "(B,B,B,B)"
]

state_idx = {s: i for i, s in enumerate(states)}
n = len(states)
Q = sp.zeros(n, n)

edges = [
    # Llegadas tipo A (azul)
    ("(0,0,0,0)", "(A,0,0,0)", p*lmbda),
    ("(A,0,0,0)", "(A,A,0,0)", p*lmbda),
    ("(A,A,0,0)", "(A,A,A,0)", p*lmbda),
    ("(B,0,0,0)", "(A,B,0,0)", p*lmbda),
    ("(A,B,0,0)", "(A,B,A,0)", p*lmbda),
    ("(B,B,0,0)", "(B,B,A,0)", p*lmbda),

    # Llegadas tipo B (verde)
    ("(0,0,0,0)", "(B,0,0,0)", (1-p)*lmbda),
    ("(B,0,0,0)", "(B,B,0,0)", (1-p)*lmbda),
    ("(B,B,0,0)", "(B,B,B,0)", (1-p)*lmbda),
    ("(A,0,0,0)", "(A,B,0,0)", (1-p)*lmbda),
    ("(A,B,0,0)", "(A,B,B,0)", (1-p)*lmbda),
    ("(A,B,B,0)", "(A,B,B,B)", (1-p)*lmbda),
    ("(B,B,A,0)", "(B,B,A,B)", (1-p)*lmbda),
    ("(A,B,A,0)", "(A,B,A,B)", (1-p)*lmbda),
    ("(A,A,0,0)", "(A,A,B,0)", (1-p)*lmbda),
    ("(A,A,B,0)", "(A,A,B,B)", (1-p)*lmbda),
    ("(A,A,A,0)", "(A,A,A,B)", (1-p)*lmbda),

    # Salidas tipo A (rojo)
    ("(A,0,0,0)", "(0,0,0,0)", mu),
    ("(A,A,0,0)", "(A,0,0,0)", mu),
    ("(A,A,A,0)", "(A,A,0,0)", mu),
    ("(A,A,A,B)", "(A,B,A,0)", mu),
    ("(A,B,A,0)", "(A,B,0,0)", mu),
    ("(A,B,0,0)", "(B,0,0,0)", mu),
    ("(A,A,B,0)", "(A,B,0,0)", mu),
    ("(A,A,B,B)", "(A,B,B,0)", mu),
    ("(A,B,B,0)", "(B,B,0,0)", mu),
    ("(A,B,A,B)", "(B,B,A,0)", mu),
    ("(A,B,B,B)", "(B,B,B,0)", mu),

    # Salidas tipo B (amarillo)
    ("(B,0,0,0)", "(0,0,0,0)", mu),
    ("(B,B,0,0)", "(B,0,0,0)", mu),
    ("(B,B,B,0)", "(B,B,0,0)", mu),
    ("(B,B,B,B)", "(B,B,B,0)", mu),
    ("(B,B,A,B)", "(B,B,A,0)", mu),
    ("(B,B,A,0)", "(A,B,0,0)", mu),
    ("(A,B,B,B)", "(A,B,B,0)", mu),
    ("(A,B,B,0)", "(A,B,0,0)", mu),
    ("(A,B,0,0)", "(A,0,0,0)", mu),
    ("(A,B,A,B)", "(A,B,A,0)", mu),
    ("(A,B,A,0)", "(A,A,0,0)", mu),
]

# Fill the Q-matrix
for src, dst, rate in edges:
    i, j = state_idx[src], state_idx[dst]
    Q[i, j] = rate

# Set diagonals so each row sums to zero
for i in range(n):
    Q[i, i] = -sp.simplify(sum(Q[i, :]))

# Print the Q-matrix
sp.pprint(Q)

with open("Q_matrix.csv", "w", encoding="utf-8") as f:
    # Encabezados entre comillas dobles
    f.write(',"' + '","'.join(states) + '"\n')
    for i in range(n):
        row = [str(Q[i, j]) for j in range(n)]
        f.write(f'"{states[i]}",' + ",".join(row) + "\n")


# Exportar la matriz Q a LaTeX con encabezados de estados
with open("Q_matrix_bmatrix.tex", "w", encoding="utf-8") as f:
    f.write("\\begin{bmatrix}\n")
    for i in range(n):
        row = [sp.latex(Q[i, j]) for j in range(n)]
        f.write(" & ".join(row) + " \\\\\n")
    f.write("\\end{bmatrix}\n")


