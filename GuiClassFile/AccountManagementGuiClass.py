import sys
from PySide6.QtWidgets import *


class Management(QWidget):
    def __init__(self):
        super(Management, self).__init__()
        self.setWindowTitle('계정 관리')
        self.setGeometry(300, 300, 300, 500)

        self.main_layout = QGridLayout()
        self.account_plus_button = QPushButton('+')
        self.list_account_widget = QWidget()

        self._init_gui()
        self._init_ui()

    def _init_ui(self):
        # main layout
        self.setLayout(self.main_layout)
        self.

    def _init_gui(self):
        pass
