from mazapanes import Ui_MainWindow

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from pathlib import Path

class Inicio(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Inicio()
    window.show();
    sys.exit(app.exec())