# main.py
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Battery Test Analyzer")
layout = QVBoxLayout()

label = QLabel("Hello, Aziz! PyQt6 is working.")
layout.addWidget(label)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
