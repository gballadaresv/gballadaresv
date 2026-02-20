import sys
import os
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDialog
from PyQt6.QtCore import pyqtSignal, Qt
from frontend.reloj import Reloj
from frontend.laberinto import Laberinto

class MenuJuego(QWidget):
    senal_abrir_juego = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DCConejoChico")
        self.setGeometry(50, 50, 800, 600)
        self.setStyleSheet('background-color: lightgreen')

    def desplegar(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Un layout horizontal para el reloj y el inventario
        layout_inventario_reloj_botones = QHBoxLayout()

        # INVENTARIO
        self.widget_inventario = QWidget()
        layout_inventario = QVBoxLayout()
        self.widget_inventario.setLayout(layout_inventario)
        label_inventario = QLabel("Inventario")
        layout_inventario.addWidget(label_inventario)
        layout_inventario_reloj_botones.addWidget(self.widget_inventario)

        # RELOJ
        self.widget_reloj = QWidget()
        layout_reloj = QVBoxLayout()
        self.widget_reloj.setLayout(layout_reloj)
        label_reloj = Reloj()
        label_reloj.setStyleSheet("border: 1px solid black;")
        layout_reloj.addWidget(label_reloj)
        layout_inventario_reloj_botones.addWidget(self.widget_reloj)

        # BOTONES
        # Un layout horizontal para el reloj y el inventario
        layout_botones = QVBoxLayout()
        
        self.boton_cerrar = QPushButton("Salir", self)
        self.boton_cerrar.clicked.connect(self.close)
        layout_botones.addWidget(self.boton_cerrar)

        self.boton_pausar = QPushButton("Pausa", self)
        layout_botones.addWidget(self.boton_pausar)

        layout_inventario_reloj_botones.addLayout(layout_botones)

        # LABERINTO
        maze_layouts = []

        laberinto1 = os.path.join('../assets/laberintos/tablero_1.txt')
        laberinto2 = os.path.join('../assets/laberintos/tablero_2.txt')
        laberinto3 = os.path.join('../assets/laberintos/tablero_3.txt')
        lista_rutas = [laberinto1, laberinto2, laberinto3]

        for ruta in lista_rutas:
            with open(ruta, 'r') as maze:
                laberinto = []
                lineas = maze.readlines()
                for linea in lineas:
                    fila = linea.strip().split(',')
                    laberinto.append(fila)
            maze_layouts.append(laberinto)

        self.widget_laberinto = Laberinto(maze_layouts)

        # Agregar el reloj e inventario en la parte superior de la ventana
        self.widget_inventario_reloj = QWidget()
        self.widget_inventario_reloj.setLayout(layout_inventario_reloj_botones)
        self.layout.addWidget(self.widget_inventario_reloj)

        # Agregar el laberinto abajo
        self.layout.addWidget(self.widget_laberinto)

        self.show()
        self.senal_abrir_juego.emit()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_W:
            self.widget_laberinto.moverConejo('W')
        elif key == Qt.Key.Key_A:
            self.widget_laberinto.moverConejo('A')
        elif key == Qt.Key.Key_S:
            self.widget_laberinto.moverConejo('S')
        elif key == Qt.Key.Key_D:
            self.widget_laberinto.moverConejo('D')
        

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    DCConejo_Chico = QApplication(sys.argv)
    juego = MenuJuego()
    sys.exit(DCConejo_Chico.exec())

