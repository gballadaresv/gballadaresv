I1 = 3.37 # Considerar recorrección
I2 = 5.69 
EX = 4.57 # P
CONTROLES = [7, 5, 7, 7, 7, 5, 6, 4.6, 2, 7] # 7 
CONTROLES.sort()
NC = CONTROLES[6:] # El 70% superior de los controles
NC = sum(NC) / len(NC)
CASO1 = 5.2
CASO2 = 5.4

def promedio():
    nota = I1 * 0.2 + I2 * 0.2 + NC * 0.15 + CASO1 * 0.1 + CASO2 * 0.1 + EX * 0.25
    print(nota)
    return nota

def aprueba():
    nota = promedio()
    ni = (I1 + I2 + EX) / 3
    if nota >= 4 and ni >= 4 and EX >= 3:
        return print("Aprueba")
    elif ni < 4:
        return print(f"No aprueba, nota interrograciones {ni}")
    elif EX < 3:
        return print(f"No aprueba, nota examen final {EX}")
    return print("No aprueba por promedio final")
    
if __name__ == "__main__":
    aprueba()