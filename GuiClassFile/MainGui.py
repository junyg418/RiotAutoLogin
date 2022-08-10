import sys
from PySide6.QtWidgets import *


class MainGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('라이엇 자동 로그인')
        self.setGeometry(300, 100, 300, 200)
        self.setFixedSize(300, 200)

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self._init_widget()
        self._init_ui()
        self.show()

    def _init_widget(self):
        pass

    def _init_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainGui()
    sys.exit(app.exec_())
