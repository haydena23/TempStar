from Models.classes import ClassType
from Models.item import *

class Character:
    def __init__(self, name, class_type: ClassType, level, champion_level, realm_rank, allAddedItems = None, vault = None):
        self.name = name
        self.class_type = class_type
        self.level = level
        self.champion_level = champion_level
        self.realm_rank = realm_rank
        self.total_utility = 0
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
        self.skills = class_type.skills
        self.magic_skills = class_type.magic_skills
        self.melee_skills = class_type.melee_skills
        self.dual_wield_skills = class_type.dual_wield_skills
        self.archery_skills = class_type.archery_skills
        self.allowed_races = class_type.allowed_races
        self.toa_bonuses = {
            'all_focus_levels': 50, 'all_melee_skills': 11,  'all_magic_skills': 11, 'all_dual_wielding_skills': 11,
            'all_archery_skills': 11,  'melee_speed': 10, 'melee_damage': 10, 'style_damage': 10, 'spell_speed': 10, 
            'spell_damage': 10, 'spell_range': 10, 'resist_pierce': 10, 'power_pool': 25, 'spell_duration': 25, 
            'arcane_siphoning': 25, 'healing_bonus': 25, 'buff_enhance': 25, 'debuff_bonus': 25, 'mythical_xp': 10,
            'mythical_realm_points': 10, 'mythical_bounty_points': 10, 'power_regen': 50, 'spell_level': 10, 
            'endurance_regen': 10, 'health_regen': 50, 'mythical_physical_defenses': 50, 'mythical_dps': 50, 
            'mythical_evade_chance': 10, 'mythical_safe_fall': 50, 'mythical_siege': 50, 'mythical_strength_cap': 50, 
            'mythical_constitution_cap': 50, 'mythical_dexterity_cap': 50, 'mythical_quickness_cap': 50, 
            'mythical_acuity_cap': 50, 'mythical_crush_resist': 15,  'mythical_slash_resist': 15, 'mythical_thrust_resist': 15, 
            'mythical_heat_resist': 15, 'mythical_cold_resist': 15, 'mythical_matter_resist': 15, 'mythical_energy_resist': 15, 
            'mythical_body_resist': 15, 'mythical_spirit_resist': 15, 'mythical_essence_resist': 50, 'mythical_parry_chance': 10, 
            'mythical_block_chance': 10, 'mythical_mesmerize_reduction': 50, 'mythical_stun_reduction': 50,
            'mythical_speed_decrease_reduction': 50, 'mythical_encumberance': 50,  'mythical_craft_speed': 50,
            'mythical_coin': 50
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