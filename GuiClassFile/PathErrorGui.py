from PySide6.QtWidgets import *
import sys


class PathError(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 100)
        self.setFixedSize(400, 100)
        self.setWindowTitle('클라이언트 경로 지정')

        self.main_layout = QGridLayout()
        self.riot_path_lineEdit = QLineEdit()
        self.setPath_button = QPushButton('버튼')
        self.close_button = QPushButton('확인')

        self.init_ui()
        self.init_widget()


    def init_ui(self):
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.riot_path_lineEdit, 0, 0, 2, 1)
        self.main_layout.addWidget(self.setPath_button, 0, 1, 1, 1)
        self.main_layout.addWidget(self.close_button, 1, 1, 1, 1)
        self.main_layout.setRowStretch(1,1)
    

    def init_widget(self):
        # ---- lineEdit
        self.riot_path_lineEdit.setReadOnly(True)
        # ---- setPath_Button
        self.setPath_button.clicked.connect(self.findPath)

    
    def findPath(self):
        '''
        클라이언트 경로를 지정해주는 함수 -> setPath_button 누르면 호출
        '''
        file_path = QFileDialog.getOpenFileName(self, 'select Riot_Clint', 'C:/', filter='*.exe')
        self.riot_path_lineEdit.setText(file_path[0])
        # print(file_path[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = PathError()
    widget.show()
    sys.exit(app.exec())
