from PyQt5.QtWidgets import QComboBox

from class_types import *
from mappings import *
from changeClass import changeClass

def configureUI(self):
    configClassComboBox(self)
    
"""
Configure Class ComboBox
"""
def configClassComboBox(self):
    self.classComboBox = self.findChild(QComboBox, 'classComboBox')
    self.classComboBox.currentIndexChanged.connect(self.on_class_changed)
    
def on_class_changed(self):
    selected_class_name = self.classComboBox.currentText()
    selected_class_type = class_type_mapping.get(selected_class_name)

    if selected_class_type:
        changeClass(self, selected_class_type)