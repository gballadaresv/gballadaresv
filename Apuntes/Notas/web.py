T = [7, 7, 5.8, 1]
I = [6.6, 4.1]
E = [7, 7, 5.4, 3.5]
C = [6.6, 7, 5, 6.3, 6.7, 1, 6.6]

def nota_tareas(T):
    PT = sum(T) / len(T)
    return PT

def nota_interrogaciones(I):
    NI = sum(I) / len(I)
    return NI

def nota_grupal(E):
    NE = sum(E) / len(E)
    return NE

def nota_controles(C):
    NC = sum(C) / len(C)
    return NC

def promedio_final(PT, NI, NE, NC):
    NF = PT * 0.16 + NI * 0.24 + NE * 0.56 + NC * 0.04
    return NF

def aprueba(PT, NI, NE, NC, NF):
    if NF < 3.95:
        return print(f"No aprueba, nota final {NF}")
    elif PT < 4:
        return print(f"No aprueba, nota tareas {PT}")
    elif NI < 4:
        return print(f"No aprueba, nota catedra {NI}")
    elif NE < 4:
        return print(f"No aprueba, nota grupal {NE}")
    elif E[3] < 3.5:
        return print(f"No aprueba, nota E4 {E[3]}")
    else:
        return print(f"Aprueba, nota tareas: {PT}, nota catedra: {NI}, nota grupal: {NE}, nota controles: {NC}, nota final: {NF}")
    

if __name__ == "__main__":
    PT = nota_tareas(T)
    NI = nota_interrogaciones(I)
    NE = nota_grupal(E)
    NC = nota_controles(C)
    NF = promedio_final(PT, NI, NE, NC)
    aprueba(PT, NI, NE, NC, NF)