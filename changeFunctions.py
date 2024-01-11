from newCharacter import new_character_change
from statsHandler import updateResistsFromRace, adjustSkillsFromRealmRank, autoUpdateRealmRank

from Models.classes import ClassType, RaceType
from Models.mappings import slot_mapping, equip_weapon_map
from widgets import unequipMessageBox
from reportGeneration import formatItemReportForInformationBox

from PyQt5.QtWidgets import QLabel, QListWidget, QListWidgetItem, QComboBox, QTabWidget
from PyQt5.QtWidgets import QGroupBox, QTextEdit, QSpinBox, QCheckBox, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

from SCCalc.adjustUIfunctions import checkForItemsForDisable

def changeClass(self, class_type: ClassType):
    new_character_change(self, class_type)
    slotSelectionWidget = self.findChild(QListWidget, 'slotSelectionListWidget')
    slotSelectionWidget.clear()
    slotSelectionWidget.addItem(QListWidgetItem(str("<Empty Slot>")))

def changeRace(self, race_type: RaceType):
    updateResistsFromRace(self, race_type)
    autoUpdateRealmRank(self)

def changeChampionLevel(self):
    pass

def changeRealmRank(self, realm_rank):
    adjustSkillsFromRealmRank(self, realm_rank)

def setSlotSelectionLabel(self, text):
    text = str(text).split(":")[0]
    label = self.findChild(QLabel, 'slotSelectionLabel')
    label.setText(f"{text} Slot Selections :")
    
def setSlotSelectionList(self, text):
    slotSelectionListWidget = self.findChild(QListWidget, 'slotSelectionListWidget')
    slotSelectionListWidget.clear()
    emptyItem = QListWidgetItem(str("<Empty Slot>"))
    slotSelectionListWidget.addItem(emptyItem)
    try:
        availableItems = self.character.allAddedItems.get(text)
        for item in availableItems:
            slotSelectionListWidget.addItem(QListWidgetItem(item.name))
    except Exception as e:
        print(f"Error in setSlotSelectionList: {e}")
    slotSelectionListWidget.sortItems(Qt.SortOrder.AscendingOrder)
    itemsSelectionListWidget = self.findChild(QListWidget, 'itemsListWidget')
    slotWidget = itemsSelectionListWidget.findItems(text, Qt.MatchFlag.MatchStartsWith)[0]
    if self.character.currentItems.get(text) is None:
        slotWidget.setText(f"{text}:\t\t<Empty Slot>")
        slotSelectionListWidget.setCurrentItem(emptyItem)
    else:
        slotWidget.setText(f"{text}:\t\t{self.character.currentItems.get(text).name}")
        itemWidget = slotSelectionListWidget.findItems(self.character.currentItems.get(text).name, Qt.MatchFlag.MatchExactly)[0]
        slotSelectionListWidget.setCurrentItem(itemWidget)
    itemScanForLockStatus(self, itemsSelectionListWidget)
        
def itemScanForLockStatus(self, itemList):
    allEmpty = True
    for row in range(itemList.count()):
        if "<Empty Slot>" not in itemList.item(row).text():
             allEmpty = False
    if allEmpty:
        setUnlockStatus(self)
    else:
        setLockStatus(self)

def setItemsListWidgetSlots(self, itemsListWidget):
    for slot in range(itemsListWidget.count()):
        text = itemsListWidget.item(slot).text().split(":")[0]
        if self.character.currentItems.get(text) is None:
            itemsListWidget.item(slot).setText(f"{text}:\t\t<Empty Slot>")
            setUnlockStatus(self)
        else:
            setLockStatus(self)
            itemsListWidget.item(slot).setText(f"{text}:\t\t{self.character.currentItems.get(text).name}")
    autoUpdateRealmRank(self)

def setInformationTextEdit(self, slot, name):
    infoBox = self.findChild(QTextEdit, 'informationBox')
    items = self.character.vault.get(slot)
    selectedItemInfo = None
    for item in items:
        if item.name == name:
            selectedItemInfo = item
    try:
        infoBox.setText(formatItemReportForInformationBox(selectedItemInfo))
    except Exception as e:
        print(f"Error in setInformationTextEdit: {e}")
        infoBox.setText("<Empty Slot>")
    
def setItemFromSlotSelection(self):
    slotSelectionListWidget = self.findChild(QListWidget, 'slotSelectionListWidget')
    slotRow = self.findChild(QListWidget, 'itemsListWidget').currentRow()
    slotName = slot_mapping.get(slotRow)
    equipWeapons = self.findChild(QComboBox, 'equippedWeaponsComboBox')
    weaponsNotAllowed = equip_weapon_map.get(equipWeapons.currentText())
    if slotSelectionListWidget.currentRow() == 0:
        self.character.setCurrentItem(slotName, None)
        setInformationTextEdit(self, slotName, None)
        setUnlockStatus(self)
    else:
        setLockStatus(self)
        for item in self.character.allAddedItems[slotName]:
            if item.name == slotSelectionListWidget.currentItem().text():
                if item.slot not in weaponsNotAllowed:
                    self.character.setCurrentItem(slotName, item)
                setInformationTextEdit(self, slotName, item.name)
    setItemsListWidgetSlots(self, self.findChild(QListWidget, 'itemsListWidget'))
    autoUpdateRealmRank(self)
    if slotSelectionListWidget.currentRow() != 0:
        setLockStatus(self)
    else:
        setUnlockStatus(self)

def setEquippedWeapons(self):
    self.findChild(QListWidget, 'vaultAvailableWidget').setCurrentRow(0)
    autoUpdateRealmRank(self)
    
def setLevel(self):
    populateVault(self)
    populateAvailable(self)
    autoUpdateRealmRank(self)

def unquipAllSlotsWarning(self):
    if unequipMessageBox():
        unequipAllSlots(self)

def unequipAllSlots(self):
    for slot in self.character.currentItems:
        self.character.setCurrentItem(slot,None)
    setItemsListWidgetSlots(self, self.findChild(QListWidget, 'itemsListWidget'))
    setUnlockStatus(self)

def setLockStatus(self):
    self.lockTemp()
    self.findChild(QComboBox, 'classComboBox').setDisabled(True)
    
def setUnlockStatus(self):
    self.unlockTemp()
    self.findChild(QComboBox, 'classComboBox').setDisabled(False)

def changeTab(self, index, slot):
    self.tabWidget = self.findChild(QTabWidget, 'tabWidget')
    populateVault(self)
    populateAvailable(self)
    if index == 2:
        self.character.copyCurrentToTemp()
        setLockStatus(self)
    else:
        self.character.copyTempToCurrent()
        setUnlockStatus(self)

    self.tabWidget.setCurrentIndex(index)
    if slot is not None:
        self.vaultCurrentSlotWidget = self.findChild(QComboBox, 'vaultCurrentSlot')
        indexOfVaultSlot = self.vaultCurrentSlotWidget.findText(slot, Qt.MatchFlag.MatchExactly)
        self.vaultCurrentSlotWidget.setCurrentIndex(indexOfVaultSlot)
    autoUpdateRealmRank(self)
    itemsListWidget = self.findChild(QListWidget, 'itemsListWidget')
    setItemsListWidgetSlots(self, itemsListWidget)
    slotSelectionWidget = self.findChild(QListWidget, 'slotSelectionListWidget')
    slotSelectionWidget.sortItems(Qt.SortOrder.AscendingOrder)
    checkForItemsForDisable(self)

def resetOnVaultComboBoxChange(self):
    autoUpdateRealmRank(self)
    populateVault(self)
    populateAvailable(self)
    
    vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    itemsListWidget = self.findChild(QListWidget, 'itemsListWidget').findItems(vaultCurrentSlotText, Qt.MatchFlag.MatchStartsWith)[0]
    self.findChild(QListWidget, 'itemsListWidget').setCurrentItem(itemsListWidget)
    setSlotSelectionLabel(self, vaultCurrentSlotText)
    refreshSlotSelectionListWidget(self)

def setFilters(self):
    filters = []
    for i in range(1, 6):
        filterName = f'bonusFilter{i}'
        valueName = f'bonusFilter{i}Value'
        bonusFilterText = self.findChild(QComboBox, filterName).currentText().replace(" ","_").lower()
        bonusFilterValue = self.findChild(QSpinBox, valueName).value()
        if "<unfiltered>" not in bonusFilterText:
            filters.append({'stat': bonusFilterText, 'value': bonusFilterValue})
    return filters

def resetFilterPage(self):
    for i in range(1, 6):
        filterName = f'bonusFilter{i}'
        valueName = f'bonusFilter{i}Value'
        self.findChild(QComboBox, filterName).setCurrentIndex(0)
        self.findChild(QSpinBox, valueName).setValue(1)

def populateVault(self):
    vaultAvailableWidget = self.findChild(QListWidget, 'vaultAvailableWidget')
    vaultAvailableWidget.clear()
    vaultAvailableWidget.addItem(QListWidgetItem(str("<Empty Slot>")))
    counter = 0
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    currentLevel = int(self.findChild(QComboBox, 'levelComboBox').currentText())
    
    filterFlagText = self.findChild(QLabel, 'filterLabel').text().split(": ")[1]
    filterFlag = False
    filters = []
    if filterFlagText == "Active":
        filters = setFilters(self)
        if len(filters) != 0:
            filterFlag = True
        else:
            filterFlag = False
            self.findChild(QLabel, 'filterLabel').setText("Filter Status: Inactive")
    try:
        availableVaultItems = self.character.vault.get(self.vaultCurrentSlotText)
        addedItemNames = [item.name for item in self.character.allAddedItems.get(self.vaultCurrentSlotText)]
        for item in availableVaultItems:
            if item.name not in addedItemNames and currentLevel >= item.bonus_level:
                if item.item_type in self.character.class_type.weaponry or item.item_type in self.character.class_type.armor_types or item.item_type == "Magical":
                    if item.realm == "All" or item.realm == self.character.class_type.realm:
                        playerClass = self.character.class_type.name.split(" ")[1]
                        if item.usable == "All" or playerClass in item.usable:
                            if item.item_type == 'Shield' and item.shield_size not in self.character.class_type.shield_types:
                                pass
                            elif (item.slot == 'Left Hand' and item.item_type != 'Shield' and 
                                len(self.character.dual_wield_skills) == 0 and self.vaultCurrentSlotText == 'Left Hand'):
                                pass
                            elif filterFlag:
                                if all(item.stats.get(f['stat'], 0) >= f['value'] for f in filters):
                                    vaultAvailableWidget.addItem(QListWidgetItem(item.name))
                                    counter += 1  
                            else:
                                vaultAvailableWidget.addItem(QListWidgetItem(item.name))
                                counter += 1
        self.findChild(QGroupBox, 'availableItemListGroupBox').setTitle(f"Available Item List : ( {counter} )")
        vaultAvailableWidget.sortItems(Qt.SortOrder.AscendingOrder)
        setSlotSelectionList(self, self.vaultCurrentSlotText)
    except Exception as e:
        print(f"Error in populateVault: {e}")
    
def populateAvailable(self):
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    currentlyInWidget = self.findChild(QListWidget, 'currentlyInItemListWidget')
    currentlyInWidget.clear()
    try:
        itemsToPickFrom = self.character.allAddedItems.get(self.vaultCurrentSlotText)
        counter = 0       
        for item in itemsToPickFrom:
            currentlyInWidget.addItem(QListWidgetItem(item.name))
            counter += 1
        self.findChild(QGroupBox, 'currentlyInItemList').setTitle(f"Current in Item List : ( {counter} )")
        currentlyInWidget.sortItems(Qt.SortOrder.AscendingOrder)
    except Exception as e:
        print(f"Error in populateAvailable: {e}")

def vaultItemSingleClick(self):
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    selectedItem = self.findChild(QListWidget, 'vaultAvailableWidget').currentItem().text()
    itemsToPickFrom = self.character.vault.get(self.vaultCurrentSlotText)
    foundItem = False
    equipWeapons = self.findChild(QComboBox, 'equippedWeaponsComboBox')
    weaponsNotAllowed = equip_weapon_map.get(equipWeapons.currentText())
    for item in itemsToPickFrom:
        if item.name == selectedItem:
            if item.slot not in weaponsNotAllowed:
                self.character.setCurrentItem(self.vaultCurrentSlotText, item)
            setInformationTextEdit(self, self.vaultCurrentSlotText, item.name)
            foundItem = True
    if foundItem != True:
        self.character.setCurrentItem(self.vaultCurrentSlotText, None)
        setInformationTextEdit(self, self.vaultCurrentSlotText, None)
    autoUpdateRealmRank(self)

def vaultItemDoubleClick(self):
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    self.selectedItemWidget = self.findChild(QListWidget, 'vaultAvailableWidget')
    try:
        selectedItem = self.selectedItemWidget.currentItem().text()
    except Exception as e:
        print(f"Error in vaultItemDoubleClick: {e}")
        selectedItem = None
    if selectedItem != "<Empty Slot>" or selectedItem is not None:
        itemsToPickFrom = self.character.vault.get(self.vaultCurrentSlotText)
        for item in itemsToPickFrom:
            if item.name == selectedItem:
                self.character.addToAllItems(self.vaultCurrentSlotText, item)
                self.character.setTempItem(self.vaultCurrentSlotText, item)
                row = self.selectedItemWidget.currentRow()
                item = self.selectedItemWidget.takeItem(row)
                del item
                self.selectedItemWidget.setCurrentRow(0)                
        refreshSlotSelectionListWidget(self)
    populateVault(self)
    populateAvailable(self)
    
def vaultItemAddAll(self):
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    self.selectedItemWidget = self.findChild(QListWidget, 'vaultAvailableWidget')
    itemsToPickFrom = self.character.vault.get(self.vaultCurrentSlotText)
    self.selectedItemWidget.setCurrentRow(0)
    for item in itemsToPickFrom:
        if item.name != "<Empty Slot>":
            self.character.addToAllItems(self.vaultCurrentSlotText, item)
            row = self.selectedItemWidget.currentRow()
            item = self.selectedItemWidget.takeItem(row)
            del item
            self.selectedItemWidget.setCurrentRow(row+1)
    self.selectedItemWidget.clear()
    refreshSlotSelectionListWidget(self)
    populateVault(self)
    populateAvailable(self)

def vaultCurrentRemoveAll(self):
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    self.selectedItemWidget = self.findChild(QListWidget, 'currentlyInItemListWidget')
    if self.selectedItemWidget.count() != 0:
        self.selectedItemWidget.setCurrentRow(0)
        itemsToPickFrom = self.character.allAddedItems.get(self.vaultCurrentSlotText)
        print(len(itemsToPickFrom))
        for i in range(len(itemsToPickFrom)):
            item = itemsToPickFrom[0]
            print(item.name)
            selectedItem = itemsToPickFrom[0].name
            self.character.removeFromAllItems(self.vaultCurrentSlotText, item)
            try:
                if self.character.temporaryItems[self.vaultCurrentSlotText].name == selectedItem:
                    self.character.setTempItem(self.vaultCurrentSlotText, None) 
            except Exception as e:
                print(f"Error in vaultCurrentRemoveAll: {e}")
        self.selectedItemWidget.clear()
    refreshSlotSelectionListWidget(self)
    populateVault(self)
    populateAvailable(self)
    
def vaultCurrentSingleClick(self):  
    vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    selectedItem = self.findChild(QListWidget, 'currentlyInItemListWidget').currentItem().text()
    equipWeapons = self.findChild(QComboBox, 'equippedWeaponsComboBox')
    weaponsNotAllowed = equip_weapon_map.get(equipWeapons.currentText())
    if selectedItem is None:
        pass
    else:
        itemsToPickFrom = self.character.allAddedItems.get(vaultCurrentSlotText)
        foundItem = False
        for item in itemsToPickFrom:
            if item.name == selectedItem:
                if item.slot not in weaponsNotAllowed:
                    self.character.setCurrentItem(vaultCurrentSlotText, item)
                    self.character.setTempItem(vaultCurrentSlotText, item)
                setInformationTextEdit(self, vaultCurrentSlotText, item.name)
                foundItem = True
        if foundItem != True:
            self.character.setCurrentItem(vaultCurrentSlotText, None)
            setInformationTextEdit(self, vaultCurrentSlotText, None)
        autoUpdateRealmRank(self)

def vaultCurrentDoubleClick(self):
    vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    self.selectedItemWidget = self.findChild(QListWidget, 'currentlyInItemListWidget')
    if self.selectedItemWidget.count() != 0:
        selectedItem = self.selectedItemWidget.currentItem().text()
        itemsToPickFrom = self.character.allAddedItems.get(vaultCurrentSlotText)
        for item in itemsToPickFrom:
            if item.name == selectedItem:
                self.character.removeFromAllItems(vaultCurrentSlotText, item)
                try:
                    if self.character.temporaryItems[vaultCurrentSlotText].name == selectedItem:
                        self.character.setTempItem(vaultCurrentSlotText, None) 
                    if self.character.currentItems[vaultCurrentSlotText].name == selectedItem:
                        self.character.setCurrentItem(vaultCurrentSlotText, None)
                except Exception as e:
                    print(f"Error in vaultCurrentDoubleClick: {e}")
                row = self.selectedItemWidget.currentRow()
                item = self.selectedItemWidget.takeItem(row)
                del item
                try:
                    self.selectedItemWidget.setCurrentRow(0)
                except Exception as e:
                    print(f"Error: {e}")
        refreshSlotSelectionListWidget(self)
        populateVault(self)
        populateAvailable(self)
    autoUpdateRealmRank(self)
    
def refreshSlotSelectionListWidget(self):
    slotSelectionListWidget = self.findChild(QListWidget, 'slotSelectionListWidget')
    slotSelectionListWidget.clear()
    slotSelectionListWidget.addItem(QListWidgetItem(str("<Empty Slot>")))
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    for item in self.character.allAddedItems[self.vaultCurrentSlotText]:
        slotSelectionListWidget.addItem(QListWidgetItem(str(item.name)))
    autoUpdateRealmRank(self)