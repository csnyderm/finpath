#import PyQt6.QtWidgets
#import PySide6
import PyQt6
import PyQt6.QtWidgets
import sys


## Goals:
## ? Review and break down how qrtvsim handled QtWidgets
## ? Decide which formatting I want a basic layout of buttons
## ?


class HomeApplication(PyQt6.QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    
    self.my_layout = PyQt6.QtWidgets.QVBoxLayout(self)
    #self.tabs = PyQt6.QtWidgets.QButtonGroup()
    self.tabs2= PyQt6.QtWidgets.QMenuBar()
    self.demo_menu = PyQt6.QtWidgets.QMenu("Load")
    self.tabs2.addMenu(self.demo_menu)
    #self.my_layout.addWidget(self.tabs)
    self.my_layout.addWidget(self.tabs2)

app = PyQt6.QtWidgets.QApplication([])
widget = HomeApplication()
widget.resize(800,800)
widget.show()

sys.exit(app.exec())