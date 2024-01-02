from newCharacter import new_character_change
from statsHandler import updateResistsFromRace, adjustSkillsFromRealmRank

# REMOVE BELOW
from statsHandler import calculateNowStats

from Models.classes import *
from Models.races import *

from PyQt5.QtWidgets import QLabel, QTableWidget, QTableWidgetItem

def changeClass(self, class_type: ClassType):
    if(self.lockTemplate == False):
        new_character_change(self, class_type)
        
def changeRace(self, race_type: RaceType):
    updateResistsFromRace(self, race_type)

def changeChampionLevel(self):
    pass

def changeRealmRank(self, realm_rank):
    adjustSkillsFromRealmRank(self, realm_rank)
    # pass

def changeLevel(self):
    pass

def changeWeapons(self):
    pass

def setSlotSelectionLabel(self, text):
    text = str(text).replace(":","")
    label = self.findChild(QLabel, 'slotSelectionLabel')
    label.setText(f"{text} Slot Selections :")
    
    #Remove below
    calculateNowStats(self)