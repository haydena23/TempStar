from newCharacter import new_character_change
from statsHandler import updateResistsFromRace

from Models.class_types import *
from Models.race_types import *

def changeClass(self, class_type: ClassType):
    if(self.lockTemplate == False):
        new_character_change(self, class_type)
        
def changeRace(self, race_type: RaceType):
    updateResistsFromRace(self, race_type)