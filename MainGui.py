from sys import argv, exit
from time import sleep
from PySide6.QtWidgets import (
    QWidget,

    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,

    QScrollArea,
    QPushButton,
    QRadioButton,
    QSpacerItem,
    QButtonGroup,

    QSizePolicy,
    QApplication
)
from PySide6.QtCore import Qt, QObject, Signal
from CsvDataProcessingModule import MainGuiCsvDataProcess

from GuiClassFile import AccountAddGui

import ImageFIndModule
import RiotRunModule
from GuiClassFile import SettingGui


class ResetSignal(QObject):
    reset_signal = Signal()

    def run(self):
        self.reset_signal.emit()


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.reset_signal_class = ResetSignal()
        self.reset_signal_class.reset_signal.connect(self.new_account_list_widget)

        self.setWindowTitle('자동 로그인')
        self.setGeometry(300, 300, 250, 300)
        self.setFixedSize(270, 300)

        self.main_layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()

        # button layout
        self.account_plus_button = QPushButton('계정 추가')
        self.setting_button = QPushButton('설정')
        self.riot_start_button = QPushButton('게임 실행')

        # right_layout
        self.scroll_area = QScrollArea()
        self.account_list_widget = AccountWidget(self.reset_signal_class)  # 계정 표시 나열되는 위젯

        self._init_ui()
        self._init_widget()
        self.set_AccountWidget()

    def _init_ui(self):
        # main layout
        self.setLayout(self.main_layout)

        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.scroll_area)

        # button layout -> (left_layout)
        self.button_layout.addWidget(self.account_plus_button, Qt.AlignTop)
        self.button_layout.addWidget(self.setting_button, Qt.AlignCenter)
        self.button_layout.addSpacerItem(QSpacerItem(5, 100))
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
        # TODO 곧 삭제 내역
        self.setting_button.clicked.connect(SettingGui.open_pass_page)

        # riot start button
        self.riot_start_button.clicked.connect(self.clicked_riot_start_button)
        self.riot_start_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.riot_start_button.setMaximumHeight(70)
    
    def set_AccountWidget(self):
        """
        AccountWidget 을 scroll_area에 setWidget하는 함수
        """
        return self.scroll_area.setWidget(self.account_list_widget)

    def clicked_riot_start_button(self) -> None:
        """
        riot_start_button click 할때 호출되는 함수
        :return:
            None
        """
        account_id, account_password = self.get_username_password()
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
        sleep(10)
        self.new_account_list_widget()

    def new_account_list_widget(self):
        """
        account_list_widget 을 새로운 인스턴트로 갱신하는 함수
        """
        self.account_list_widget.clear_account_list_layout()
        self.account_list_widget.deleteLater()
        self.account_list_widget = AccountWidget(self.reset_signal_class)
        return self.set_AccountWidget()

    def get_selected_button(self) -> QPushButton:
        """
        현재 선택된 버튼을 반환해주는 함수
        :return:
            QPushButton
        """
        selected_button = self.account_list_widget.id_button_group.checkedButton()
        return selected_button

    def get_username_password(self) -> tuple:
        """
        id, password 반환해주는 함수
        :return:
            (id, password) -> tuple
        """
        selected_button = self.get_selected_button()
        account_id = selected_button.text()
        password = MainGuiCsvDataProcess.get_password_to_id(account_id)
        return account_id, password


class AccountWidget(QWidget):
    def __init__(self, signal_class: ResetSignal):
        super(AccountWidget, self).__init__()
        self.reset_signal_class = signal_class

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
        id_list = MainGuiCsvDataProcess.id_to_list()
        for idx, id_value in enumerate(id_list):
            self.account_list_layout.addWidget(AccountCell(idx, id_value, signal_class=self.reset_signal_class))

    def set_id_button_group(self) -> None:
        """
        id button group 에 버튼들 추가, 기본값 설정하는 함수
        :return:
            None
        """
        self.id_button_group.setExclusive(True)

        account_list = self.get_AccountWidget_list()
        for class_element in account_list:
            id_button = class_element.id_button
            self.id_button_group.addButton(id_button)
        default_button_idx = MainGuiCsvDataProcess.get_account_default()
        if not default_button_idx: return
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
        """
        account_list_layout 에 있는 위젯들을 데이터상 전부 제거하는 함수:
            -> 새롭게 인스턴트 생성시 똑같은 속성의 인스턴트가 중복되는 것을 방지하기 위해
        """
        for idx in range(self.account_list_layout.count()):
            widget = self.account_list_layout.itemAt(idx).widget()
            widget.deleteLater()
            del widget


class AccountCell(QWidget):
    """
    MainWindow 의 상속되는 클라스
    MainWindow.account_list_layout 에 포함되는 Widget
    """

    def __init__(self, account_idx: int, account_id: str, *, signal_class: ResetSignal) -> object:
        """
        :param account_idx:
            accountCsvData.csv 내부의 작성되어 있는 계정의 순서 index
        :param account_id:
            accountCsvData.csv 내부의 작성되어 있는 계정의 아이디
        :param signal_class:
            AccountWidget 을 초기화 하기 위한 reset signal -> MainWindow 에서 signal 받음
        """
        super().__init__()
        self.account_idx = account_idx
        self.id = account_id
        self.reset_signal_class = signal_class

        self.main_layout = QGridLayout()

        self.id_button = QRadioButton(str(self.id))
        self.delete_account_button = QPushButton('-')

        self._init_widget()
        self._init_ui()

    def _init_ui(self):
        # main layout
        self.setLayout(self.main_layout)

        self.main_layout.setHorizontalSpacing(3)

        self.main_layout.addWidget(self.id_button, 0, 0)
        self.main_layout.addWidget(self.delete_account_button, 0, 1)

    def _init_widget(self):
        # main layout
        self.main_layout.setColumnStretch(0, 5)
        self.main_layout.setColumnStretch(1, 1)

        # delete_account_button
        self.delete_account_button.clicked.connect(self.delete_account)
        self.delete_account_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.delete_account_button.setFixedSize(30, 30)

    def delete_account(self):
        MainGuiCsvDataProcess.delete_account(self.account_idx)
        self.reset_signal_class.run()


def main_gui_open() -> None:
    app = QApplication(argv)
    widget = MainWindow()
    widget.show()
    exit(app.exec())


if __name__ == '__main__':
    main_gui_open()
