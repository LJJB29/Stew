from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QLabel
from PyQt6.QtGui import QPixmap
import sys

class StewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stew - Steam Banner Manager")
        self.setGeometry(200, 200, 800, 600)
        
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Game list
        self.game_list = QListWidget()
        self.game_list.addItem("Game 1")
        self.game_list.addItem("Game 2")
        self.layout.addWidget(self.game_list)
        
        # Banner preview
        self.banner_label = QLabel("Select a game to preview its banner")
        self.banner_label.setPixmap(QPixmap("default_banner.png"))
        self.layout.addWidget(self.banner_label)
        
        # Change Banner Button
        self.change_banner_btn = QPushButton("Change Banner")
        self.layout.addWidget(self.change_banner_btn)
        
        # Settings Button
        self.settings_btn = QPushButton("Settings")
        self.layout.addWidget(self.settings_btn)
        
        # Connect buttons (placeholder actions)
        self.change_banner_btn.clicked.connect(self.change_banner)
        self.settings_btn.clicked.connect(self.open_settings)

    def change_banner(self):
        print("Change Banner Clicked")
    
    def open_settings(self):
        print("Settings Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StewApp()
    window.show()
    sys.exit(app.exec())
