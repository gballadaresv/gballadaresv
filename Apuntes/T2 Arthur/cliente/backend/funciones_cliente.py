def validacion_formato(nombre:str) -> bool:
    contador_mayusculas = 0
    contador_numeros = 0

    if not nombre.isalnum():
        return (False)

    if len(nombre) < 3 or len(nombre) > 16:
        return (False)

    for caracter in nombre:
        if caracter.isupper():
            contador_mayusculas += 1
        if caracter.isdigit():
            contador_numeros += 1
    if contador_mayusculas == 0 or contador_numeros == 0:
        return (False)

    return (True)
# DONE

def riesgo_mortal(laberinto: list[list]) -> bool:
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if laberinto[fila][columna] == 'C':
                f = fila
                c = columna

    lista_items = []
    indice_f = f
    indice_c = c
    # IZQUIERDA
    while True:
        if laberinto[f][indice_c - 1] == '-':
            indice_c -= 1
        else:
            lista_items.append([laberinto[f][indice_c - 1], [f, indice_c - 1]])
            indice_c = c
            break
    # DERECHA
    while True:
        if laberinto[f][indice_c + 1] == '-':
            indice_c += 1
        else:
            lista_items.append([laberinto[f][indice_c + 1], [f, indice_c + 1]])
            indice_c = c
            break
    # ARRIBA
    while True:
        if laberinto[indice_f - 1][c] == '-':
            indice_f -= 1
        else:
            lista_items.append([laberinto[indice_f - 1][c], [indice_f - 1, c]])
            indice_f = f
            break
    # ABAJO
    while True:
        if laberinto[indice_f + 1][c] == '-':
            indice_f += 1
        else:
            lista_items.append([laberinto[indice_f + 1][c], [indice_f + 1, c]])
            indice_f = f
            break

    lista_riesgos = []
    for item in lista_items:
        if item[0] != 'P':
            lista_riesgos.append(item)

    contador = 0
    for item in lista_riesgos:
        if item[0] == 'LV':
            if item[1][1] == c:
                contador += 1
        if item[0] == 'LH':
            if item[1][0] == f:
                contador += 1
        if item[0] == 'CU':
            if item[1][1] == c and item[1][0] > f:
                contador += 1
        if item[0] == 'CD':
            if item[1][1] == c and item[1][0] < f:
                contador += 1
        if item[0] == 'CR':
            if item[1][0] == f and item[1][1] < c:
                contador += 1
        if item[0] == 'CL':
            if item[1][0] == f and item[1][1] > c:
                contador += 1

    if contador == 0:
        return (False)
    else:
        return (True)
# DONE

def usar_item(item: str, inventario: list) -> tuple[bool, list]:
    lista = inventario.copy()
    if item in lista:
        pos = lista.index(item)
        lista.pop(pos)
        return (True, lista)
    else:
        return (False, lista)
# DONE

def calcular_puntaje(tiempo: int, vidas: int, cantidad_lobos: int, PUNTAJE_LOBO: int) -> float:
    try:
        puntaje_nivel = (tiempo * vidas) / (cantidad_lobos * PUNTAJE_LOBO)
        puntaje_nivel = round(puntaje_nivel, 2)
        return (puntaje_nivel)
    except ZeroDivisionError as zero:
        return (float(0))
# DONE

def validar_direccion(laberinto: list[list], tecla: str) -> bool:
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if laberinto[fila][columna] == 'C':
                fila_conejo = fila
                columna_conejo = columna
    
    try:
        if tecla == 'W':
            if laberinto[fila_conejo - 1][columna_conejo] == '-'\
                 or laberinto[fila_conejo - 1][columna_conejo] == 'S':
                return (True)
            else:
                return (False)
        
        elif tecla == 'S':
            if laberinto[fila_conejo + 1][columna_conejo] == '-'\
                 or laberinto[fila_conejo + 1][columna_conejo] == 'S':
                return (True)
            else:
                return (False)
        
        elif tecla == 'A':
            if laberinto[fila_conejo][columna_conejo - 1] == '-'\
                 or laberinto[fila_conejo][columna_conejo - 1] == 'S':
                return (True)
            else:
                return (False)
        
        elif tecla == 'D':
            if laberinto[fila_conejo][columna_conejo + 1] == '-'\
                 or laberinto[fila_conejo][columna_conejo + 1] == 'S':
                return (True)
            else:
                return (False)

    except IndexError as rango:
        return (False)
# DONE


# AGREGADO

def rango_pieza(laberinto: list[list], pieza: str) -> int:
    pass