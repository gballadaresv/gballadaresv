from backend.funciones_cliente import validacion_formato
from PyQt6.QtCore import QObject, pyqtSignal

class LogicaInicio(QObject):
    
    senal_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    # SACADO DE AYUDANTIA DE DCCRUSH AND SMACK
    def comprobar_usuario(self, usuario):
        error = []
        valid = True
        if validacion_formato(usuario) == False:
            valid = False
            error.append('Usuario')
        if valid:
            self.senal_abrir_juego.emit(usuario)
        self.senal_validacion.emit(valid, error)


if __name__ == '__main__':
    logica = LogicaInicio()
    logica.comprobar_usuario('Arthur123')
