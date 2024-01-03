from Models.classes import *
from Models.races import *

stats_row_mapping = {
    'strength': 0, 
    'constitution': 1, 
    'dexterity': 2, 
    'quickness': 3,
    'piety': 4, 
    'intelligence': 5, 
    'empathy': 6, 
    'charisma': 7,
    'acuity': 8, 
    'fatigue': 9, 
    'power_points': 10, 
    'hit_points': 11, 
    'armor_factor': 12
}

stats_cap_mapping = {
    'strength_cap': 0, 
    'constitution_cap': 1, 
    'dexterity_cap': 2, 
    'quickness_cap': 3,
    'piety_cap': 4, 
    'intelligence_cap': 5, 
    'empathy_cap': 6, 
    'charisma_cap': 7,
    'acuity_cap': 8, 
    'fatigue_cap': 9, 
    'power_points_cap': 10, 
    'hit_points_cap': 11
}

resists_row_mapping = {
    'crush_resist': 0, 
    'slash_resist': 1, 
    'thrust_resist': 2, 
    'heat_resist': 3, 
    'cold_resist': 4,
    'matter_resist': 5, 
    'energy_resist': 6, 
    'body_resist': 7, 
    'spirit_resist': 8,
    'essence_resist': 9
}

class_type_mapping = {
    "(Alb) Armsman": Armsman,
    "(Alb) Cabalist": Cabalist,
    "(Alb) Cleric": Cleric,
    "(Alb) Friar": Friar,
    "(Alb) Heretic": Heretic,
    "(Alb) Infiltrator": Infiltrator,
    "(Alb) Mauler": Mauler_Alb,
    "(Alb) Mercenary": Mercenary,
    "(Alb) Minstrel": Minstrel,
    "(Alb) Necromancer": Necromancer,
    "(Alb) Paladin": Paladin,
    "(Alb) Reaver": Reaver,
    "(Alb) Scout": Scout,
    "(Alb) Sorcerer": Sorcerer,
    "(Alb) Theurgist": Theurgist,
    "(Alb) Wizard": Wizard,
    "(Hib) Animist": Animist,
    "(Hib) Bainshee": Bainshee,
    "(Hib) Bard": Bard,
    "(Hib) Blademaster": Blademaster,
    "(Hib) Champion": Champion,
    "(Hib) Druid": Druid,
    "(Hib) Eldritch": Eldritch,
    "(Hib) Enchanter": Enchanter,
    "(Hib) Hero": Hero,
    "(Hib) Mauler": Mauler_Hib,
    "(Hib) Mentalist": Mentalist,
    "(Hib) Nightshade": Nightshade,
    "(Hib) Ranger": Ranger,
    "(Hib) Valewalker": Valewalker,
    "(Hib) Vampiir": Vampiir,
    "(Hib) Warden": Warden,
    "(Mid) Berserker": Berserker,
    "(Mid) Bonedancer": Bonedancer,
    "(Mid) Healer": Healer,
    "(Mid) Hunter": Hunter,
    "(Mid) Mauler": Mauler_Mid,
    "(Mid) Runemaster": Runemaster,
    "(Mid) Savage": Savage,
    "(Mid) Shadowblade": Shadowblade,
    "(Mid) Shaman": Shaman,
    "(Mid) Skald": Skald,
    "(Mid) Spiritmaster": Spiritmaster,
    "(Mid) Thane": Thane,
    "(Mid) Valkyrie": Valkyrie,
    "(Mid) Warlock": Warlock,
    "(Mid) Warrior": Warrior,
}

race_type_mapping = {
    "<None>": NoRace,
    "Avalonian": Avalonian,
    "Briton": Briton,
    "Half-Ogre": HalfOgre,
    "Highlander": Highlander,
    "Inconnu": Inconnu,
    "Saracen": Saracen,
    "Celt": Celt,
    "Elf": Elf,
    "Firbolg": Firbolg,
    "Lurikeen": Lurikeen,
    "Shar": Shar,
    "Sylvan": Sylvan,
    "Dwarf": Dwarf,
    "Frostalf": Frostalf,
    "Kobold": Kobold,
    "Norseman": Norseman,
    "Troll": Troll,
    "Valkyn": Valkyn,
    "Minotaur": Minotaur
}

main_stats_default_caps = {
    'strength': 75, 
    'constitution': 75, 
    'dexterity': 75, 
    'quickness': 75,
    'piety': 75, 
    'intelligence': 75, 
    'empathy': 75, 
    'charisma': 75,
    'acuity': 75, 
    'fatigue': 50, 
    'power_points': 26, 
    'hit_points': 200, 
    'armor_factor': 50
}

stat_cap_default_caps = {
    'strength_cap': 26, 
    'constitution_cap': 26, 
    'dexterity_cap': 26, 
    'quickness_cap': 26,
    'piety_cap': 26, 
    'intelligence_cap': 26, 
    'empathy_cap': 26, 
    'charisma_cap': 26,
    'acuity_cap': 26, 
    'fatigue_cap': 25, 
    'power_points_cap': 50, 
    'hit_points_cap': 200
}

resists_default_caps = {
    'crush_resist': 26, 
    'slash_resist': 26, 
    'thrust_resist': 26, 
    'heat_resist': 26, 
    'cold_resist': 26,
    'matter_resist': 26, 
    'energy_resist': 26, 
    'body_resist': 26, 
    'spirit_resist': 26,
    'essence_resist': 26
}

skills_default_caps = {
    'skill1': 11,
    'skill2': 11,
    'skill3': 11,
    'skill4': 11,
    'skill5': 11,
    'skill6': 11,
    'skill7': 11,
    'skill8': 11,
}

default_caps_map = {
    'statsTable': main_stats_default_caps,
    'statsCapTable': stat_cap_default_caps,
    'resistsTable': resists_default_caps,
    'skillsTable': skills_default_caps
}

table_names = {
    'statsTable',
    'statsCapTable',
    'resistsTable',
    'skillsTable',
    # 'bonusesTable'
}

realm_rank_map = {
    'RR1': 1,
    'RR2': 2,
    'RR3': 3,
    'RR4': 4,
    'RR5': 5,
    'RR6': 6,
    'RR7': 7,
    'RR8': 8,
    'RR9': 9,
    'RR10': 10,
    'RR11': 11,
    'RR12': 12,
    'RR13': 13,
    'RR14': 14,
}

slot_mapping = {
    0: 'Jewel',
    1: 'Neck',
    2: 'Cloak',
    3: 'Belt',
    4: 'Ring 1',
    5: 'Ring 2',
    6: 'Wrist 1',
    7: 'Wrist 2',
    8: 'Chest',
    9: 'Head',
    10: 'Arms',
    11: 'Hands',
    12: 'Legs',
    13: 'Feet',
    14: 'Right Hand',
    15: 'Left Hand',
    16: 'Two Hand',
    17: 'Ranged',
    18: 'Mythirian'
}