import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
from PyQt5 import uic
from newCharacter import create_new_character_on_open
from mappings import *
from changeClass import changeClass

class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gbx.ui', self)
        self.character = None
        self.lockTemplate = False
        create_new_character_on_open(self)
        self.classComboBox = self.findChild(QComboBox, 'classComboBox')
        self.classComboBox.currentIndexChanged.connect(self.on_class_changed)
        
        print(self.character.melee_skills)
    
    def on_class_changed(self):
        selected_class_name = self.classComboBox.currentText()
        selected_class_type = class_type_mapping.get(selected_class_name)
        print(selected_class_type)
        if selected_class_type:
            changeClass(self, selected_class_type)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MyApplication()
    mainWindow.show()
    sys.exit(app.exec_())