import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer  # Agrega la importación de QTimer
from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory

# Pines GPIO para cada motor
PIN_MOTOR_IZQUIERDA_FORWARD = 17
PIN_MOTOR_IZQUIERDA_BACKWARD = 27
PIN_MOTOR_DERECHA_FORWARD = 22
PIN_MOTOR_DERECHA_BACKWARD = 23

# Crea los objetos Motor independientes para cada motor
MOTOR_IZQUIERDA = Motor(forward=PIN_MOTOR_IZQUIERDA_FORWARD, backward=PIN_MOTOR_IZQUIERDA_BACKWARD)
MOTOR_DERECHA = Motor(forward=PIN_MOTOR_DERECHA_FORWARD, backward=PIN_MOTOR_DERECHA_BACKWARD)

class MotorControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Control de Motores')

        layout = QVBoxLayout()

        self.btn_izquierda_izquierdo = QPushButton('Mover a la izquierda (Motor Izquierdo)', self)
        self.btn_izquierda_izquierdo.clicked.connect(self.mover_izquierda_izquierdo)
        layout.addWidget(self.btn_izquierda_izquierdo)

        self.btn_derecha_izquierdo = QPushButton('Mover a la derecha (Motor Izquierdo)', self)
        self.btn_derecha_izquierdo.clicked.connect(self.mover_derecha_izquierdo)
        layout.addWidget(self.btn_derecha_izquierdo)

        self.btn_izquierda_derecho = QPushButton('Mover a la izquierda (Motor Derecho)', self)
        self.btn_izquierda_derecho.clicked.connect(self.mover_izquierda_derecho)
        layout.addWidget(self.btn_izquierda_derecho)

        self.btn_derecha_derecho = QPushButton('Mover a la derecha (Motor Derecho)', self)
        self.btn_derecha_derecho.clicked.connect(self.mover_derecha_derecho)
        layout.addWidget(self.btn_derecha_derecho)

        self.setLayout(layout)

    def detener_motor_izquierdo(self):
        MOTOR_IZQUIERDA.stop()

    def detener_motor_derecho(self):
        MOTOR_DERECHA.stop()

    def mover_izquierda_izquierdo(self):
        print("Moviendo a la izquierda (Motor Izquierdo)")
        MOTOR_IZQUIERDA.forward()
        # Detener el motor después de 1 segundo
        QTimer.singleShot(500, self.detener_motor_izquierdo)

    def mover_derecha_izquierdo(self):
        print("Moviendo a la derecha (Motor Izquierdo)")
        MOTOR_IZQUIERDA.backward()
        # Detener el motor después de 1 segundo
        QTimer.singleShot(500, self.detener_motor_izquierdo)

    def mover_izquierda_derecho(self):
        print("Moviendo a la izquierda (Motor Derecho)")
        MOTOR_DERECHA.forward()
        # Detener el motor después de 1 segundo
        QTimer.singleShot(500, self.detener_motor_derecho)

    def mover_derecha_derecho(self):
        print("Moviendo a la derecha (Motor Derecho)")
        MOTOR_DERECHA.backward()
        # Detener el motor después de 1 segundo
        QTimer.singleShot(500, self.detener_motor_derecho)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MotorControl()
    window.show()
    sys.exit(app.exec_())
