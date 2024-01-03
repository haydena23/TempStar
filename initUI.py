from PyQt5.QtWidgets import QComboBox, QListWidget, QPushButton
from Models.classes import *
from Models.races import *
from Models.mappings import *

from changeFunctions import *

from newCharacter import create_new_character_on_open

def initUI(self):
    create_new_character_on_open(self)
    
    # Configure UI components
    configClassComboBox(self, class_type_mapping, changeClass)
    configRaceComboBox(self, race_type_mapping, changeRace)
    configItemsListWidget(self, setSlotSelectionLabel, setSlotSelectionList, setInformationTextEdit)
    configRealmRankComboBox(self, realm_rank_map, changeRealmRank)
    configUnequipAllButton(self, unquipAllSlotsWarning)
    configSlotSelectionListWidget(self, setItemFromSlotSelection)
"""
Configure Class ComboBox
"""
def configClassComboBox(self, class_type_mapping, change_class_callback):
    self.classComboBox = self.findChild(QComboBox, 'classComboBox')
    self.classComboBox.currentIndexChanged.connect(lambda: on_class_changed(self, class_type_mapping, change_class_callback))

def on_class_changed(self, class_type_mapping, change_class_callback):
    selected_class_name = self.classComboBox.currentText()
    selected_class_type = class_type_mapping.get(selected_class_name)
    if selected_class_type:
        change_class_callback(self, selected_class_type)
        
"""
Configure Race ComboBox
"""
def configRaceComboBox(self, race_type_mapping, change_race_callback):
    self.raceComboBox = self.findChild(QComboBox, 'raceComboBox')
    self.raceComboBox.currentIndexChanged.connect(lambda: on_race_changed(self, race_type_mapping, change_race_callback))

def on_race_changed(self, race_type_mapping, change_race_callback):
    selected_race_name = self.raceComboBox.currentText()
    selected_race_type = race_type_mapping.get(selected_race_name)
    if selected_race_type:
        change_race_callback(self, selected_race_type)

"""
Configure Items ListWidget
"""
def configItemsListWidget(self, set_slot_selection_label_callback, set_slot_selection_list_callback, set_information_textedit_callback):
    self.itemsListWidget = self.findChild(QListWidget, 'itemsListWidget')
    setItemsListWidgetSlots(self, self.itemsListWidget)
    self.itemsListWidget.itemClicked.connect(lambda: on_items_list_widget_clicked_set_slot_selection_label(self, set_slot_selection_label_callback))
    self.itemsListWidget.itemClicked.connect(lambda: on_items_list_widget_clicked_set_slot_selection_list_widget(self, set_slot_selection_list_callback))
    self.itemsListWidget.itemClicked.connect(lambda: on_items_list_widget_clicked_set_information_textedit_widget(self, set_information_textedit_callback))

def on_items_list_widget_clicked_set_slot_selection_label(self, set_slot_selection_callback):
    selected_item = self.itemsListWidget.currentItem()
    if selected_item:
        selected_text = selected_item.text()
        set_slot_selection_callback(self, selected_text)
    
def on_items_list_widget_clicked_set_slot_selection_list_widget(self, set_slot_selection_callback):
    selected_item = self.itemsListWidget.currentItem()
    if selected_item:
        selected_text = selected_item.text().split(':')[0].strip()
        set_slot_selection_callback(self, selected_text)
    
def on_items_list_widget_clicked_set_information_textedit_widget(self, set_slot_selection_callback):
    set_slot_selection_callback(self)
    
"""
Configure Realm Rank ComboBox
"""
def configRealmRankComboBox(self, realm_rank_map, change_realm_rank_callback):
    self.realmRankComboBox = self.findChild(QComboBox, 'realmRankComboBox')
    self.realmRankComboBox.currentIndexChanged.connect(lambda: on_realm_rank_changed(self, realm_rank_map, change_realm_rank_callback))

def on_realm_rank_changed(self, realm_rank_map, change_realm_rank_callback):
    realmRankRaw = self.realmRankComboBox.currentText()
    realmRank = realm_rank_map.get(realmRankRaw)
    if realmRank:
        change_realm_rank_callback(self, realmRank)
        
"""
Configure Unequip All Items Push Button
"""

def configUnequipAllButton(self, unequip_all_button_callback):
    self.unequipAllButton = self.findChild(QPushButton, 'unequipAllButton')
    self.unequipAllButton.clicked.connect(lambda: on_unequip_all_pressed(self, unequip_all_button_callback))

def on_unequip_all_pressed(self, unequip_all_button_callback):
    unequip_all_button_callback(self)
    
"""
Configure Slot Selection List Widget
"""

def configSlotSelectionListWidget(self, slot_selection_callback):
    self.slotSelectionListWidget = self.findChild(QListWidget, 'slotSelectionListWidget')
    self.slotSelectionListWidget.clicked.connect(lambda: on_slot_pressed(self, slot_selection_callback))

def on_slot_pressed(self, slot_selection_callback):
    slot_selection_callback(self)