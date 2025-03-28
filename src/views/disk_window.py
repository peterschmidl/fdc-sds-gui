from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class DiskWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.label = QLabel(f"Disk")
        self.load_button = QPushButton("Load")
        self.unload_button = QPushButton("Unload")
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.load_button)
        self.h_layout.addWidget(self.unload_button)
        
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.h_layout)
        
        self.setLayout(self.layout)
        # Connect signals and slots
        self.load_button.clicked.connect(self.on_load_button_click)

    def on_load_button_click(self):
        self.label.setText("Button Clicked!")