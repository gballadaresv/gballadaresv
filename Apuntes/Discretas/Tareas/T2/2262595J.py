def reemplazar_simolo(w: str, a: str, b: str) -> str:
    # El caso base es una palabra vacia
    new_word = ""
    # Cada iteracion del for es el paso inductivo de la funcion
    for i in w:
        if i == a:
            # Se utiliza la definicion inductiva del conjunto de palabras
            new_word += b
        else:
            new_word += i
    return new_word


w = input("Ingrese una palabra: ")
a = input("Ingrese el simbolo a reemplazar: ")
b = input("Ingrese el simbolo de reemplazo: ")
print(reemplazar_simolo(w, a, b))