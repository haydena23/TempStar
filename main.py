import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
from PyQt5 import uic
from setupUI import setupUI

class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gbx.ui', self)
        self.character = None
        self.lockTemplate = False
        setupUI(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MyApplication()
    mainWindow.show()
    sys.exit(app.exec_())