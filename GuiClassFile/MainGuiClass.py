import sys
from PySide6.QtWidgets import *


class MainGui(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('라이엇 자동 로그인')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainGui()
    sys.exit(app.exec_())
