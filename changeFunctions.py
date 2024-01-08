from newCharacter import new_character_change
from statsHandler import updateResistsFromRace, adjustSkillsFromRealmRank

from statsHandler import adjustSkillsFromRealmRank, autoUpdateRealmRank, calculateNowStats

from Models.classes import ClassType, RaceType
from Models.mappings import slot_mapping
from widgets import unequipMessageBox
from reportGeneration import formatItemReport

from PyQt5.QtWidgets import QLabel, QListWidget, QListWidgetItem, QComboBox, QTabWidget
from PyQt5.QtWidgets import QGroupBox, QTextEdit
from PyQt5.QtCore import Qt

def changeClass(self, class_type: ClassType):
    new_character_change(self, class_type)

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
    except:
        pass
    itemsSelectionListWidget = self.findChild(QListWidget, 'itemsListWidget')
    slotWidget = itemsSelectionListWidget.findItems(text, Qt.MatchFlag.MatchStartsWith)[0]
    if self.character.currentItems.get(text) is None:
        slotWidget.setText(f"{text}:\t\t<Empty Slot>")
        slotSelectionListWidget.setCurrentItem(emptyItem)
    else:
        slotWidget.setText(f"{text}:\t\t{self.character.currentItems.get(text).name}")
        itemWidget = slotSelectionListWidget.findItems(self.character.currentItems.get(text).name, Qt.MatchFlag.MatchExactly)[0]
        slotSelectionListWidget.setCurrentItem(itemWidget)
        
def setItemsListWidgetSlots(self, itemsListWidget):
    for slot in range(itemsListWidget.count()):
        text = itemsListWidget.item(slot).text().split(":")[0]
        if self.character.currentItems.get(text) is None:
            itemsListWidget.item(slot).setText(f"{text}:\t\t<Empty Slot>")
        else:
            setLockStatus(self)
            itemsListWidget.item(slot).setText(f"{text}:\t\t{self.character.currentItems.get(text).name}")
    autoUpdateRealmRank(self)

def setInformationTextEdit(self, slot, name):
    infoBox = self.findChild(QTextEdit, 'informationBox')
    items = self.character.vault.get(slot)[0]
    
    infoBox.setText(formatItemReport(items))

def setItemFromSlotSelection(self):
    slotSelectionListWidget = self.findChild(QListWidget, 'slotSelectionListWidget')
    slotRow = self.findChild(QListWidget, 'itemsListWidget').currentRow()
    slotName = slot_mapping.get(slotRow)
    if slotSelectionListWidget.currentRow() == 0:
        self.character.setCurrentItem(slotName, None)
    else:
        for item in self.character.allAddedItems[slotName]:
            if item.name == slotSelectionListWidget.currentItem().text():
                self.character.setCurrentItem(slotName, item)
    setItemsListWidgetSlots(self, self.findChild(QListWidget, 'itemsListWidget'))
    autoUpdateRealmRank(self)

def setEquippedWeapons(self):
    autoUpdateRealmRank(self)
    
def setLevel(self):
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
    if index == 2:
        self.character.copyCurrentToTemp()
    else:
        self.character.copyTempToCurrent()
    self.tabWidget.setCurrentIndex(index)
    if slot is not None:
        self.vaultCurrentSlotWidget = self.findChild(QComboBox, 'vaultCurrentSlot')
        indexOfVaultSlot = self.vaultCurrentSlotWidget.findText(slot, Qt.MatchFlag.MatchExactly)
        self.vaultCurrentSlotWidget.setCurrentIndex(indexOfVaultSlot)
    autoUpdateRealmRank(self)
    itemsListWidget = self.findChild(QListWidget, 'itemsListWidget')
    setItemsListWidgetSlots(self, itemsListWidget)

def resetOnVaultComboBoxChange(self):
    self.character.copyTempToCurrent()
    autoUpdateRealmRank(self)
    populateVault(self)
    populateAvailable(self)
    
    vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    itemsListWidget = self.findChild(QListWidget, 'itemsListWidget').findItems(vaultCurrentSlotText, Qt.MatchFlag.MatchStartsWith)[0]
    self.findChild(QListWidget, 'itemsListWidget').setCurrentItem(itemsListWidget)
    setSlotSelectionLabel(self, vaultCurrentSlotText)
    refreshSlotSelectionListWidget(self)

def populateVault(self):
    vaultAvailableWidget = self.findChild(QListWidget, 'vaultAvailableWidget')
    vaultAvailableWidget.clear()
    vaultAvailableWidget.addItem(QListWidgetItem(str("<Empty Slot>")))
    counter = 0
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    try:
        availableVaultItems = self.character.vault.get(self.vaultCurrentSlotText)
        addedItemNames = [item.name for item in self.character.allAddedItems.get(self.vaultCurrentSlotText)]
        for item in availableVaultItems:
            if item.name in addedItemNames:
                pass
            else:
                vaultAvailableWidget.addItem(QListWidgetItem(item.name))
                counter += 1
        self.findChild(QGroupBox, 'availableItemListGroupBox').setTitle(f"Available Item List : ( {counter} )")
    except:
        pass
    
def populateAvailable(self):
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    currentlyInWidget = self.findChild(QListWidget, 'currentlyInItemListWidget')
    currentlyInWidget.clear()
    itemsToPickFrom = self.character.allAddedItems.get(self.vaultCurrentSlotText)
    counter = 0       
    for item in itemsToPickFrom:
        currentlyInWidget.addItem(QListWidgetItem(item.name))
        counter += 1
    self.findChild(QGroupBox, 'currentlyInItemList').setTitle(f"Current in Item List : ( {counter} )")

def vaultItemSingleClick(self):  
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    selectedItem = self.findChild(QListWidget, 'vaultAvailableWidget').currentItem().text()
    itemsToPickFrom = self.character.vault.get(self.vaultCurrentSlotText)
    for item in itemsToPickFrom:
        if item.name == selectedItem:
            self.character.setCurrentItem(self.vaultCurrentSlotText, item)
        else:
            self.character.setCurrentItem(self.vaultCurrentSlotText, None)
    autoUpdateRealmRank(self)

def vaultItemDoubleClick(self):
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    self.selectedItemWidget = self.findChild(QListWidget, 'vaultAvailableWidget')
    try:
        selectedItem = self.selectedItemWidget.currentItem().text()
    except:
        selectedItem = None
    if selectedItem != "<Empty Slot>" or selectedItem is not None:
        itemsToPickFrom = self.character.vault.get(self.vaultCurrentSlotText)
        for item in itemsToPickFrom:
            if item.name == selectedItem:
                self.character.addToAllItems(self.vaultCurrentSlotText, item)
                row = self.selectedItemWidget.currentRow()
                item = self.selectedItemWidget.takeItem(row)
                del item
                self.selectedItemWidget.setCurrentRow(0)                
        refreshSlotSelectionListWidget(self)
    populateVault(self)
    populateAvailable(self)
    
def vaultCurrentSingleClick(self):  
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    selectedItem = self.findChild(QListWidget, 'currentlyInItemListWidget').currentItem().text()
    if selectedItem is None:
        pass
    else:
        itemsToPickFrom = self.character.allAddedItems.get(self.vaultCurrentSlotText)
        for item in itemsToPickFrom:
            if item.name == selectedItem:
                self.character.setCurrentItem(self.vaultCurrentSlotText, item)
            else:
                self.character.setCurrentItem(self.vaultCurrentSlotText, None)
        autoUpdateRealmRank(self)

def vaultCurrentDoubleClick(self):
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    self.selectedItemWidget = self.findChild(QListWidget, 'currentlyInItemListWidget')
    if self.selectedItemWidget.count() != 0:
        selectedItem = self.selectedItemWidget.currentItem().text()
        itemsToPickFrom = self.character.allAddedItems.get(self.vaultCurrentSlotText)
        for item in itemsToPickFrom:
            if item.name == selectedItem:
                self.character.removeFromAllItems(self.vaultCurrentSlotText, item)
                try:
                    if self.character.temporaryItems[self.vaultCurrentSlotText].name == selectedItem:
                        self.character.setTempItem(self.vaultCurrentSlotText, None) 
                except:
                    pass
                row = self.selectedItemWidget.currentRow()
                item = self.selectedItemWidget.takeItem(row)
                del item
                try:
                    self.selectedItemWidget.setCurrentRow(0)
                except:
                    pass
        refreshSlotSelectionListWidget(self)
        populateVault(self)
        populateAvailable(self)
    
def refreshSlotSelectionListWidget(self):
    slotSelectionListWidget = self.findChild(QListWidget, 'slotSelectionListWidget')
    slotSelectionListWidget.clear()
    slotSelectionListWidget.addItem(QListWidgetItem(str("<Empty Slot>")))
    self.vaultCurrentSlotText = self.findChild(QComboBox, 'vaultCurrentSlot').currentText()
    for item in self.character.allAddedItems[self.vaultCurrentSlotText]:
        slotSelectionListWidget.addItem(QListWidgetItem(str(item.name)))
    autoUpdateRealmRank(self)