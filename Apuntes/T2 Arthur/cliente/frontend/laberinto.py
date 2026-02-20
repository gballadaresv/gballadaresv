import sys
import os
from PyQt6.QtCore import Qt, QObject, QTimer, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QMessageBox

class LoboVertical():
    def __init__(self, posicion_inicial, largo, maze_layout, col, grid_layout):
        self.posicion = posicion_inicial
        self.col = col
        self.largo = largo
        self.direccion = 1
        self.maze_layout = maze_layout
        self.grid_layout = grid_layout
        self.lobo_vertical = QLabel()
        self.lobo_vertical.setFixedSize(35, 35)
        lobo_vertical_pixmap = QPixmap('../assets/sprites/lobo_vertical_abajo_1.png')
        self.lobo_vertical.setPixmap(lobo_vertical_pixmap)
        self.lobo_vertical.setScaledContents(True)
        self.timer = QTimer()
        self.timer.timeout.connect(self.mover)
        self.timer.start(500)

    def stop(self):
        self.timer.stop()

    def mover(self):
        siguiente = self.posicion + self.direccion

        if 0 <= siguiente < self.largo and self.maze_layout[siguiente] != 'P':
            self.posicion = siguiente
        else:
            self.direccion *= -1

        self.grid_layout.addWidget(self.lobo_vertical, self.posicion, self.col)

class LoboHorizontal():
    def __init__(self, posicion_inicial, largo, maze_layout, fila, grid_layout):
        self.posicion = posicion_inicial
        self.fila = fila
        self.largo = largo
        self.direccion = 1
        self.maze_layout = maze_layout
        self.grid_layout = grid_layout
        self.lobo_vertical = QLabel()
        self.lobo_vertical.setFixedSize(35, 35)
        lobo_vertical_pixmap = QPixmap('../assets/sprites/lobo_horizontal_derecha_1.png')
        self.lobo_vertical.setPixmap(lobo_vertical_pixmap)
        self.lobo_vertical.setScaledContents(True)
        self.timer = QTimer()
        self.timer.timeout.connect(self.mover)
        self.timer.start(500)

    def stop(self):
        self.timer.stop()

    def mover(self):
        siguiente = self.posicion + self.direccion

        if 0 <= siguiente < self.largo and self.maze_layout[siguiente] != 'P':
            self.posicion = siguiente
        else:
            self.direccion *= -1

        self.grid_layout.addWidget(self.lobo_vertical, self.fila, self.posicion)

class Cannon(QObject):
    def __init__(self, fila, col, direccion, maze_layout, grid_layout):
        super().__init__()
        self.fila = fila
        self.col = col
        self.direccion = direccion
        self.maze_layout = maze_layout
        self.grid_layout = grid_layout
        self.cannon = QLabel()
        self.cannon.setFixedSize(35, 35)
        pixmap_cannon = QPixmap(self.Pixmap_path(direccion))
        self.cannon.setPixmap(pixmap_cannon)
        self.cannon.setScaledContents(True)
        self.grid_layout.addWidget(self.cannon, self.fila, self.col)
        
        self.zanahorias = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.disparar)
        self.timer.start(1000)

    def disparar(self):
        zanahoria = Zanahoria(self.fila, self.col, self.direccion, self.maze_layout, self.grid_layout)
            
        self.zanahorias.append(zanahoria)

        self.grid_layout.addWidget(zanahoria.zanahoria, self.fila, self.col)

        for zanahoria in self.zanahorias.copy():
            if not self.en_rango(zanahoria.fila, zanahoria.col):
                self.zanahorias.remove(zanahoria)
                zanahoria.timer.stop()
                zanahoria.zanahoria.deleteLater()

    def en_rango(self, fila, col):
        return 0 <= fila < len(self.maze_layout) and 0 <= col < len(self.maze_layout[0])

    def Pixmap_path(self, direction):
        cannon_path = {
            'CU': '../assets/sprites/canon_arriba.png',
            'CD': '../assets/sprites/canon_abajo.png',
            'CL': '../assets/sprites/canon_izquierda.png',
            'CR': '../assets/sprites/canon_derecha.png',
        }
        return (cannon_path.get(direction))

class Zanahoria(QObject):
    def __init__(self, fila, col, direccion, maze_layout, grid_layout):
        super().__init__()
        self.fila = fila
        self.col = col
        self.direccion = direccion
        self.maze_layout = maze_layout
        self.grid_layout = grid_layout
        self.zanahoria = QLabel()
        self.zanahoria.setFixedSize(35, 35)
        pixmap_zanahoria = QPixmap(self.Pixmap_path(direccion))
        self.zanahoria.setPixmap(pixmap_zanahoria)
        self.zanahoria.setScaledContents(True)
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(200)

    def move(self):
        if self.direccion == 'CU':
            self.fila -= 1
        elif self.direccion == 'CD':
            self.fila += 1
        elif self.direccion == 'CL':
            self.col -= 1
        elif self.direccion == 'CR':
            self.col += 1

        if 0 <= self.fila < len(self.maze_layout) and 0 <= self.col < len(self.maze_layout[0]) and self.maze_layout[self.fila][self.col] != 'P':
            self.grid_layout.addWidget(self.zanahoria, self.fila, self.col)
        else:
            self.timer.stop()
            self.zanahoria.deleteLater()

    def Pixmap_path(self, direction):
        zanahoria_path = {
            'CU': '../assets/sprites/zanahoria_arriba.png',
            'CD': '../assets/sprites/zanahoria_abajo.png',
            'CL': '../assets/sprites/zanahoria_izquierda.png',
            'CR': '../assets/sprites/zanahoria_derecha.png',
        }
        return (zanahoria_path.get(direction))

class Laberinto(QWidget):
    def __init__(self, maze_layouts):
        super().__init__()

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.maze_layouts = maze_layouts
        self.nivel_laberinto = 0
        self.tamano = 16
        self.maze_layout = self.maze_layouts[self.nivel_laberinto]
        
        self.posicion_conejo = self.posicion_inicial('C')

        self.lista_lobos_vertical = []
        self.lista_lobos_horizontal = []
        self.lista_zanahorias = []
        self.lista_cannons = []

        self.initGrid()
        self.initLobos()
        self.initConejo()
        self.initCannons()

    def posicion_inicial(self, tipo_elemento, fila = None, col = None):
        if fila is not None and col is not None:
            return [fila, col]
        for fila in range(self.tamano):
            for col in range(self.tamano):
                if self.maze_layout[fila][col] == tipo_elemento:
                    return [fila, col]

    def Pixmap_path(self, tipo_elemento):
        elemento = {
            '-': '../assets/sprites/bloque_fondo.jpeg',
            'P': '../assets/sprites/bloque_pared.jpeg',
            'BM': '../assets/sprites/manzana_burbuja.png',
            'BC': '../assets/sprites/congelacion_burbuja.png',
            'LH': '../assets/sprites/lobo_horizontal_derecha_1.png',
            'LV': '../assets/sprites/lobo_vertical_abajo_1.png',
            'CU': '../assets/sprites/canon_arriba.png',
            'CD': '../assets/sprites/canon_abajo.png',
            'CL': '../assets/sprites/canon_izquierda.png',
            'CR': '../assets/sprites/canon_derecha.png',
            'E': '../assets/sprites/bloque_fondo.jpeg',
            'C': '../assets/sprites/bloque_fondo.jpeg',
            'S': '../assets/sprites/bloque_fondo.jpeg'
        }
        return (elemento.get(tipo_elemento))

    def initGrid(self):
        for fila in range(self.tamano):
            for col in range(self.tamano):
                casilla = QLabel()
                casilla.setFixedSize(35, 35)
                casilla.setStyleSheet("border: 1px solid black;")
                
                if self.maze_layout[fila][col] == 'P':
                    pixmap = QPixmap('../assets/sprites/bloque_pared.jpeg')
                else:
                    pixmap = QPixmap('../assets/sprites/bloque_fondo.jpeg')
                casilla.setPixmap(pixmap)
                casilla.setScaledContents(True)
                self.grid_layout.addWidget(casilla, fila, col)

    def initConejo(self):
        self.conejo = QLabel()
        self.conejo.setFixedSize(35, 35)

        conejo_pixmap = QPixmap('../assets/sprites/conejo.png')
        self.conejo.setPixmap(conejo_pixmap)
        self.conejo.setScaledContents(True)
        self.grid_layout.addWidget(self.conejo, *self.posicion_conejo)

    def initLobos(self):
        for fila in range(self.tamano):
            for col in range(self.tamano):
                if self.maze_layout[fila][col] == 'LH':
                    lobo_horizontal = LoboHorizontal(self.posicion_inicial('LH', fila, col)[1], self.tamano, self.maze_layout[fila], fila, self.grid_layout)
                    self.lista_lobos_horizontal.append(lobo_horizontal)
                if self.maze_layout[fila][col] == 'LV':
                    fila_col = [self.maze_layout[f][col] for f in range(self.tamano)]
                    lobo_vertical = LoboVertical(self.posicion_inicial('LV', fila, col)[0], self.tamano, fila_col, col, self.grid_layout)
                    self.lista_lobos_vertical.append(lobo_vertical)

    def initCannons(self):
        for fila in range(self.tamano):
            for col in range(self.tamano):
                if self.maze_layout[fila][col] in ('CU', 'CD', 'CL', 'CR'):
                    direccion = self.maze_layout[fila][col]
                    cannon = Cannon(fila, col, direccion, self.maze_layout, self.grid_layout)
                    self.lista_cannons.append(cannon)

    def stopLobos(self):
        for lobo_vertical in self.lista_lobos_vertical:
            lobo_vertical.stop()
        for lobo_horizontal in self.lista_lobos_horizontal:
            lobo_horizontal.stop()

    def moverConejo(self, direccion):
        x, y = self.posicion_conejo

        if direccion == 'W':
            x = max(0, x - 1)
        elif direccion == 'A':
            y = max(0, y - 1)
        elif direccion == 'S':
            x = min(self.tamano - 1, x + 1)
        elif direccion == 'D':
            y = min(self.tamano - 1, y + 1)

        if self.maze_layout[x][y] != 'P' \
            and self.maze_layout[x][y] != 'CD' \
                and self.maze_layout[x][y] != 'CU' \
                    and self.maze_layout[x][y] !='CL' \
                        and self.maze_layout[x][y] !='CR':
            if self.maze_layout[x][y] == 'S':
                if self.nivel_laberinto < len(self.maze_layouts) - 1:
                    self.siguiente_nivel()
                else:
                    self.fin_de_laberintos()
            else:
                self.posicion_conejo = [x, y]
                self.grid_layout.addWidget(self.conejo, *self.posicion_conejo)

    def siguiente_nivel(self):
        self.nivel_laberinto += 1
        self.maze_layout = self.maze_layouts[self.nivel_laberinto]
        self.tamano = 16
        self.posicion_conejo = self.posicion_inicial('C')
        
        self.stopLobos()

        for zanahoria in self.lista_zanahorias:
            zanahoria.stop()
        self.lista_zanahorias = []

        for i in reversed(range(self.grid_layout.count())): 
            self.grid_layout.itemAt(i).widget().setParent(None) # Sacado de, https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt

        self.initGrid()
        self.initConejo()
        self.initLobos()
        self.initCannons()

    def fin_de_laberintos(self):
        msg = QMessageBox()
        msg.setWindowTitle("Fin de Juego")
        msg.setText("Se terminaron los laberintos")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)

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

    Laberinto_Juego = Laberinto(maze_layouts)
    Laberinto_Juego.show()
    sys.exit(app.exec())
