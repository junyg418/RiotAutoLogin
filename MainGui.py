import sys
import os
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from CsvDataProcessingModule import MainGuiCsvdataProcess

from GuiClassFile import AccountAddGui

import ImageFIndModule
import RiotRunModule


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('라이엇 자동 로그인')
        self.setGeometry(300, 300, 300, 350)
        self.setFixedSize(300, 350)

        self.main_layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()

        # button layout
        self.account_plus_button = QPushButton('계정 추가')
        self.setting_button = QPushButton('설정')
        self.riot_start_button = QPushButton('게임 실행')

        # right_layout
        self.scroll_area = QScrollArea()
        self.account_list_widget = AccountWidget()  # 계정 표시 나열되는 위젯

        self._init_ui()
        self._init_widget()
        self.set_AccountWidget()
        self.show()

    def _init_ui(self):
        # main layout
        self.setLayout(self.main_layout)

        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.scroll_area)

        # button layout -> (left_layout)
        self.button_layout.addWidget(self.account_plus_button, Qt.AlignTop)
        self.button_layout.addWidget(self.setting_button, Qt.AlignCenter)
        self.button_layout.addSpacerItem(QSpacerItem(5, 140))
        self.button_layout.addWidget(self.riot_start_button, Qt.AlignBottom)

    def _init_widget(self):
        # ----- Button -----
        # account plus button
        self.account_plus_button.clicked.connect(self.clicked_account_plus_button)
        self.account_plus_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.account_plus_button.setMaximumHeight(40)

        # setting button
        self.setting_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setting_button.setMaximumHeight(40)

        # riot start button
        self.riot_start_button.clicked.connect(self.click_riot_start_button)
        self.riot_start_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.riot_start_button.setMaximumHeight(70)

    def set_AccountWidget(self):
        return self.scroll_area.setWidget(self.account_list_widget)

    def click_riot_start_button(self) -> None:
        """
        riot_start_button click 할때 호출되는 함수
        :return:
            None
        """
        account_id, account_password = self.get_username_password()
        # print(f'ac:{account_id}, pw:{account_password}')
        RiotRunModule.run()
        ImageFIndModule.run(account_id, account_password)

    def clicked_account_plus_button(self) -> None:
        """
        account_plus_button 의 click 시그널 발생시 호출되는 함수
        :return:
            AccountAddGui show -> None
        """
        account_add_gui = AccountAddGui.Account()
        account_add_gui.exec()
        time.sleep(10)
        self.new_account_list_widget()


    def new_account_list_widget(self):
        print('생성')
        self.account_list_widget.clear_account_list_layout()
        self.account_list_widget.deleteLater()
        self.account_list_widget = AccountWidget()
        return self.set_AccountWidget()


    def get_username_password(self) -> tuple:
        """
        id, password 반환해주는 함수
        :return:
            (id, password) -> tuple
        """
        selected_button = self.account_list_widget.id_button_group.checkedButton()
        account_id = selected_button.text()
        password = MainGuiCsvdataProcess.get_password_to_id(account_id)
        return account_id, password


class AccountWidget(QWidget):
    def __init__(self):
        super(AccountWidget, self).__init__()
        self.account_list_layout = QVBoxLayout()
        self.setLayout(self.account_list_layout)

        self.id_button_group = QButtonGroup()

        self.set_account_layout()
        self.set_id_button_group()

    def set_account_layout(self) -> None:
        """
        account_layout 에 들어가는 위젯들을 설정시켜주는 함수
        :return:
            self.scroll_area.setWidget(self.account_list_widget) -> 위젯 scroll_area 에 set 시킴
        """
        id_list = MainGuiCsvdataProcess.id_to_list()
        for idx, id_value in enumerate(id_list):
            self.account_list_layout.addWidget(AccountCell(idx, id_value))

    def set_id_button_group(self) -> None:
        """
        id button group 에 버튼들 추가, 기본값 설정하는 함수
        :return:
            None
        """
        # TODO print()삭제
        self.id_button_group.setExclusive(True)

        account_list = self.get_AccountWidget_list()
        for class_element in account_list:
            id_button = class_element.id_button
            self.id_button_group.addButton(id_button)

        default_button_idx = MainGuiCsvdataProcess.get_account_default()
        default_account_button = account_list[default_button_idx].id_button
        default_account_button.setChecked(True)

    # noinspection PyPep8Naming
    def get_AccountWidget_list(self) -> list:
        """
        계정들 리스트를 반환하는 함수
        :return:
            list -> AccountWidget
        """
        return self.findChildren(AccountCell)

    def clear_account_list_layout(self):
        for idx in range(self.account_list_layout.count()):
            widget = self.account_list_layout.itemAt(idx).widget()
            widget.deleteLater()
            del widget


class AccountCell(QWidget):
    """
    MainWindow.account_list_layout 에 포함되는 Widget
    """

    def __init__(self, account_idx: int, account_id: str):
        super().__init__()
        # self.setFixedSize(100,25)
        self.account_idx = account_idx
        self.id = account_id

        self.main_layout = QGridLayout()

        self.id_button = QRadioButton(str(self.id))
        self.edit_password_button = QPushButton('+')
        self.delete_account_button = QPushButton('-')

        self._init_widget()
        self._init_ui()

    def _init_ui(self):
        # main layout
        self.setLayout(self.main_layout)

        self.main_layout.setHorizontalSpacing(3)

        self.main_layout.addWidget(self.id_button, 0, 0)
        self.main_layout.addWidget(self.edit_password_button, 0, 1)
        self.main_layout.addWidget(self.delete_account_button, 0, 2)

    def _init_widget(self):
        # main layout
        self.main_layout.setColumnStretch(0, 3)
        self.main_layout.setColumnStretch(1, 1)
        self.main_layout.setColumnStretch(2, 1)

        # edit_password_button
        # TODO: edit_password_button -> click -> QDialog: password 변경 gui open
        self.edit_password_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.edit_password_button.setFixedSize(30, 30)

        # delete_account_button
        self.delete_account_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.delete_account_button.setFixedSize(30, 30)
        # TODO: 구상 아직...


def main_gui_open() -> None:
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main_gui_open()
