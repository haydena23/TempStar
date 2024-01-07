from Models.classes import ClassType
from Models.item import *

class Character:
    def __init__(self, name, class_type: ClassType, level, champion_level, realm_rank, allAddedItems = None, vault = None):
        self.name = name
        self.class_type = class_type
        self.level = level
        self.champion_level = champion_level
        self.realm_rank = realm_rank
        self.base_stats = {
            'strength': 0, 'constitution': 0, 'dexterity': 0, 'quickness': 0,
            'piety': 0, 'intelligence': 0, 'empathy': 0, 'charisma': 0,
            'acuity': 0, 'fatigue': 0, 'power_points': 0, 'hit_points': 0, 'armor_factor': 0
        }
        self.stat_caps = {
            'strength_cap': 0, 'constitution_cap': 0, 'dexterity_cap': 0, 'quickness_cap': 0,
            'piety_cap': 0, 'intelligence_cap': 0, 'empathy_cap': 0, 'charisma_cap': 0,
            'acuity_cap': 0, 'fatigue_cap': 0, 'power_points_cap': 0, 'hit_points_cap': 0
        }
        self.resists = {
            'crush_resist': 0, 'slash_resist': 0, 'thrust_resist': 0, 'heat_resist': 0, 'cold_resist': 0,
            'matter_resist': 0, 'energy_resist': 0, 'body_resist': 0, 'spirit_resist': 0, 'essence_resist': 0
        }
        self.magic_skills = class_type.magic_skills
        self.melee_skills = class_type.melee_skills
        self.allowed_races = class_type.allowed_races
        self.toa_bonuses = {
            'melee_speed': 0, 'melee_damage': 0, 'style_damage': 0, 'power_pool': 0,
            'spell_speed': 0, 'spell_damage': 0, 'spell_range': 0, 'spell_pierce': 0,
            'spell_duration': 0, 'arcane_siphoning': 0, 'healing_bonus': 0, 'buff_enhance': 0,
            'debuff_bonus': 0, 'xp_bonus': 0, 'rp_bonus': 0, 'bp_bonus': 0,
        }
        self.currentItems = {
            'Jewel': None,
            'Neck': None,
            'Cloak': None,
            'Belt': None,
            'Ring 1': None,
            'Ring 2': None,
            'Wrist 1': None,
            'Wrist 2': None,
            'Chest': None,
            'Head': None,
            'Arms': None,
            'Hands': None,
            'Legs': None,
            'Feet': None,
            'Right Hand': None,
            'Left Hand': None,
            'Two Hand': None,
            'Ranged': None,
            'Mythirian': None,
        }
        self.allAddedItems = allAddedItems if allAddedItems is not None else{
            'Jewel': [],
            'Neck': [],
            'Cloak': [],
            'Belt': [],
            'Ring 1': [],
            'Ring 2': [],
            'Wrist 1': [],
            'Wrist 2': [],
            'Chest': [],
            'Head': [],
            'Arms': [],
            'Hands': [],
            'Legs': [],
            'Feet': [],
            'Right Hand': [],
            'Left Hand': [],
            'Two Hand': [],
            'Ranged': [],
            'Mythirian': [],
        }
        self.vault = vault if vault is not None else {
            'Jewel': [],
            'Neck': [],
            'Cloak': [],
            'Belt': [],
            'Ring 1': [],
            'Ring 2': [],
            'Wrist 1': [],
            'Wrist 2': [],
            'Chest': [],
            'Head': [],
            'Arms': [],
            'Hands': [],
            'Legs': [],
            'Feet': [],
            'Right Hand': [],
            'Left Hand': [],
            'Two Hand': [],
            'Ranged': [],
            'Mythirian': [],
        }
        self.temporaryItems = {
            'Jewel': None,
            'Neck': None,
            'Cloak': None,
            'Belt': None,
            'Ring 1': None,
            'Ring 2': None,
            'Wrist 1': None,
            'Wrist 2': None,
            'Chest': None,
            'Head': None,
            'Arms': None,
            'Hands': None,
            'Legs': None,
            'Feet': None,
            'Right Hand': None,
            'Left Hand': None,
            'Two Hand': None,
            'Ranged': None,
            'Mythirian': None,
        }
    
    def setCurrentItem(self, slot, item: Item):
        self.currentItems[slot] = item
        
    def setTempItem(self, slot, item: Item):
        self.temporaryItems[slot] = item
    
    def addToVault(self, slot, item: Item):
        self.vault[slot].append(item)
    
    def addToAllItems(self, slot, item: Item):
        self.allAddedItems[slot].append(item)
    
    def removeFromAllItems(self, slot, item: Item):
        self.allAddedItems[slot].remove(item)
    
    def copyCurrentToTemp(self):
        self.temporaryItems = self.currentItems.copy()
    
    def copyTempToCurrent(self):
        self.currentItems = self.temporaryItems.copy()
