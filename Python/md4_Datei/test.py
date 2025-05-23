import sys
from qtpy.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from qtpy.QtGui import QIcon
 
### create a class for the main window
class myApp(QWidget):
    def __init__(self):
        super().__init__()
        
app = QApplication(sys.argv)

window = myApp()
window.show()
            

sys.exit(app.exec_())
 
