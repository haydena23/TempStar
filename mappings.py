from class_types import *
from race_types import *

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
    "Avalonian": Armsman,
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