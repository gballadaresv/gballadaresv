T = [5.2, 3, 3.22, 4.17]
I = [5.1, 3.93, 3.4000000]

def nota_tareas(T):
    PT = T[0] * 0.2 + T[1] * 0.3 + T[2] * 0.25 + T[3] * 0.25
    return PT

def nota_interrogaciones(I):
    PE = sum(I) / len(I)
    return PE

def promedio_final(PT, PE):
    NF = PT * 0.5 + PE * 0.5
    return NF

def aprueba(PT, PE, NF):
    if PT < 3.7:
        return print(f"No aprueba, nota tareas {PT}")
    elif PE < 3.7:
        return print(f"No aprueba, nota cátedra {PE}")
    elif NF < 3.95:
        return print(f"No aprueba, nota final {NF}")
    return print(f"Aprueba, nota tareas: {PT}, nota catedra: {PE}, nota final: {NF}")

if __name__ == "__main__":
    PT = nota_tareas(T)
    PE = nota_interrogaciones(I)
    NF = promedio_final(PT, PE)
    aprueba(PT, PE, NF)