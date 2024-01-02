from PyQt5.QtWidgets import QComboBox, QListWidget, QPushButton

from Models.classes import *
from Models.races import *
from Models.mappings import *

from changeFunctions import *

from newCharacter import create_new_character_on_open

def initUI(main_window):
    create_new_character_on_open(main_window)
    
    # Configure UI components
    configClassComboBox(main_window, class_type_mapping, changeClass)
    configRaceComboBox(main_window, race_type_mapping, changeRace)
    configItemsListWidget(main_window, setSlotSelectionLabel)
    configRealmRankComboBox(main_window, realm_rank_map, changeRealmRank)
    configUnequipAllButton(main_window, unquipAllSlotsWarning)
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
    if selected_race_type:
        change_race_callback(main_window, selected_race_type)

"""
Configure Items ListWidget
"""
def configItemsListWidget(main_window, set_slot_selection_callback):
    main_window.itemsListWidget = main_window.findChild(QListWidget, 'itemsListWidget')
    main_window.itemsListWidget.itemClicked.connect(lambda: on_items_list_widget_clicked(main_window, set_slot_selection_callback))

def on_items_list_widget_clicked(main_window, set_slot_selection_callback):
    selected_item = main_window.itemsListWidget.currentItem()
    if selected_item:
        selected_text = selected_item.text()
        set_slot_selection_callback(main_window, selected_text)
    ## Todo
    ## Fill information box with item details
    
"""
Configure Realm Rank ComboBox
"""
def configRealmRankComboBox(main_window, realm_rank_map, change_realm_rank_callback):
    main_window.realmRankComboBox = main_window.findChild(QComboBox, 'realmRankComboBox')
    main_window.realmRankComboBox.currentIndexChanged.connect(lambda: on_realm_rank_changed(main_window, realm_rank_map, change_realm_rank_callback))

def on_realm_rank_changed(main_window, realm_rank_map, change_realm_rank_callback):
    realmRankRaw = main_window.realmRankComboBox.currentText()
    realmRank = realm_rank_map.get(realmRankRaw)
    if realmRank:
        change_realm_rank_callback(main_window, realmRank)
        
"""
Configure Unequip All Items Push Button
"""

def configUnequipAllButton(main_window, unequip_all_button_callback):
    main_window.unequipAllButton = main_window.findChild(QPushButton, 'unequipAllButton')
    main_window.unequipAllButton.clicked.connect(lambda: on_unequip_all_pressed(main_window, unequip_all_button_callback))

def on_unequip_all_pressed(main_window, unequip_all_button_callback):
    unequip_all_button_callback(main_window)