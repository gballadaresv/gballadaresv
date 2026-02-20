I1 = 3.33
I2 = 4.82
T = 6.48
EX = 1.4000
pPG = [0.06, 0.1, 0.12, 0.2, 0.02, 0.1, 0.18, 0.02, 0.1, 0.1]
nPG = [5.03, 6.23, 6.1, 6.66, 5.94, 6.21, 5.52, 1.0000, 5.94, 5.54]
PG = sum([a*b for a,b in zip(pPG, nPG)])

def aprueba(I1, I2, T, EX, PG):
    NF = 0.125 * I1 + 0.125 * I2 + 0.15 * T + 0.20 * EX + 0.40 * PG
    prom = (I1 + I2 + EX + T) / 4
    if prom < 4:
        return print(f"No aprueba, promedio catedra {prom}")
    elif PG < 4:
        return print(f"No aprueba, proyecto grupal {PG}")
    elif NF < 4:
        return print(f"No aprueba, nota final {NF}")
    return print(f"Aprueba, nota final: {NF}, promedio catedra: {prom}, proyecto grupal: {PG}")

if __name__ == "__main__":
    aprueba(I1, I2, T, EX, PG)