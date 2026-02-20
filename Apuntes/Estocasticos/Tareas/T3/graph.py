from graphviz import Digraph

# Crea el grafo dirigido usando el motor 'dot' para jerarquía
dot = Digraph(engine="dot")
dot.attr(rankdir='TB', size='10,8')  # Top-Bottom, tamaño ajustable

# Define los estados (nodos)
states = [
    "(0, 0, 0, 0)",
    "(A, 0, 0, 0)", "(B, 0, 0, 0)",
    "(A, A, 0, 0)", "(A, B, 0, 0)", "(B, B, 0, 0)",
    "(A, A, A, 0)", "(A, A, B, 0)", "(A, B, A, 0)", "(A, B, B, 0)", "(B, B, A, 0)", "(B, B, B, 0)",
    "(A, A, A, B)", "(A, A, B, B)", "(A, B, A, B)", "(A, B, B, B)", "(B, B, A, B)", "(B, B, B, B)"
]

# Agrupa nodos por niveles (ranks)
dot.body += [
    '{rank=same; "(0, 0, 0, 0)";}',
    '{rank=same; "(A, 0, 0, 0)"; "(B, 0, 0, 0)";}',
    '{rank=same; "(A, A, 0, 0)"; "(A, B, 0, 0)"; "(B, B, 0, 0)";}',
    '{rank=same; "(A, B, A, 0)"; "(A, B, B, 0)";}',
    '{rank=same; "(A, A, A, 0)"; "(A, A, B, 0)"; "(B, B, A, 0)"; "(B, B, B, 0)";}',
    '{rank=same; "(A, A, A, B)"; "(A, B, A, B)"; "(B, B, A, B)"; "(B, B, B, B)";}',
    '{rank=same; "(A, A, B, B)"; "(A, B, B, B)";}',
]

# Agrega los nodos al grafo
for state in states:
    dot.node(state, state)

# Define las transiciones (aristas) con colores
edges = [
    # Azules
    ("(0, 0, 0, 0)", "(A, 0, 0, 0)", "blue"),
    ("(A, 0, 0, 0)", "(A, A, 0, 0)", "blue"),
    ("(A, A, 0, 0)", "(A, A, A, 0)", "blue"),
    ("(B, 0, 0, 0)", "(A, B, 0, 0)", "blue"),
    ("(A, B, 0, 0)", "(A, B, A, 0)", "blue"),
    ("(B, B, 0, 0)", "(B, B, A, 0)", "blue"),
    # Verdes
    ("(0, 0, 0, 0)", "(B, 0, 0, 0)", "green"),
    ("(B, 0, 0, 0)", "(B, B, 0, 0)", "green"),
    ("(B, B, 0, 0)", "(B, B, B, 0)", "green"),
    ("(B, B, B, 0)", "(B, B, B, B)", "green"),
    ("(A, 0, 0, 0)", "(A, B, 0, 0)", "green"),
    ("(A, B, 0, 0)", "(A, B, B, 0)", "green"),
    ("(A, B, B, 0)", "(A, B, B, B)", "green"),
    ("(B, B, A, 0)", "(B, B, A, B)", "green"),
    ("(A, B, A, 0)", "(A, B, A, B)", "green"),
    ("(A, A, 0, 0)", "(A, A, B, 0)", "green"),
    ("(A, A, B, 0)", "(A, A, B, B)", "green"),
    ("(A, A, A, 0)", "(A, A, A, B)", "green"),
    # Rojas
    ("(A, 0, 0, 0)", "(0, 0, 0, 0)", "red"),
    ("(A, A, 0, 0)", "(A, 0, 0, 0)", "red"),
    ("(A, A, A, 0)", "(A, A, 0, 0)", "red"),
    ("(A, A, A, B)", "(A, B, A, 0)", "red"),
    ("(A, B, A, 0)", "(A, B, 0, 0)", "red"),
    ("(A, B, 0, 0)", "(B, 0, 0, 0)", "red"),
    ("(A, A, B, 0)", "(A, B, 0, 0)", "red"),
    ("(A, A, B, B)", "(A, B, B, 0)", "red"),
    ("(A, B, B, 0)", "(B, B, 0, 0)", "red"),
    ("(A, B, A, B)", "(B, B, A, 0)", "red"),
    ("(A, B, B, B)", "(B, B, B, 0)", "red"),
    # Amarillas
    ("(B, 0, 0, 0)", "(0, 0, 0, 0)", "yellow"),
    ("(B, B, 0, 0)", "(B, 0, 0, 0)", "yellow"),
    ("(B, B, B, 0)", "(B, B, 0, 0)", "yellow"),
    ("(B, B, B, B)", "(B, B, B, 0)", "yellow"),
    ("(B, B, A, B)", "(B, B, A, 0)", "yellow"),
    ("(B, B, A, 0)", "(A, B, 0, 0)", "yellow"),
    ("(A, B, B, B)", "(A, B, B, 0)", "yellow"),
    ("(A, B, B, 0)", "(A, B, 0, 0)", "yellow"),
    ("(A, B, 0, 0)", "(A, 0, 0, 0)", "yellow"),
    ("(A, B, A, B)", "(A, B, A, 0)", "yellow"),
    ("(A, B, A, 0)", "(A, A, 0, 0)", "yellow"),
]

# Agrega las aristas al grafo
for src, dst, color in edges:
    dot.edge(src, dst, color=color)

# Guarda y muestra el grafo
dot.render('grafo_markov', format='png')