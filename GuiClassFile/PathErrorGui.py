from PySide6.QtWidgets import *
import sys


class PathError(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 100)
        self.setFixedSize(400, 100)
        self.setWindowTitle('클라이언트 경로 지정')

        self.main_layout = QGridLayout(self)
        self.riot_path_lineEdit = QLineEdit()
        self.setPath_button = QPushButton('설정')
        self.close_button = QPushButton('확인')

        self.init_ui()
        self.init_widget()

    def init_ui(self):
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.riot_path_lineEdit, 0, 0, 2, 1)
        self.main_layout.addWidget(self.setPath_button, 0, 1, 1, 1)
        self.main_layout.addWidget(self.close_button, 1, 1, 1, 1)
        self.main_layout.setRowStretch(1, 1)

    def init_widget(self):
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
        self.path_save()
        self.close()

    def path_save(self) -> None:
        """
        경로를 로컬에 저장해주는 함수 -> page_close 에서 호출
        """
        file_path = self.riot_path_lineEdit.text()
        print(file_path)  # TODO 로컬파일 저장으로 바꾸기


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = PathError()
    widget.show()
    sys.exit(app.exec())
