from PyQt5.QtWidgets import QComboBox, QLabel, QListWidget, QCheckBox, QPushButton, QLineEdit
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import Qt

from SCCalc.sc_maps import alb_arch_maps, arch_map, imbue_caps
from SCCalc.calculator import onNewItemCreated

def resetSpellcraftUI(self):
    resetArchtypes(self)

def initSCArmorTypes(self):
    self.scArmorComboBox.clear()
    armor = []
    for armor_type in self.character.class_type.armor_types:
        armor.append(armor_type)
    armor.sort()
    currentSlot = self.findChild(QComboBox, 'scArmorTypeCombo').currentText()
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
    statBox = self.findChild(QComboBox, f'gemCombo{archBox}')
    statBox.clear()
    currentRealm = self.character.class_type.realm
    for index, stat in enumerate(arch_map[currentRealm][currentArchtype]):
        statBox.insertItem(index, stat.replace("_"," ").title())
        
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

#####################################################
############# Item Handler
#####################################################

def checkForItemsForDisable(self):
    scCurrentSlot = self.findChild(QListWidget, 'scItemsListWidget').count()
    if scCurrentSlot == 0:
        self.findChild(QCheckBox, 'autonameCheckbox').setEnabled(False)
        for i in range(1, 5):
            self.findChild(QComboBox, f'statCategory{i}').setEnabled(False)
            self.findChild(QComboBox, f'gemCombo{i}').setEnabled(False)
            self.findChild(QComboBox, f'gem{i}Value').setEnabled(False)
        self.findChild(QComboBox, 'slot5Bonus').setEnabled(False)
        self.findChild(QListWidget, 'procsList').setEnabled(False)
        self.findChild(QPushButton, 'scClearStatsButton').setEnabled(False)
        self.findChild(QPushButton, 'scDeleteItemButton').setEnabled(False)
        self.findChild(QComboBox, 'scArmorTypeCombo').setEnabled(False)
        self.findChild(QComboBox, 'scArmorLevelCombo').setEnabled(False)
        self.findChild(QLineEdit, 'scArmorNameBox').setEnabled(False)
    else:
        self.findChild(QCheckBox, 'autonameCheckbox').setEnabled(True)
        for i in range(1, 5):
            self.findChild(QComboBox, f'statCategory{i}').setEnabled(True)
            self.findChild(QComboBox, f'gemCombo{i}').setEnabled(True)
            self.findChild(QComboBox, f'gem{i}Value').setEnabled(True)
        self.findChild(QComboBox, 'slot5Bonus').setEnabled(True)
        self.findChild(QListWidget, 'procsList').setEnabled(True)
        self.findChild(QPushButton, 'scClearStatsButton').setEnabled(True)
        self.findChild(QPushButton, 'scDeleteItemButton').setEnabled(True)
        self.findChild(QComboBox, 'scArmorTypeCombo').setEnabled(True)
        self.findChild(QComboBox, 'scArmorLevelCombo').setEnabled(True)
        self.findChild(QLineEdit, 'scArmorNameBox').setEnabled(True)
        
def createNewItem(self):
    itemListWidget = self.findChild(QListWidget, 'scItemsListWidget')
    currentItemLevel = self.findChild(QComboBox, 'scArmorLevelCombo').currentText()
    armorType = self.findChild(QComboBox, 'scArmorTypeCombo').currentText()
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    
    index = self.findChild(QComboBox, 'vaultCurrentSlot').findText(currentSlot)
    self.findChild(QComboBox, 'vaultCurrentSlot').setCurrentIndex(index)
    
    name = f'Level {currentItemLevel} {armorType} {currentSlot}'
    nameCopies = itemListWidget.findItems(name, Qt.MatchFlag.MatchContains)
    if len(nameCopies) != 0:
        count = str(len(nameCopies))
        name = f'Level {currentItemLevel} {armorType} {currentSlot} {count}'
    newItem = QListWidgetItem(name)
    itemListWidget.addItem(newItem)
    itemListWidget.setCurrentItem(newItem)
    checkForItemsForDisable(self)
    onNewItemCreated(self, name)
    
def deleteItem(self):
    itemListWidget = self.findChild(QListWidget, 'scItemsListWidget')
    try:
        currentlyRow = itemListWidget.currentRow()
        itemToDelete = itemListWidget.takeItem(currentlyRow)
        del itemToDelete
        checkForItemsForDisable(self)
    except Exception as e:
        print(f'Error: {e}')