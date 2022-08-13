import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('라이엇 자동 로그인')
        self.setGeometry(300, 300, 300, 350)

        self.main_layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()

        self.account_plus_button = QPushButton('계정 추가')
        self.setting_button = QPushButton('설정')
        self.riot_start_button = QPushButton('게임 실행')

        self.scroll_area = QScrollArea()
        self.account_list_widget = QWidget()  # 계정 표시 나열되는 위젯
        self.scroll_area.setWidget(self.account_list_widget)

        self.account_list_layout = QHBoxLayout()  # -> account_list_widget 에 포함

        self.show()
        self._init_widget()
        self._init_ui()

    def _init_ui(self):
        # main layout
        self.setLayout(self.main_layout)

        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.scroll_area)

        # button layout
        self.button_layout.addWidget(self.account_plus_button, Qt.AlignTop)
        self.button_layout.addWidget(self.setting_button, Qt.AlignCenter)
        self.button_layout.addSpacerItem(QSpacerItem(5, 140))
        self.button_layout.addWidget(self.riot_start_button, Qt.AlignBottom)

        # list account widget
        self.account_list_widget.setLayout(self.account_list_layout)
        # list account layout

        for i in range(10):
            self.account_list_layout.addWidget(AccountWidget(i, 1234, 1234))

    def _init_widget(self):
        # ----- button -----
        # account plus button
        self.account_plus_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.account_plus_button.setMaximumHeight(40)
        # setting button
        self.setting_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setting_button.setMaximumHeight(40)
        # riot start button
        self.riot_start_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.riot_start_button.setMaximumHeight(70)

    def append_account_to_layout(self):
        pass


# Todo 그리드에 idx = 0 라디오버튼(0,0) , AccountWidget(인덱스0 ~~ )(0,1) -> idx=1 라디오 (1,0 형식으로 예상
class AccountWidget(QWidget):
    """
    MainWindow.account_list_layout 에 포함되는 Widget
    """

    def __init__(self, account_idx: int, account_id: str, account_pw: str):
        super().__init__()
        # self.setFixedSize(100,25)
        self.account_idx = account_idx
        self.id = account_id
        self.pw = account_pw

        self.main_layout = QGridLayout()

        self.id_label = QLabel('아이디')
        self.edit_password_button = QPushButton('+')
        self.delete_account_button = QPushButton('-')

        self._init_widget()
        self._init_ui()

    def _init_ui(self):
        # main layout
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.id_label, 0, 0)
        self.main_layout.addWidget(self.edit_password_button, 0, 1)
        self.main_layout.addWidget(self.delete_account_button, 0, 2)

    def _init_widget(self):
        # main layout
        self.main_layout.setColumnStretch(0, 2)
        self.main_layout.setColumnStretch(1, 1)
        self.main_layout.setColumnStretch(2, 1)
        # edit_password_button
        # TODO: edit_password_button -> click -> QDialog: password 변경 gui open
        # delete_account_button
        # TODO: 구상 아직...


def main_gui_open() -> None:
    app = QApplication(sys.argv)
    widget = MainWindow()
    # widget = AccountWidget(0, '1234', '1234')
    sys.exit(app.exec())


if __name__ == '__main__':
    main_gui_open()
