import sys
from PyQt5 import QtWidgets , uic

class iniciar:
     def __init__(self):
          app = QtWidgets.QApplication ([])
          self.ventana = uic.loadUi("interfaz.ui")
          self.ventana.show ()
          
          self.ventana.actionsalir.triggered.connect(self.click_actionsalir)
          self.ventana.actionitems.triggered.connect(self.click_actionitems)
          app.exec()
     def click_actionitems(self):
     
    
     def click_actionsalir(self):
         sys.exit()

       
            