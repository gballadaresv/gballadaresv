import sys

from frontend.ventana_inicio import MenuPrincipal
from frontend.ventana_juego import MenuJuego
from backend.logica_inicio import LogicaInicio

from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # INSTANCIAR VENTANAS
    ventana_inicio = MenuPrincipal()
    ventana_juego = MenuJuego()

    # INSTANCIAR LOGICAS
    logica_inicio = LogicaInicio()

    ventana_inicio.senal_login.connect(logica_inicio.comprobar_usuario)

    logica_inicio.senal_validacion.connect(
        ventana_inicio.recibir_validacion)
    logica_inicio.senal_abrir_juego.connect(ventana_juego.desplegar)

    app.exec()