import sys
import os
from PySide6.QtWidgets import (
    QDialog,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QLabel
)
from PySide6.QtCore import Qt

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CsvDataProcessingModule import add_account, is_duplicate_value

class NoneValueError(Exception):pass
# An error that occurs when there is no data value

class OverlapValueError(Exception):pass
# An error that occurs when data values are duplicated


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
        self.account_id = self.id_lineedit.text().strip()
        self.account_pw = self.pw_lineedit.text().strip()

        try:
            self.check_id_overlap()
            self.check_none_value()

        except OverlapValueError:
            message = "중복된 아이디입니다.\n 다른계정으로 로그인하세요."
            error_gui = ErrorDialog(message)
            error_gui.exec()

        except NoneValueError:
            message = "입력되지 않은 칸이 있습니다.\n전부 입력해주세요."
            error_gui = ErrorDialog(message)
            error_gui.exec()

        else:
            self.close_dialog()

    def check_id_overlap(self):
        """
        id 중복확인하는 함수
        """
        if is_duplicate_value(self.account_id):
            raise OverlapValueError

    def check_none_value(self):
        """
        입력된 데이터가 없는지 확인하는 함수
        :return:
            두 칸이 비워져있을 경우: 종료
            한 칸만 비워져있을 경우: 에러 발생
        """
        if self.account_id == "" and self.account_pw == "": # 두 칸다 비웠을 때
            self.close()

        elif self.account_id == "" or self.account_pw == "": # 한 칸만 비웠을 때
            raise NoneValueError
            
    def close_dialog(self):
        """
        dialog 를 끝내는 함수
        """
        add_account(self.account_id, self.account_pw)
        return self.close()





        
        

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    widget = Account()
    # widget = ErrorDialog('에러메세지입니다 고쳐주세요')
    sys.exit(app.exec())
