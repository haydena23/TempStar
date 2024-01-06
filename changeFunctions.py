from newCharacter import new_character_change
from statsHandler import updateResistsFromRace, adjustSkillsFromRealmRank

from statsHandler import adjustSkillsFromRealmRank, autoUpdateRealmRank, calculateNowStats

from Models.classes import ClassType, RaceType
from Models.mappings import slot_mapping
from widgets import unequipMessageBox

from PyQt5.QtWidgets import QLabel, QListWidget, QListWidgetItem, QComboBox, QTabWidget
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

def setInformationTextEdit(self):
    pass

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
    self.tabWidget.setCurrentIndex(index)
    if slot is not None:
        self.vaultCurrentSlotWidget = self.findChild(QComboBox, 'vaultCurrentSlot')
        indexOfVaultSlot = self.vaultCurrentSlotWidget.findText(slot, Qt.MatchFlag.MatchExactly)
        self.vaultCurrentSlotWidget.setCurrentIndex(indexOfVaultSlot)