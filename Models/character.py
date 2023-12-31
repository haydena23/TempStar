from Models.classes import ClassType
from Models.item import Item, belt

class Character:
    def __init__(self, name, class_type: ClassType, level, champion_level, realm_rank):
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
        self.items = {
            'jewel': None,
            'neck': None,
            'cloak': None,
            'belt': belt,
            'ring_one': None,
            'ring_two': None,
            'wrist_one': None,
            'wrist_two': None,
            'chest': None,
            'head': None,
            'arms': None,
            'hands': None,
            'legs': None,
            'feet': None,
            'right_hand': None,
            'left_hand': None,
            'two_hand': None,
            'ranged': None,
            'mythirian': None,
        }
    
    def setItem(self, item: Item):
        self.items[item.slot] = item