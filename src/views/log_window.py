from datetime import datetime
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel


class LogWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.log_label = QLabel("Log")
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setMinimumHeight(200)

        layout.addWidget(self.log_label)
        layout.addWidget(self.log_output)
        self.setLayout(layout)

    def append(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        cursor = self.log_output.textCursor()
        cursor.movePosition(QTextCursor.Start)
        cursor.insertText(f"[{timestamp}] {message}\n")
