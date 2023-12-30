from PyQt5.QtWidgets import QComboBox

from class_types import *
from mappings import *
from changeClass import changeClass
from newCharacter import create_new_character_on_open

def setupUI(main_window):
    create_new_character_on_open(main_window)
    configClassComboBox(main_window, class_type_mapping, changeClass)
    # configRaceComboBox(main_window, race_type_mapping, changeRace)
    
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
        
"""
Configure Race ComboBox
"""
def configRaceComboBox(main_window, race_type_mapping, change_race_callback):
    main_window.raceComboBox = main_window.findChild(QComboBox, 'raceComboBox')
    main_window.raceComboBox.currentIndexChanged.connect(lambda: on_race_changed(main_window, race_type_mapping, change_race_callback))

def on_race_changed(main_window, race_type_mapping, change_race_callback):
    selected_race_name = main_window.raceComboBox.currentText()
    selected_race_type = race_type_mapping.get(selected_race_name)
    print(selected_race_name)
    if selected_race_type:
        change_race_callback(main_window, selected_race_type)