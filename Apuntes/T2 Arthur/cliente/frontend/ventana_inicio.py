import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal
from frontend.ventana_juego import MenuJuego
#from ventana_juego import MenuJuego

class MenuPrincipal(QMainWindow):

    senal_login = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Principal")
        self.setGeometry(50, 50, 800, 600)  # Adjusted the window size
        self.setStyleSheet('background-color: lightgreen')
        self.desplegar()
        self.show()

    def desplegar(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # LOGO
        self.logo = QLabel(self)
        ruta = os.path.join('../assets/sprites/logo.png')
        pixeles = QPixmap(ruta)
        self.logo.setPixmap(pixeles)
        self.layout.addWidget(self.logo)

        # Input del usuario
        self.usuario = QLineEdit(self)
        self.usuario.setPlaceholderText("Ingrese su nombre de usuario")
        self.layout.addWidget(self.usuario)

        # Agregar botones
        self.boton_jugar = QPushButton("Jugar", self)

        self.boton_jugar.clicked.connect(self.enviar_login) # SENAL

        self.layout.addWidget(self.boton_jugar)

        self.boton_cerrar = QPushButton("Salir", self)
        self.boton_cerrar.clicked.connect(self.close)
        self.layout.addWidget(self.boton_cerrar)

        # Salon de la fama
        self.rankings = QGridLayout()
        self.layout.addLayout(self.rankings)

        valores = [
                    'Jugador_1', 'Puntos',
                   'Jugador_2', 'Puntos',
                   'Jugador_3', 'Puntos',
                   'Jugador_4', 'Puntos',
                   'Jugador_5', 'Puntos'
                   ]

        posiciones = [(i, j) for i in range(5) for j in range(2)]
        
        for posicion, valor in zip(posiciones, valores):
            ranking = QLabel(valor, self)
            self.rankings.addWidget(ranking, *posicion)
        
    def enviar_login(self):
        self.senal_login.emit(self.usuario.text())

    def recibir_validacion(self, valid, error):
        if valid:
            self.hide()
        else:
            self.usuario.setPlaceholderText('')
            if 'Usuario' in error:
                self.usuario.setPlaceholderText('Usuario invalido')
            self.usuario.setText('')


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    DCConejo_Chico = QApplication(sys.argv)
    juego = MenuPrincipal()
    sys.exit(DCConejo_Chico.exec())