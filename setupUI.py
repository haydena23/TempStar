from PyQt5.QtWidgets import QComboBox

from class_types import *
from mappings import *
from changeClass import changeClass
from newCharacter import create_new_character_on_open

def setupUI(main_window):
    create_new_character_on_open(main_window)
    configClassComboBox(main_window, class_type_mapping, changeClass)
    
"""
Configure Class ComboBox
"""
def configClassComboBox(main_window, class_type_mapping, change_class_callback):
    main_window.classComboBox = main_window.findChild(QComboBox, 'classComboBox')
    main_window.classComboBox.currentIndexChanged.connect(lambda: on_class_changed(main_window, class_type_mapping, change_class_callback))

def on_class_changed(main_window, class_type_mapping, change_class_callback):
    selected_class_name = main_window.classComboBox.currentText()
    selected_class_type = class_type_mapping.get(selected_class_name)
    if selected_class_type:
        change_class_callback(main_window, selected_class_type)