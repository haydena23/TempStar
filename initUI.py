from PyQt5.QtWidgets import QComboBox, QListWidget, QPushButton, QTabWidget, QCheckBox, QLabel
from PyQt5.QtCore import Qt

from Models.mappings import class_type_mapping, race_type_mapping, realm_rank_map

from changeFunctions import changeClass, changeRace, setSlotSelectionLabel, setSlotSelectionList, setInformationTextEdit
from changeFunctions import changeRealmRank, unquipAllSlotsWarning, setItemFromSlotSelection, setEquippedWeapons, setLevel, setItemsListWidgetSlots
from changeFunctions import changeTab, vaultItemDoubleClick, vaultItemSingleClick, populateVault, resetOnVaultComboBoxChange
from changeFunctions import vaultCurrentDoubleClick, vaultCurrentSingleClick, vaultItemAddAll, vaultCurrentRemoveAll, populateAvailable
from changeFunctions import resetFilterPage
from statsHandler import checkTOADisplay

from SCCalc.adjustUIfunctions import initSCArmorTypes, onChangeArmor, setArchtypes, setLevelBox
from SCCalc.adjustUIfunctions import setMaxImbue, createNewItem, deleteItem, onSCSlotChanged, onSCStatComboBoxChanged
from SCCalc.adjustUIfunctions import updateAfterValueChange, onSCItemClicked, initSCItemsListWidget

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
    configRemoveItemButton(self, vaultCurrentDoubleClick)
    configTOACheckBox(self, checkTOADisplay)
    configVaultAddAllButton(self, vaultItemAddAll)
    configRemoveAllItemButton(self, vaultCurrentRemoveAll)
    configFilterSearchButton(self, changeTab)
    configVaultClearFilterButton(self, changeTab)
    configFilterClearFilterButton(self, resetFilterPage)
    
    self.scItems = []
    
    # Spellcrafting
    configSCItemListWidget(self, onSCItemClicked)
    
    # configSCArmorComboBox(self, onChangeArmor)
    # configSCArchtypesComboBox(self, setArchtypes, setArchtypes, setArchtypes, setArchtypes)
    # configSCLevelComboBox(self, setLevelBox)
    # configSCCreateButton(self, createNewItem)
    # configSCDeleteButton(self, deleteItem)
    # configSCSlotComboBox(self, onSCSlotChanged)
    # configSCStatComboBox(self, onSCStatComboBoxChanged)
    # configSCValueComboBox(self, updateAfterValueChange)
    
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
    initSCArmorTypes(self)
        
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
    try:
        currentSelection = self.findChild(QListWidget, 'itemsListWidget').currentItem().text().split(":")[0]
        print(currentSelection)
        index = self.findChild(QComboBox, 'scCurrentSlot').findText(currentSelection, Qt.MatchFlag.MatchExactly)
        if index == -1:
            self.findChild(QComboBox, 'scCurrentSlot').setCurrentIndex(0)
            spellcraft_button_callback(self, 4, None)
        else:
            self.findChild(QComboBox, 'scCurrentSlot').setCurrentIndex(index)
            spellcraft_button_callback(self, 4, None)
    except Exception as e:
        print(f"Error at on_spellcraft_button_pressed: {e}")
    
"""
Configure Tab Widget
"""

def configTabWidget(self, tab_widget_callback):
    self.tabWidget = self.findChild(QTabWidget, 'tabWidget')
    self.tabWidget.currentChanged.connect(lambda: on_tab_widget_changed(self, tab_widget_callback))

def on_tab_widget_changed(self, tab_widget_callback):
    index = self.tabWidget.currentIndex()
    selected_slot = self.findChild(QListWidget, 'itemsListWidget').currentItem().text().split(":")[0]
    try:
        currentSelection = self.findChild(QListWidget, 'itemsListWidget').currentItem().text().split(":")[0]
        indexOfSlot = self.findChild(QComboBox, 'scCurrentSlot').findText(currentSelection, Qt.MatchFlag.MatchExactly)
        if indexOfSlot != -1:
            self.findChild(QComboBox, 'scCurrentSlot').setCurrentIndex(indexOfSlot)
    except Exception as e:
        pass
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
    self.findChild(QLabel, 'filterLabel').setText("Filter Status: Inactive")
    vault_done_callback(self, 1, None)
    
"""
Configure Vault Clear Filter Push Button
"""

def configVaultClearFilterButton(self, vault_clear_filter_callback):
    self.vaultClearFilter = self.findChild(QPushButton, 'vaultClearFilter')
    self.vaultClearFilter.clicked.connect(lambda: on_vault_clear_filter_button_pressed(self, vault_clear_filter_callback))

def on_vault_clear_filter_button_pressed(self, vault_clear_filter_callback):
    self.findChild(QLabel, 'filterLabel').setText("Filter Status: Inactive")
    resetFilterPage(self)
    vault_clear_filter_callback(self, 2, None)
    
"""
Configure Filter Page Clear Filter Push Button
"""

def configFilterClearFilterButton(self, filter_clear_filter_callback):
    self.filterClearFilter = self.findChild(QPushButton, 'clearFiltersOnFilterPage')
    self.filterClearFilter.clicked.connect(lambda: on_filter_clear_filter_button_pressed(self, filter_clear_filter_callback))

def on_filter_clear_filter_button_pressed(self, filter_clear_filter_callback):
    self.findChild(QLabel, 'filterLabel').setText("Filter Status: Inactive")
    filter_clear_filter_callback(self)
    
"""
Configure Vault Add Single Item Push Button
"""

def configVaultAddItemButton(self, add_item_button_callback):
    self.vaultAddItem = self.findChild(QPushButton, 'addFromVaultButton')
    self.vaultAddItem.clicked.connect(lambda: on_vault_add_item_button_pressed(self, add_item_button_callback))

def on_vault_add_item_button_pressed(self, add_item_button_callback):
    add_item_button_callback(self)
    
"""
Configure Vault Add All Item Push Button
"""

def configVaultAddAllButton(self, add_all_button_callback):
    self.vaultAddAll = self.findChild(QPushButton, 'addAllFromVault')
    self.vaultAddAll.clicked.connect(lambda: on_vault_add_all_button_pressed(self, add_all_button_callback))

def on_vault_add_all_button_pressed(self, add_all_button_callback):
    add_all_button_callback(self)
    
"""
Configure Vault Remove Single Item Push Button
"""

def configRemoveItemButton(self, remove_item_button_callback):
    self.vaultRemoveItem = self.findChild(QPushButton, 'removeFromVaultButton')
    self.vaultRemoveItem.clicked.connect(lambda: on_vault_remove_item_button_pressed(self, remove_item_button_callback))

def on_vault_remove_item_button_pressed(self, remove_item_button_callback):
    remove_item_button_callback(self)

"""
Configure Vault Remove All Item Push Button
"""

def configRemoveAllItemButton(self, remove_all_button_callback):
    self.vaultRemoveAll = self.findChild(QPushButton, 'removeAllButton')
    self.vaultRemoveAll.clicked.connect(lambda: on_vault_remove_all_button_pressed(self, remove_all_button_callback))

def on_vault_remove_all_button_pressed(self, remove_all_button_callback):
    remove_all_button_callback(self)
      
"""
Configure TOA Check Box
"""

def configTOACheckBox(self, checkbox_callback):
    self.checkbox = self.findChild(QCheckBox, 'checkBox')
    self.checkbox.stateChanged.connect(lambda: on_checkbox_pressed(self, checkbox_callback))

def on_checkbox_pressed(self, checkbox_callback):
    checkbox_callback(self)
    
"""
Configure Filter Search Push Button
"""

def configFilterSearchButton(self, filter_search_callback):
    self.filterSearch = self.findChild(QPushButton, 'filterSearchButton')
    self.filterSearch.clicked.connect(lambda: on_filter_search_button_pressed(self, filter_search_callback))

def on_filter_search_button_pressed(self, filter_search_callback):
    self.findChild(QLabel, 'filterLabel').setText("Filter Status: Active")
    filter_search_callback(self, 2, None)
    
"""
Configure SC Armor Combo Box
"""

def configSCArmorComboBox(self, sc_armor_combobox_slot_callback):
    self.scArmorComboBox = self.findChild(QComboBox, 'scArmorTypeCombo')
    initSCArmorTypes(self)
    self.scArmorComboBox.currentIndexChanged.connect(lambda: on_sc_armor_combobox_changed(self, sc_armor_combobox_slot_callback))

def on_sc_armor_combobox_changed(self, sc_armor_combobox_slot_callback):
    sc_armor_combobox_slot_callback(self)
    
"""
Configure SC Archtype Combo Box
"""

def configSCArchtypesComboBox(self, sc_archtype1_combobox_callback, sc_archtype2_combobox_callback, sc_archtype3_combobox_callback, sc_archtype4_combobox_callback):
    self.scArchtype1 = self.findChild(QComboBox, 'statCategory1')
    self.scArchtype2 = self.findChild(QComboBox, 'statCategory2')
    self.scArchtype3 = self.findChild(QComboBox, 'statCategory3')
    self.scArchtype4 = self.findChild(QComboBox, 'statCategory4')
    for i in range(1, 5):
        setArchtypes(self, self.findChild(QComboBox, f'statCategory{i}'))
    self.scArchtype1.currentIndexChanged.connect(lambda: on_sc_archtype1_combobox_changed(self, sc_archtype1_combobox_callback))
    self.scArchtype2.currentIndexChanged.connect(lambda: on_sc_archtype2_combobox_changed(self, sc_archtype2_combobox_callback))
    self.scArchtype3.currentIndexChanged.connect(lambda: on_sc_archtype3_combobox_changed(self, sc_archtype3_combobox_callback))
    self.scArchtype4.currentIndexChanged.connect(lambda: on_sc_archtype4_combobox_changed(self, sc_archtype4_combobox_callback))

def on_sc_archtype1_combobox_changed(self, sc_armor_combobox_slot_callback):
    sc_armor_combobox_slot_callback(self, self.scArchtype1)
    
def on_sc_archtype2_combobox_changed(self, sc_armor_combobox_slot_callback):
    sc_armor_combobox_slot_callback(self, self.scArchtype2)
    
def on_sc_archtype3_combobox_changed(self, sc_armor_combobox_slot_callback):
    sc_armor_combobox_slot_callback(self, self.scArchtype3)
    
def on_sc_archtype4_combobox_changed(self, sc_armor_combobox_slot_callback):
    sc_armor_combobox_slot_callback(self, self.scArchtype4)

"""
Configure SC Level Combo Box
"""
 
def configSCLevelComboBox(self, sc_level_combobox_callback):
    self.scLevelCombobox = self.findChild(QComboBox, 'scArmorLevelCombo')
    setMaxImbue(self, self.scLevelCombobox.currentText())
    self.scLevelCombobox.currentIndexChanged.connect(lambda: on_sc_level_combobox_changed(self, sc_level_combobox_callback))

def on_sc_level_combobox_changed(self, sc_level_combobox_callback):
    sc_level_combobox_callback(self)
    
"""
Configure SC Create Push Button
"""

def configSCCreateButton(self, sc_create_button_callback):
    self.createButton = self.findChild(QPushButton, 'scCreateNewButton')
    self.createButton.clicked.connect(lambda: on_sc_create_button_pressed(self, sc_create_button_callback))

def on_sc_create_button_pressed(self, sc_create_button_callback):
    sc_create_button_callback(self)
    
"""
Configure SC Delete Push Button
"""

def configSCDeleteButton(self, sc_delete_button_callback):
    self.deleteButton = self.findChild(QPushButton, 'scDeleteItemButton')
    self.deleteButton.clicked.connect(lambda: on_sc_delete_button_pressed(self, sc_delete_button_callback))

def on_sc_delete_button_pressed(self, sc_delete_button_callback):
    sc_delete_button_callback(self)
    
"""
Config SC Slot Combobox
"""

def configSCSlotComboBox(self, sc_slot_combobox_callback):
    self.scCurrentSlot = self.findChild(QComboBox, 'scCurrentSlot')
    self.scCurrentSlot.currentIndexChanged.connect(lambda: on_sc_current_slot_changed(self, sc_slot_combobox_callback))
    
def on_sc_current_slot_changed(self, on_sc_current_slot_changed):
    on_sc_current_slot_changed(self)

"""
Config SC Stat Combobox
"""

def configSCStatComboBox(self, sc_stat_combo_box_callback):
    self.scStatComboBox1 = self.findChild(QComboBox, 'statCombo1')
    self.scStatComboBox2 = self.findChild(QComboBox, 'statCombo2')
    self.scStatComboBox3 = self.findChild(QComboBox, 'statCombo3')
    self.scStatComboBox4 = self.findChild(QComboBox, 'statCombo4')
    self.scStatComboBox1.currentIndexChanged.connect(lambda: on_sc_stat_combo1_changed(self, sc_stat_combo_box_callback))
    self.scStatComboBox2.currentIndexChanged.connect(lambda: on_sc_stat_combo2_changed(self, sc_stat_combo_box_callback))
    self.scStatComboBox3.currentIndexChanged.connect(lambda: on_sc_stat_combo3_changed(self, sc_stat_combo_box_callback))
    self.scStatComboBox4.currentIndexChanged.connect(lambda: on_sc_stat_combo4_changed(self, sc_stat_combo_box_callback))

def on_sc_stat_combo1_changed(self, sc_stat_combo_box_callback):
    sc_stat_combo_box_callback(self, self.scStatComboBox1)
    
def on_sc_stat_combo2_changed(self, sc_stat_combo_box_callback):
    sc_stat_combo_box_callback(self, self.scStatComboBox2)
    
def on_sc_stat_combo3_changed(self, sc_stat_combo_box_callback):
    sc_stat_combo_box_callback(self, self.scStatComboBox3)
    
def on_sc_stat_combo4_changed(self, sc_stat_combo_box_callback):
    sc_stat_combo_box_callback(self, self.scStatComboBox4)

"""
Config SC Stat Combobox
"""

def configSCValueComboBox(self, sc_value_combo_box_callback):
    self.scValueComboBox1 = self.findChild(QComboBox, 'statValue1')
    self.scValueComboBox2 = self.findChild(QComboBox, 'statValue2')
    self.scValueComboBox3 = self.findChild(QComboBox, 'statValue3')
    self.scValueComboBox4 = self.findChild(QComboBox, 'statValue4')
    self.scValueComboBox1.currentIndexChanged.connect(lambda: on_sc_value_combo1_changed(self, sc_value_combo_box_callback))
    self.scValueComboBox2.currentIndexChanged.connect(lambda: on_sc_value_combo2_changed(self, sc_value_combo_box_callback))
    self.scValueComboBox3.currentIndexChanged.connect(lambda: on_sc_value_combo3_changed(self, sc_value_combo_box_callback))
    self.scValueComboBox4.currentIndexChanged.connect(lambda: on_sc_value_combo4_changed(self, sc_value_combo_box_callback))

def on_sc_value_combo1_changed(self, sc_value_combo_box_callback):
    sc_value_combo_box_callback(self)
    
def on_sc_value_combo2_changed(self, sc_value_combo_box_callback):
    sc_value_combo_box_callback(self)
    
def on_sc_value_combo3_changed(self, sc_value_combo_box_callback):
    sc_value_combo_box_callback(self)
    
def on_sc_value_combo4_changed(self, sc_value_combo_box_callback):
    sc_value_combo_box_callback(self)
    
"""
Config SC Fifth Combobox
"""

def configSCFifthComboBox(self, sc_fifth_callback):
    self.fifthBox = self.findChild(QComboBox, 'slot5Bonus')
    self.fifthBox.currentIndexChanged.connect(lambda: on_sc_fifth_changed(self, sc_fifth_callback))
    
def on_sc_fifth_changed(self, sc_fifth_callback):
    sc_fifth_callback(self)
    
"""
Config SC Item List
"""

def configSCItemListWidget(self, sc_item_single_click_callback):
    self.scItemList = self.findChild(QListWidget, 'scItemsListWidget')
    initSCItemsListWidget(self, self.scItemList)
    self.scItemList.itemClicked.connect(lambda: on_sc_item_clicked(self, sc_item_single_click_callback))

def on_sc_item_clicked(self, sc_item_single_click_callback):
    selected_item = self.scItemList.currentRow()
    sc_item_single_click_callback(self, selected_item)
