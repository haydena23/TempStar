from PyQt5.QtWidgets import QComboBox, QLabel, QListWidget, QCheckBox, QPushButton, QLineEdit
from PyQt5.QtWidgets import QListWidgetItem, QTextEdit
from PyQt5.QtCore import Qt, QItemSelectionModel

from SCCalc.sc_maps import alb_arch_maps, arch_map, imbue_caps, stat_values_by_level
from SCCalc.armor_maps import armor_by_realm
from SCCalc.calculator import onNewItemCreated, calculateTotalImbueCost

def initSCArmorTypes(self):
    self.scArmorComboBox.clear()
    armor = list(self.character.class_type.armor_types)
    preferred_order = ['Cloth', 'Leather', 'Studded', 'Reinforced', 'Chain', 'Scale', 'Plate']
    ordered_armor = [armor_type for armor_type in preferred_order if armor_type in armor]
    for armor_type in ordered_armor:
        self.scArmorComboBox.addItem(armor_type)
        
def setMaxImbue(self, level):
    pass

def setLevelBox(self):
    pass

#####################################################
############# ARCHTYPES AND STAT BOX SETTING
#####################################################

def initSCArchTypes(self):
    for i in range(1, 5):
        self.findChild(QComboBox, f'statCategory{i}').clear()
        for index, category in enumerate(alb_arch_maps):
            self.findChild(QComboBox, f'statCategory{i}').insertItem(index, category)

def setArchtypes(self, box):
    pass

def setItemNameBox(self):
    pass

def setFifthSlotBonus(self):
    pass

def onChangeArmor(self):
    print(self.scItems)
    pass

def onSCSlotChanged(self):
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    index = self.findChild(QComboBox, 'vaultCurrentSlot').findText(currentSlot)
    self.findChild(QComboBox, 'vaultCurrentSlot').setCurrentIndex(index)

def onSCStatComboBoxChanged(self, box):
    pass
    
def updateAfterValueChange(self):
    pass
    
#####################################################
############# Labels
#####################################################
    
def setImbueLabels(self, costs):
    pass

#####################################################
############# Item Handler
#####################################################
    
def checkForItemsForDisable(self):
    pass
        
#####################################################
############# Item List Widget
#####################################################

def initSCItemsListWidget(self, listWidget):
    listWidget.addItem(QListWidgetItem(str("<Empty Slot>")))
    currentSlot = getCurrentSlot(self)
    for index, item in enumerate(self.character.vault[currentSlot]):
        if item.slot == currentSlot and item.crafted:
            itemWidget = QListWidgetItem(str(item.name))
            listWidget.addItem(itemWidget)
            self.scItems.append({'listWidgetItem': itemWidget, 'itemInVault': item, 'itemName': item.name})
    listWidget.setCurrentItem(listWidget.item(0))
    
def onSCItemClicked(self, index):
    if index == 0:
        resetSCPage(self)
        return
    print(getItemDetails(self))

def createNewItem(self):
    pass
    
def deleteItem(self):
    pass

#####################################################
############# Helper Functions
#####################################################
def resetSCPage(self):
    pass

def renameItem(self, name):
    pass

def setInfoBox(self):
    pass

def getItemDetails(self):
    if self.scItemList.currentRow() != 0:
        currentSelectionItem = self.scItemList.currentItem()
        for itemSet in self.scItems:
            if itemSet['listWidgetItem'] == currentSelectionItem:
                return itemSet
        return None

def getCurrentSlot(self):
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    return currentSlot