import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CsvDataProcessingModule import resetting_path

"""
default_path = C:\Riot Games\Riot Client\RiotClientServices.exe
"""


class PathError(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 100)
        self.setFixedSize(400, 100)
        self.setWindowTitle('클라이언트 경로 지정')
        self.show()

        self.main_layout = QGridLayout(self)
        self.riot_path_lineEdit = QLineEdit()
        self.status_display_label = QLabel('라이엇 클라이언트의 경로를 설정해주세요!')
        self.setPath_button = QPushButton('설정')
        self.close_button = QPushButton('확인')

        self.init_ui()
        self.init_widget()

    def init_ui(self):
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.status_display_label, 0, 0, 1, 1)
        self.main_layout.addWidget(self.setPath_button, 0, 2, 1, 1)

        self.main_layout.addWidget(self.riot_path_lineEdit, 1, 0, 1, 2)
        self.main_layout.addWidget(self.close_button, 1, 2, 1, 1)
        self.main_layout.setColumnStretch(0, 2)
        self.main_layout.setRowStretch(1, 1)

    def init_widget(self):
        # ---- Label
        self.status_display_label.setAlignment(Qt.AlignCenter)
        # ---- lineEdit
        self.riot_path_lineEdit.setReadOnly(True)
        # ---- setPath_Button
        self.setPath_button.clicked.connect(self.find_path)
        # ---- close_button
        self.close_button.clicked.connect(self.page_close)

    def find_path(self) -> None:
        """
        클라이언트 경로를 지정해주는 함수 -> setPath_button 누르면 호출
        """
        file_path = QFileDialog.getOpenFileName(self, 'select Riot_Clint', 'C:/', filter='*.exe')
        self.riot_path_lineEdit.setText(file_path[0])

    def page_close(self):
        if 'RiotClientServices.exe' in self.riot_path_lineEdit.text().split('/'):
            self.path_save()
            self.close()
            import RiotRunModule
            RiotRunModule.run()
        else:
            self.status_display_label.setText('경로가 잘못되었습니다')

    def path_save(self) -> None:
        """
        경로를 로컬에 저장해주는 함수 -> page_close 에서 호출
        """
        file_path = self.riot_path_lineEdit.text()
        resetting_path(file_path)


def open_error_page():
    app = QApplication(sys.argv)
    widget = PathError()
    sys.exit(app.exec())


if __name__ == '__main__':
    open_error_page()
