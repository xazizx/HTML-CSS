# import modules
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

# main app objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(500, 350) #width, height

# create all app objects
title = QLabel('Random Keywords')

text1 = QLabel('?')
text2 = QLabel('?')
text3 = QLabel('?')
text4 = QLabel('0')

button1 = QPushButton('Click Me')
button2 = QPushButton('Click Me')
button3 = QPushButton('Click Me')
button4 = QPushButton('Reset')

# design the layout
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()

## add widgets to the layout
row1.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignmentFlag.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

row4.addWidget(button4, alignment=Qt.AlignmentFlag.AlignTrailing)
row4.addWidget(text4, alignment=Qt.AlignmentFlag.AlignLeading)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)
master_layout.addLayout(row4)
## set the layout to the main window
main_window.setLayout(master_layout)

# create functions
myWords = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
counter_value = 0  # global counter variable, so that it can be accessed in all functions

def random_word1():
    word = choice(myWords)
    text1.setText(word)
def random_word2():
    word = choice(myWords)
    text2.setText(word)
def random_word3():
    word = choice(myWords)
    text3.setText(word)
    
def reset(): # reset all text fields and counter
    global counter_value # to access the global variable and not create a new local one
    text1.setText('?')
    text2.setText('?')
    text3.setText('?')
    text4.setText('0')
    counter_value = 0

def counter():  # each time a button is clicked, the counter increases
    global counter_value
    counter_value += 1
    text4.setText(str(counter_value))
    
## creating wrapper functions to call more than one function
def random_word1_and_count():
    random_word1()
    counter()
def random_word2_and_count():
    random_word2()
    counter()
def random_word3_and_count():
    random_word3()
    counter()
    
# create events
button1.clicked.connect(random_word1_and_count)
button2.clicked.connect(random_word2_and_count)
button3.clicked.connect(random_word3_and_count)
button4.clicked.connect(reset)

 
main_window.show()
sys.exit(app.exec())