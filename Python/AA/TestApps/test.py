import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QIcon
 
# create a class for the main window
class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setwindowTitle = "Test Analyzer"
        self.windowIcon = QIcon("/Users/azizbaubaid/Library/Mobile Documents/com~apple~CloudDocs/Documents/2. Deutschland/Programmierung/HTML/icons8-graph-arcade/icons8-graph-64.png") # Icon von https://icons8.com
        self.resize(500, 350) #width, height
        # create a layout object
        layout = QVBoxLayout()
        self.setLayout(layout)
        # create a text edit widget
        self.inputField = QLineEdit()
        self.button = QPushButton("&Say Hello!", clicked=self.sayHello)
        self.output = QTextEdit()
        # add widgets to the layout
        layout.addWidget(self.inputField)
        layout.addWidget(self.button)
        layout.addWidget(self.output)
        # connect the button to the sayHello method
    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText("Hello, {0}!".format(inputText))
        
app = QApplication(sys.argv)
# styling with CSS
app.setStyleSheet('''
    QWidget {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
        font-size: 25px;
    }
    QLineEdit {
        border: 1px solid #ccc;
        padding: 5px;
    }
    QPushButton {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px;
        cursor: pointer;
        font-size: 20px;
    }
    QPushButton:hover {
        background-color: #0056b3;
    }
    QTextEdit {
        border: 1px solid #ccc;
        padding: 5px;
    }
''')

window = myApp()
window.show()
            
sys.exit(app.exec())
 
