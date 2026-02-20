import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMessageBox

class Reloj(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cuenta Regresiva")
        self.setGeometry(100, 100, 300, 150)

        self.tiempo_inicial = 120
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.timer.start(1000)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.update_label()

    def actualizar_tiempo(self):
        if self.tiempo_inicial > 0:
            self.tiempo_inicial -= 1
            self.update_label()
        else:
            self.timer.stop()
            self.show_popup()

    def update_label(self):
        minutos = self.tiempo_inicial // 60
        segundos = self.tiempo_inicial % 60
        tiempo = f"{minutos:02d}:{segundos:02d}"
        self.label.setText(tiempo)

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Game Over")
        msg.setStyleSheet('background-color: lightgreen')
        msg.setText("Se acabo")
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    reloj = Reloj()
    reloj.show()
    sys.exit(app.exec())
