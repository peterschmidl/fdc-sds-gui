from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QFileDialog, QGroupBox

class DiskWindow(QWidget):
    def __init__(self, disk_number, parent=None):
        super().__init__(parent)
        self.controller = None
        self.init_ui(disk_number)

    def init_ui(self, disk_number):
        self.group_box = QGroupBox(f"Disk {disk_number}")
        self.inner_layout = QVBoxLayout()

        self.path_text = QTextEdit()
        self.path_text.setReadOnly(True)
        self.path_text.setFixedHeight(28)

        self.inner_layout.addWidget(self.path_text)

        self.load_button = QPushButton("Load")
        self.unload_button = QPushButton("Unload")
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.load_button)
        self.h_layout.addWidget(self.unload_button)

        self.inner_layout.addLayout(self.h_layout)
        self.group_box.setLayout(self.inner_layout)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.group_box)
        self.setLayout(self.v_layout)        

    def set_controller(self, controller):
        self.controller = controller
        self.load_button.clicked.connect(self.controller.handle_load_click)
        self.unload_button.clicked.connect(self.controller.handle_unload_click)

    def get_path(self):
        return QFileDialog.getOpenFileName(self, "Select Altair Disk Image to load", "", "Disk Images (*.dsk)")[0]

    def set_path(self, path):
        self.path_text.setPlainText(path)