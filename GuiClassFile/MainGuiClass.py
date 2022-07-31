import sys
from PySide6.QtWidgets import *


class MainGui(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('라이엇 자동 로그인')
        self.setGeometry(300, 100, 400, 700)

        self.setLayout(self.main_layout)
        self.show()


class SettGui(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainGui()
    sys.exit(app.exec_())
