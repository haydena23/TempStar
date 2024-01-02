from newCharacter import new_character_change
from statsHandler import updateResistsFromRace, adjustSkillsFromRealmRank

# REMOVE BELOW
from statsHandler import calculateNowStats, adjustSkillsFromRealmRank, autoUpdateRealmRank

from Models.classes import *
from Models.races import *
from Models.mappings import *
from Models.item import belt

from PyQt5.QtWidgets import QLabel, QComboBox, QMessageBox

def changeClass(self, class_type: ClassType):
    if(self.lockTemplate == False):
        new_character_change(self, class_type)
        
def changeRace(self, race_type: RaceType):
    updateResistsFromRace(self, race_type)

def changeChampionLevel(self):
    pass

def changeRealmRank(self, realm_rank):
    adjustSkillsFromRealmRank(self, realm_rank)

def changeLevel(self):
    pass

def changeWeapons(self):
    pass

def setSlotSelectionLabel(self, text):
    text = str(text).replace(":","")
    text = str(text).replace(" <Empty Slot>","")
    label = self.findChild(QLabel, 'slotSelectionLabel')
    label.setText(f"{text} Slot Selections :")
    
    #Remove below
    self.character.setItem('belt', belt)
    autoUpdateRealmRank(self)

def unquipAllSlotsWarning(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText("Are you sure you want to unequip all items?")
    msgBox.setWindowTitle("Confirm Unequip")
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Yes:
        unequipAllSlots(self)

def unequipAllSlots(self):
    for slot in self.character.items:
        self.character.setItem(slot,None)
    autoUpdateRealmRank(self)