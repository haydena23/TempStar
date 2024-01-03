import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from initUI import initUI

# Work in progress
from stylesheets import dark_mode_style

class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gbx.ui', self)
        
        # Work in progress
        self.setStyleSheet(dark_mode_style)
        
        self.character = None
        self.lockTemplate = bool
        initUI(self)
    
    def lockTemp(self):
        self.lockTemplate == True
    def unlockTemp(self):
        self.lockTemplate == False

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MyApplication()
    mainWindow.show()
    sys.exit(app.exec_())