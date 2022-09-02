import sys
import os
from PySide6.QtWidgets import QApplication, QDialog, QGridLayout, QLineEdit, QPushButton, QLabel

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CsvDataProcessingModule import add_account


class Account(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('계정 추가')

        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)

        self.id_label = QLabel('Id')
        self.pw_label = QLabel('Pw')
        self.id_lineedit = QLineEdit()
        self.pw_lineedit = QLineEdit()

        self.accept_button = QPushButton('저장')
        self.accept_button.clicked.connect(self.clicked_accept_button)
        self._init_ui()
        self.show()

    def _init_ui(self):
        self.main_layout.addWidget(self.id_label, 0, 0)
        self.main_layout.addWidget(self.pw_label, 1, 0)

        self.main_layout.addWidget(self.id_lineedit, 0, 1)
        self.main_layout.addWidget(self.pw_lineedit, 1, 1)
        self.main_layout.addWidget(self.accept_button, 0, 2)

    def clicked_accept_button(self):
        """
        accept_button 클릭시 호출
        클릭시 accountCsvData.csv 에 입력된 id, pw 를 추가하는 함수
        :return:
            Dialog 닫기
        """
        account_id = self.id_lineedit.text()
        account_pw = self.pw_lineedit.text()
        add_account(account_id, account_pw)
        return self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Account()
    sys.exit(app.exec())
