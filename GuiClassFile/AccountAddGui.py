import sys
from PySide6.QtWidgets import QApplication ,QDialog, QGridLayout, QLineEdit, QPushButton, QLabel

class Account(QDialog):
    def __init__(self):
        super().__init__()

        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)

        self.id_label = QLabel('Id')
        self.pw_label = QLabel('Pw')
        self.id_lineedit = QLineEdit()
        self.id_lineedit.displayText()
        self.pw_lineedit = QLineEdit()
        
        self.accept_button = QPushButton('저장')
        self._init_ui()
        self.show()
    
    def _init_ui(self):
        self.main_layout.addWidget(self.id_label, 0, 0)
        self.main_layout.addWidget(self.pw_label, 1, 0)

        self.main_layout.addWidget(self.id_lineedit, 0, 1)
        self.main_layout.addWidget(self.pw_lineedit, 1, 1)
        self.main_layout.addWidget(self.accept_button, 0, 2)

def open_account_append():
    app = QApplication(sys.argv)
    widget = Account()
    sys.exit(app.exec())

if __name__ == '__main__':
    open_account_append()
