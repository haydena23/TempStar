from PyQt5.QtWidgets import QComboBox, QLabel, QListWidget, QCheckBox, QPushButton, QLineEdit
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import Qt

from SCCalc.sc_maps import alb_arch_maps, arch_map, imbue_caps, stat_values_by_level
from SCCalc.calculator import onNewItemCreated

from changeFunctions import autoUpdateRealmRank

def resetSpellcraftUI(self):
    resetArchtypes(self)

def initSCArmorTypes(self):
    self.scArmorComboBox.clear()
    armor = []
    for armor_type in self.character.class_type.armor_types:
        armor.append(armor_type)
    armor.sort()
    for index, armortype in enumerate(armor):
        self.scArmorComboBox.insertItem(index, armortype)
        
def setMaxImbue(self, level):
    imbueCapacityLabel = self.findChild(QLabel, 'imbueCapacityLabel')
    maxOverchargeLabel = self.findChild(QLabel, 'maxOverchargeLabel')
    capacity = imbue_caps[level]
    maxOverchargeLabel.setText(str(capacity))
    imbueCapacityLabel.setText(str(capacity - 5.5))

def setLevelBox(self):
    currentLevel = self.scLevelCombobox.currentText()
    setMaxImbue(self, currentLevel)
    setFifthSlotBonus(self)

#####################################################
############# ARCHTYPES AND STAT BOX SETTING
#####################################################

def initSCArchTypes(self):
    for i in range(1, 5):
        self.findChild(QComboBox, f'statCategory{i}').clear()
        for index, category in enumerate(alb_arch_maps):
            self.findChild(QComboBox, f'statCategory{i}').insertItem(index, category)

def resetArchtypes(self):
    for i in range(1,5):
        box = self.findChild(QComboBox, f'statCategory{i}')
        box.setCurrentIndex(0)

def setArchtypes(self, box):
    archBox = box.objectName()[-1]
    currentArchtype = box.currentText()
    statBox = self.findChild(QComboBox, f'statCombo{archBox}')
    statBox.clear()
    currentRealm = self.character.class_type.realm
    for index, stat in enumerate(arch_map[currentRealm][currentArchtype]):
        statBox.insertItem(index, stat.replace("_"," ").title())
        
    valueBox = self.findChild(QComboBox, f'statValue{archBox}')
    valueBox.clear()
    values = list(stat_values_by_level[currentArchtype])
    values.sort()
    for value in values:
        valueBox.addItem(str(value))
    autoUpdateRealmRank(self)
        
def setFifthSlotBonus(self):
    currentLevel = int(self.scLevelCombobox.currentText())
    fifSlotBonusBox = self.findChild(QComboBox, 'slot5Bonus')
    if currentLevel != 51:
        fifSlotBonusBox.setCurrentIndex(0)
        fifSlotBonusBox.setEnabled(False)
    else:
        fifSlotBonusBox.setEnabled(True)

def onChangeArmor(self):
    pass

def onSCSlotChanged(self):
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    index = self.findChild(QComboBox, 'vaultCurrentSlot').findText(currentSlot)
    self.findChild(QComboBox, 'vaultCurrentSlot').setCurrentIndex(index)
    setSCItemsListWidget(self)
    
def onSCStatComboBoxChanged(self, box):
    currentItem = self.findChild(QListWidget, 'scItemsListWidget').currentItem().text()
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    vaultCopy = None
    
    for index, item in enumerate(self.character.vault[currentSlot]):
        if item.name == currentItem:
            vaultCopy = item
            
    statToSet = {}
    comboboxes = [self.scStatComboBox1, self.scStatComboBox2, self.scStatComboBox3, self.scStatComboBox4]
    for index, box in enumerate(comboboxes):
        if box.currentText() != '<Empty>':
            statToSet[box.currentText().lower().replace(" ","_")] = int(self.findChild(QComboBox, f'statValue{box.objectName()[-1]}').currentText())
    vaultCopy.setStats(statToSet)
    autoUpdateRealmRank(self)
    
def updateAfterValueChange(self):
    currentItem = self.findChild(QListWidget, 'scItemsListWidget').currentItem().text()
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    vaultCopy = None
    
    for index, item in enumerate(self.character.vault[currentSlot]):
        if item.name == currentItem:
            vaultCopy = item
            
    statToSet = {}
    comboboxes = [self.scStatComboBox1, self.scStatComboBox2, self.scStatComboBox3, self.scStatComboBox4]
    for index, box in enumerate(comboboxes):
        if box.currentText() != '<Empty>':
            statToSet[box.currentText().lower().replace(" ","_")] = int(self.findChild(QComboBox, f'statValue{box.objectName()[-1]}').currentText())
    vaultCopy.setStats(statToSet)
    autoUpdateRealmRank(self)
    
#####################################################
############# Item Handler
#####################################################

def checkForItemsForDisable(self):
    scCurrentSlot = self.findChild(QListWidget, 'scItemsListWidget').count()
    if scCurrentSlot == 0:
        for i in range(1, 5):
            self.findChild(QComboBox, f'statCategory{i}').setEnabled(False)
            self.findChild(QComboBox, f'statCombo{i}').setEnabled(False)
            self.findChild(QComboBox, f'statValue{i}').setEnabled(False)
        self.findChild(QComboBox, 'slot5Bonus').setEnabled(False)
        self.findChild(QListWidget, 'procsList').setEnabled(False)
        self.findChild(QPushButton, 'scClearStatsButton').setEnabled(False)
        self.findChild(QPushButton, 'scDeleteItemButton').setEnabled(False)
        self.findChild(QComboBox, 'scArmorTypeCombo').setEnabled(True)
        self.findChild(QComboBox, 'scArmorLevelCombo').setEnabled(True)
        self.findChild(QLineEdit, 'scArmorNameBox').setEnabled(False)
    else:
        for i in range(1, 5):
            self.findChild(QComboBox, f'statCategory{i}').setEnabled(True)
            self.findChild(QComboBox, f'statCombo{i}').setEnabled(True)
            self.findChild(QComboBox, f'statValue{i}').setEnabled(True)
        self.findChild(QComboBox, 'slot5Bonus').setEnabled(True)
        self.findChild(QListWidget, 'procsList').setEnabled(True)
        self.findChild(QPushButton, 'scClearStatsButton').setEnabled(True)
        self.findChild(QPushButton, 'scDeleteItemButton').setEnabled(True)
        self.findChild(QComboBox, 'scArmorTypeCombo').setEnabled(False)
        self.findChild(QComboBox, 'scArmorLevelCombo').setEnabled(False)
        
def createNewItem(self):
    itemListWidget = self.findChild(QListWidget, 'scItemsListWidget')
    currentItemLevel = self.findChild(QComboBox, 'scArmorLevelCombo').currentText()
    armorType = self.findChild(QComboBox, 'scArmorTypeCombo').currentText()
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    
    index = self.findChild(QComboBox, 'vaultCurrentSlot').findText(currentSlot)
    self.findChild(QComboBox, 'vaultCurrentSlot').setCurrentIndex(index)
    
    existingNumbers = []
    for i in range(itemListWidget.count()):
        itemText = itemListWidget.item(i).text()
        try:
            num = int(itemText.split()[-1])
            existingNumbers.append(num)
        except Exception as e:
            print(f"Error in createNewItem: {e}")

    existingNumbers.sort()
    missingNumber = 1
    for num in existingNumbers:
        if num == missingNumber:
            missingNumber += 1
        else:
            break
    
    name = f'Level {currentItemLevel} {armorType} {currentSlot}'
    nameMissing = f'Level {currentItemLevel} {armorType} {currentSlot} {missingNumber}'
    nameCopies = itemListWidget.findItems(name, Qt.MatchFlag.MatchExactly)
    if len(nameCopies) != 0:
        name = nameMissing
    newItem = QListWidgetItem(name)
    itemListWidget.addItem(newItem)
    itemListWidget.setCurrentItem(newItem)
    checkForItemsForDisable(self)
    onNewItemCreated(self, name)
    
def deleteItem(self):
    itemListWidget = self.findChild(QListWidget, 'scItemsListWidget')
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    try:
        currentRow = itemListWidget.currentRow()
        itemToDelete = itemListWidget.takeItem(currentRow)
        itemName = itemToDelete.text()
        del itemToDelete
        itemObjectVault = None
        itemObjectAllAddedItems = None
        
        for index, item in enumerate(self.character.vault[currentSlot]):
            if item.name == itemName:
                itemObjectVault = self.character.vault[currentSlot][index]
        for index, item in enumerate(self.character.allAddedItems[currentSlot]):
            if item.name == itemName:
                itemObjectAllAddedItems = self.character.allAddedItems[currentSlot][index]
        self.character.removeFromVault(currentSlot, itemObjectVault)
        self.character.removeFromAllItems(currentSlot, itemObjectAllAddedItems)
        self.character.setCurrentItem(currentSlot, None)
        self.character.setTempItem(currentSlot, None)
        
        itemsList = self.findChild(QListWidget, 'itemsListWidget')
        itemListWidgetItem = itemsList.findItems(currentSlot, Qt.MatchFlag.MatchStartsWith)[0]
        if "<Empty Slot>" not in itemListWidgetItem.text():
            itemListWidgetItem.setText(f"{currentSlot}:\t\t<Empty Slot>")
        checkForItemsForDisable(self)
        autoUpdateRealmRank(self)
                
    except Exception as e:
        print(f'Error in deleteItem: {e}')
        
def setSCItemsListWidget(self):
    itemsListWidget = self.findChild(QListWidget, 'scItemsListWidget')
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    
    itemsListWidget.clear()
    
    try:
        availableVaultItems = self.character.vault.get(currentSlot)
        
        for item in availableVaultItems:
            if item.slot == currentSlot and item.crafted == "Yes":
                if item.item_type in self.character.class_type.weaponry or item.item_type in self.character.class_type.armor_types:
                    if item.realm == "All" or item.realm == self.character.class_type.realm:
                        if item.item_type == 'Shield' and item.shield_size not in self.character.class_type.shield_types:
                            pass
                        elif (item.slot == 'Left Hand' and item.item_type != 'Shield' and 
                            len(self.character.dual_wield_skills) == 0 and currentSlot == 'Left Hand'):
                            pass
                        else:
                            itemsListWidget.addItem(QListWidgetItem(item.name))
        
        itemsListWidget.sortItems(Qt.SortOrder.AscendingOrder)
    except Exception as e:
        print(f"Error in setSCItemsListWidget: {e}")