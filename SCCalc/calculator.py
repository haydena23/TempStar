from PyQt5.QtWidgets import QComboBox

from Models.item import Item
from changeFunctions import autoUpdateRealmRank

def onNewItemCreated(self, name):
    slot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    level = int(self.findChild(QComboBox, 'scArmorLevelCombo').currentText())
    itemType = self.findChild(QComboBox, 'scArmorTypeCombo').currentText()
    newSCItem = Item(
        slot, # Slot
        "", # Shield Size
        name, # Name
        {}, # Stats
        0, # Single Utility
        0, # Total Utility
        level, # Level
        1, # Bonus level
        self.character.class_type.realm, # Realm
        0, # Armor Factor
        "All", # Usable
        "Yes", # Tradeable
        itemType, # Item Type
        "99%", # Quality
        0, # DPS
        0, # Speed
        "", # Damage Type
        "Yes" # Crafted
    )
    self.character.addToVault(slot, newSCItem)
    self.character.addToAllItems(slot, newSCItem)
    self.character.setCurrentItem(slot, newSCItem)
    self.character.setTempItem(slot, newSCItem)
    autoUpdateRealmRank(self)