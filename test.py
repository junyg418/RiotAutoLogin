import sys
from PySide6.QtWidgets import QWidget, QApplication, QTextEdit
from PySide6.QtCore import *

ss = Signal()

class CustomSignal:
    def __init__(self) -> None:
        ss.emit()
    # def asd(self):
    #     self.ss.emit()
     
# class SSS(QObject):
#     def run(self):
#         self.ss.emit()

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        ss.connect(self.printaaa)
        
    

    def printaaa(self):
        print('aaa')

App = QApplication(sys.argv)
widget = MainWindow()
sys.exit(App.exec())