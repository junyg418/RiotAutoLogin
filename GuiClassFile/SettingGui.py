from PySide6.QtWidgets import (
    QWidget,
    QDialog,

    QGridLayout,

    QLabel,

    QApplication
    )
import sys

class SettingPass(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('미구현 페이지')
        self.setFixedSize(300, 400)

        self.main_layout = QGridLayout()
        self.error_lineedit = QLabel('설정 페이지는 아직 미구현입니다.')

        self._init_ui()

    def _init_ui(self):
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.error_lineedit)

def open_pass_page():
    app = QApplication(sys.argv)
    widget = SettingPass()
    widget.show()
    sys.exit(app.exec())

# class SettingPage(QDialog):
#     def __init__(self) -> None:
#         super().__init__()
        
