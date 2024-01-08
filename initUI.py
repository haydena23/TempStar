from PyQt5.QtWidgets import QComboBox, QListWidget, QPushButton, QTabWidget
from PyQt5.QtCore import QTimer

from Models.mappings import class_type_mapping, race_type_mapping, realm_rank_map

from changeFunctions import changeClass, changeRace, setSlotSelectionLabel, setSlotSelectionList, setInformationTextEdit
from changeFunctions import changeRealmRank, unquipAllSlotsWarning, setItemFromSlotSelection, setEquippedWeapons, setLevel, setItemsListWidgetSlots
from changeFunctions import changeTab, vaultItemDoubleClick, vaultItemSingleClick, populateVault, resetOnVaultComboBoxChange
from changeFunctions import vaultCurrentDoubleClick, vaultCurrentSingleClick

from newCharacter import create_new_character_on_open
from Models.vault import loadVault

def initUI(self):
    create_new_character_on_open(self)
    loadVault(self)
    
    # Configure UI components
    configClassComboBox(self, class_type_mapping, changeClass)
    configRaceComboBox(self, race_type_mapping, changeRace)
    configItemsListWidget(self, setSlotSelectionLabel, setSlotSelectionList, setInformationTextEdit)
    configRealmRankComboBox(self, realm_rank_map, changeRealmRank)
    configUnequipAllButton(self, unquipAllSlotsWarning)
    configSlotSelectionListWidget(self, setItemFromSlotSelection)
    configEquippedWeaponsComboBox(self, setEquippedWeapons)
    configLevelsComboBox(self, setLevel)
    configMasterVaultButton(self, changeTab)
    configSpellcraftButton(self, changeTab)
    configTabWidget(self, changeTab)
    configVaultAvailableWidget(self, vaultItemSingleClick, vaultItemDoubleClick)
    configVaultComboBox(self, resetOnVaultComboBoxChange)
    configVaultCurrentlyInWidget(self, vaultCurrentSingleClick, vaultCurrentDoubleClick)
    configVaultDoneButton(self, changeTab)
    configVaultAddItemButton(self, vaultItemDoubleClick)
    configRemoveAddItemButton(self, vaultCurrentDoubleClick)
    
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
    self.itemsListWidget.setCurrentRow(0)
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
    selected_item = self.itemsListWidget.currentItem()
    if selected_item:
        slot = selected_item.text().split(':')[0].strip()
        itemName = selected_item.text().split(':')[1].strip()
    set_slot_selection_callback(self, slot, itemName)
    
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
    
"""
Configure Equipped Weapons Combo Box
"""

def configEquippedWeaponsComboBox(self, weapons_selection_callback):
    self.weaponsComboBox = self.findChild(QComboBox, 'equippedWeaponsComboBox')
    self.weaponsComboBox.currentIndexChanged.connect(lambda: on_weapons_changed(self, weapons_selection_callback))

def on_weapons_changed(self, weapons_selection_callback):
    weapons_selection_callback(self)
        
"""
Configure Level Combo Box
"""

def configLevelsComboBox(self, level_selection_callback):
    self.levelComboBox = self.findChild(QComboBox, 'levelComboBox')
    self.levelComboBox.currentIndexChanged.connect(lambda: on_level_changed(self, level_selection_callback))

def on_level_changed(self, level_selection_callback):
    level_selection_callback(self)
    
"""
Configure Master Vault Push Button
"""

def configMasterVaultButton(self, master_vault_button_callback):
    self.masterVaultButton = self.findChild(QPushButton, 'masterVaultButton')
    self.masterVaultButton.clicked.connect(lambda: on_master_vault_button_pressed(self, master_vault_button_callback))

def on_master_vault_button_pressed(self, master_vault_button_callback):
    master_vault_button_callback(self, 2, None)
    
"""
Configure Spellcrafting Push Button
"""

def configSpellcraftButton(self, spellcraft_button_callback):
    self.spellcraftButton = self.findChild(QPushButton, 'spellcraftButton')
    self.spellcraftButton.clicked.connect(lambda: on_spellcraft_button_pressed(self, spellcraft_button_callback))

def on_spellcraft_button_pressed(self, spellcraft_button_callback):
    spellcraft_button_callback(self, 4, None)
    
"""
Configure Tab Widget
"""

def configTabWidget(self, tab_widget_callback):
    self.tabWidget = self.findChild(QTabWidget, 'tabWidget')
    self.tabWidget.currentChanged.connect(lambda: on_tab_widget_changed(self, tab_widget_callback))

def on_tab_widget_changed(self, tab_widget_callback):
    index = self.tabWidget.currentIndex()
    selected_slot = self.findChild(QListWidget, 'itemsListWidget').currentItem().text().split(":")[0]
    tab_widget_callback(self, index, selected_slot)
    
"""
Configure Vault Available Widget
"""

def configVaultAvailableWidget(self, vault_available_single_click_callback, vault_available_double_click_callback):
    self.vaultAvailableWidget = self.findChild(QListWidget, 'vaultAvailableWidget')
    populateVault(self)
    self.vaultAvailableWidget.itemClicked.connect(lambda: on_vault_available_clicked(self, vault_available_single_click_callback))
    self.vaultAvailableWidget.itemDoubleClicked.connect(lambda: on_vault_available_double_clicked(self, vault_available_double_click_callback))

def on_vault_available_clicked(self, vault_available_single_click_callback):
    vault_available_single_click_callback(self)

def on_vault_available_double_clicked(self, vault_available_double_click_callback):
    vault_available_double_click_callback(self)
    
"""
Configure Vault Currently In Widget
"""

def configVaultCurrentlyInWidget(self, vault_current_single_click_callback, vault_current_double_click_callback):
    self.vaultCurrentlyInWidget = self.findChild(QListWidget, 'currentlyInItemListWidget')
    self.vaultCurrentlyInWidget.itemClicked.connect(lambda: on_vault_currently_in_clicked(self, vault_current_single_click_callback))
    self.vaultCurrentlyInWidget.itemDoubleClicked.connect(lambda: on_vault_currently_in_double_clicked(self, vault_current_double_click_callback))

def on_vault_currently_in_clicked(self, vault_available_single_click_callback):
    vault_available_single_click_callback(self)

def on_vault_currently_in_double_clicked(self, vault_available_double_click_callback):
    vault_available_double_click_callback(self)
    
"""
Configure Vault Current Slot Combo Box
"""

def configVaultComboBox(self, vault_combobox_slot_callback):
    self.vaultComboBox = self.findChild(QComboBox, 'vaultCurrentSlot')
    self.vaultComboBox.currentIndexChanged.connect(lambda: on_vault_current_slot_changed(self, vault_combobox_slot_callback))

def on_vault_current_slot_changed(self, vault_combobox_slot_callback):
    vault_combobox_slot_callback(self)
    
"""
Configure Vault Done Push Button
"""

def configVaultDoneButton(self, vault_done_callback):
    self.vaultDoneButton = self.findChild(QPushButton, 'vaultDoneButton')
    self.vaultDoneButton.clicked.connect(lambda: on_vault_done_button_pressed(self, vault_done_callback))

def on_vault_done_button_pressed(self, vault_done_callback):
    vault_done_callback(self, 1, None)
    
"""
Configure Vault Add Single Item Push Button
"""

def configVaultAddItemButton(self, add_item_button_callback):
    self.vaultAddItem = self.findChild(QPushButton, 'addFromVaultButton')
    self.vaultAddItem.clicked.connect(lambda: on_vault_add_item_button_pressed(self, add_item_button_callback))

def on_vault_add_item_button_pressed(self, add_item_button_callback):
    add_item_button_callback(self)
    
"""
Configure Vault Remove Single Item Push Button
"""

def configRemoveAddItemButton(self, remove_item_button_callback):
    self.vaultRemoveItem = self.findChild(QPushButton, 'removeFromVaultButton')
    self.vaultRemoveItem.clicked.connect(lambda: on_vault_remove_item_button_pressed(self, remove_item_button_callback))

def on_vault_remove_item_button_pressed(self, remove_item_button_callback):
    remove_item_button_callback(self)