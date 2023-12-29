from newCharacter import new_character_change
from class_types import *

def changeClass(self, class_type: ClassType):
    if(self.lockTemplate == False):
        new_character_change(self, class_type)