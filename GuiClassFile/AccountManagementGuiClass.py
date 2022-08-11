import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class Management(QWidget):
    def __init__(self):
        super(Management, self).__init__()
        self.setWindowTitle('계정 관리')
        self.setGeometry(300, 300, 300, 350)

        self.main_layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()

        self.account_plus_button = QPushButton('계정 추가')
        self.riot_start_button = QPushButton('게임 실행')

        self.scroll_area = QScrollArea()
        self.list_account_widget = QWidget()
        self.scroll_area.setWidget(self.list_account_widget)

        self._init_widget()
        self._init_ui()

    def _init_ui(self):
        # main layout
        self.setLayout(self.main_layout)

        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.scroll_area)

        # button layout
        self.button_layout.addWidget(self.account_plus_button, Qt.AlignTop)
        self.button_layout.addSpacerItem(QSpacerItem(20, 200))
        self.button_layout.addWidget(self.riot_start_button, Qt.AlignBottom)

    def _init_widget(self):
        # ----- button -----
        # account plus button
        # riot start button
        self.riot_start_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.riot_start_button.setMaximumHeight(70)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Management()
    widget.show()
    sys.exit(app.exec())
