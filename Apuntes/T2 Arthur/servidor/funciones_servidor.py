def usuario_permitido(nombre: str, usuarios_no_permitidos: list[str]) -> bool:
    if nombre in usuarios_no_permitidos:
        return (False)
    else:
        return (True)
# DONE

def serializar_mensaje(mensaje: str) -> bytearray:
    
    mensaje_serializado = bytearray(mensaje.encode("utf-8"))
    return (mensaje_serializado)
# DONE

def separar_mensaje(mensaje: bytearray) -> list[bytearray]:
    Mensaje = mensaje.copy()
    orden = 0
    parte1 = bytearray(b'')
    parte2 = bytearray(b'')
    parte3 = bytearray(b'')

    while Mensaje:
        if len(Mensaje) >= 3:
            parteA, parteB, parteC = Mensaje[0:3]
            Mensaje = Mensaje[3:]
            if orden == 0:
                parte1.append(parteA)
                parte2.append(parteB)
                parte3.append(parteC)
                orden += 1

            elif orden == 1:
                parte3.append(parteA)
                parte2.append(parteB)
                parte1.append(parteC)
                orden -= 1

        elif len(Mensaje) == 2:
            parteA, parteB = Mensaje[0:2]
            Mensaje = bytearray(b'')
            if orden == 0:
                parte1.append(parteA)
                parte2.append(parteB)
                orden += 1

            elif orden == 1:
                parte3.append(parteA)
                parte2.append(parteB)
                orden -= 1

        elif len(Mensaje) == 1:
            parteA = Mensaje[0]
            Mensaje = bytearray(b'')
            if orden == 0:
                parte1.append(parteA)

            elif orden == 1:
                parte3.append(parteA)


    lista = [parte1, parte2, parte3]

    return(lista)
# DONE

def encriptar_mensaje(mensaje: bytearray) -> bytearray:
    pA, pB, pC = separar_mensaje(mensaje)
    
    byte_A = pA[0]
    byte_B = pB[-1]
    byte_C = pC[0]

    bytes_ = byte_A + byte_B + byte_C

    n = bytearray(b'')
    if bytes_ % 2 == 0:
        n.extend(b'1')
        n.extend(pA)
        n.extend(pC)
        n.extend(pB)
    
    if bytes_ % 2 != 0:
        n.extend(b'0')
        n.extend(pB)
        n.extend(pA)
        n.extend(pC)
    
    return(n)
# DONE

def codificar_mensaje(mensaje: bytearray) -> list[bytearray]:
    copia = mensaje.copy()

    lista_bytes = []
    parte1 = bytearray(len(copia).to_bytes(4, 'big'))
    lista_bytes.append(parte1)

    contador = 1
    while True:
        parte2 = bytearray(contador.to_bytes(4, 'big'))
        lista_bytes.append(parte2)
        if len(copia) > 36:
            Mensaje = bytearray(copia[0:36])
            copia = copia[36:]
            lista_bytes.append(Mensaje)
            contador += 1
        elif len(copia) == 36:
            Mensaje = bytearray(copia)
            lista_bytes.append(Mensaje)
            break
        elif len(copia) < 36:
            largo = 36 - len(copia)
            Mensaje = bytearray(copia)
            Mensaje.extend(bytearray(largo))
            lista_bytes.append(Mensaje)
            break

    return (lista_bytes)
# DONE