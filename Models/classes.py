from Models.races import *

class ClassType:
    def __init__(self, name, skills, magic_skills, melee_skills, dual_wield_skills, archery_skills, allowed_races: RaceType, armor_types, realm):
        self.name = name
        self.skills = skills
        self.magic_skills = magic_skills
        self.melee_skills = melee_skills
        self.dual_wield_skills = dual_wield_skills 
        self.archery_skills = archery_skills
        self.allowed_races = allowed_races
        self.armor_types = armor_types
        self.realm = realm

##################################
#       Hibernian Classes
##################################

Armsman = ClassType(
    "(Alb) Armsman",
    skills={'Shields Skill': 0,
            'Parry Skill': 0},
    magic_skills={},
    melee_skills={'Crush Skill': 0, 
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Polearm Skill': 0,
                  'Two Handed Skill': 0,
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   Highlander,
                   Inconnu,
                   Saracen,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain',
                 'Plate'},
    realm={'Albion'}
)

Cabalist = ClassType(
    "(Alb) Cabalist",
    skills={},
    magic_skills={'Matter Magic Skill': 0,
                  'Body Magic Skill': 0,
                  'Spirit Magic Skill': 0
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Briton, 
                   Avalonian,
                   Saracen,
                   Inconnu,
                   HalfOgre,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Albion'}
)

Cleric = ClassType(
    "(Alb) Cleric",
    skills={},
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0,
                  'Smite Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Briton, 
                   Avalonian,
                   Highlander,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Albion'}
)

Friar = ClassType(
    "(Alb) Friar",
    skills={'Parry Skill': 0},
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Briton, 
                   Avalonian,
                   Highlander,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather'},
    realm={'Albion'}
)

Heretic = ClassType(
    "(Alb) Heretic",
    skills={'Shields Skill': 0,
},
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Crush Skill': 0,
                  'Flexible Skill': 0,
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Briton, 
                   Avalonian,
                   Highlander,
                   Saracen,
                   Inconnu,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Albion'}
)

Infiltrator = ClassType(
    "(Alb) Infiltrator",
    skills={'Stealth Skill': 0,
            'Envenom Skill': 0,
            'Critical Strike Skill': 0},
    magic_skills={},
    melee_skills={'Slash Skill': 0,
                  'Thrust Skill': 0,
                  },    
    dual_wield_skills={'Dual Wield Skill': 0},
    archery_skills={},
    allowed_races={Briton, 
                   Highlander,
                   Saracen,
                   Inconnu,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather'},
    realm={'Albion'}
)

Mauler_Alb = ClassType(
    "(Alb) Mauler",
    skills={},
    magic_skills={},
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={},
    armor_types={},
    realm={'Albion'}
)

Mercenary = ClassType(
    "(Alb) Mercenary",
    skills={'Shields Skill': 0,
            'Parry Skill': 0,},
    magic_skills={},
    melee_skills={'Crush Skill': 0,
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  },
    dual_wield_skills={'Dual Wield Skill': 0},
    archery_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   Highlander,
                   Inconnu,
                   Saracen,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Albion'}
)

Minstrel = ClassType(
    "(Alb) Minstrel",
    skills={'Stealth Skill': 0},
    magic_skills={'Instruments Skill': 0,
                  },
    melee_skills={'Slash Skill': 0,
                  'Thrust Skill': 0
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Briton,
                   Highlander,
                   Inconnu,
                   Saracen,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Albion'}
)

Necromancer = ClassType(
    "(Alb) Necromancer",
    skills={},
    magic_skills={'Deathsight Skill': 0,
                  'Painworking Skill': 0,
                  'Death Servant Skill': 0
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   Inconnu,
                   Saracen,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Albion'}
)

Paladin = ClassType(
    "(Alb) Paladin",
    skills={'Shields Skill': 0,
            'Parry Skill': 0,},
    magic_skills={'Chants Skill': 0,
                  },
    melee_skills={'Crush Skill': 0,
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Two Handed Skill': 0,
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   Highlander,
                   Saracen,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain',
                 'Plate'},
    realm={'Albion'}
)

Reaver = ClassType(
    "(Alb) Reaver",
    skills={'Shield Skill': 0,
            'Parry Skill': 0,},
    magic_skills={'Soulrending Skill': 0,
                  },
    melee_skills={'Crush Skill': 0,
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Flexible Skill': 0,
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Briton,
                   Inconnu,
                   Saracen,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Albion'}
)

Scout = ClassType(
    "(Alb) Scout",
    skills={'Stealth Skill': 0,
            'Shields Skill': 0,},
    magic_skills={},
    melee_skills={'Slash Skill': 0,
                  'Thrust Skill': 0,
                  },
    dual_wield_skills={},
    archery_skills={'Archery Skill': 0},
    allowed_races={Briton,
                   Highlander,
                   Inconnu,
                   Saracen,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded'},
    realm={'Albion'}
)

Sorcerer = ClassType(
    "(Alb) Sorcerer",
    skills={},
    magic_skills={'Matter Magic Skill': 0,
                  'Body Magic Skill': 0,
                  'Mind Magic Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   Inconnu,
                   Saracen,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Albion'}
)

Theurgist = ClassType(
    "(Alb) Theurgist",
    skills={},
    magic_skills={'Earth Magic Skill': 0,
                  'Cold Magic Skill': 0,
                  'Wind Magic Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Albion'}
)

Wizard = ClassType(
    "(Alb) Wizard",
    skills={},
    magic_skills={'Earth Magic Skill': 0,
                  'Cold Magic Skill': 0,
                  'Fire Magic Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   Inconnu,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Albion'}
)

##################################
#       Hibernian Classes
##################################

Animist = ClassType(
    "(Hib) Animist",
    skills={},
    magic_skills={'Arboreal Path Skill': 0,
                  'Creeping Path Skill': 0,
                  'Verdant Path Skill': 0
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   Elf,
                   Sylvan,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Hibernia'}
)

Bainshee = ClassType(
    "(Hib) Bainshee",
    skills={},
    magic_skills={'Spectral Guard Skill': 0,
                  'Phantasmal Wail Skill': 0,
                  'Ethereal Shriek Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Hibernia'}
)

Bard = ClassType(
    "(Hib) Bard",
    skills={},
    magic_skills={'Regrowth Skill': 0,
                  'Nurture Skill': 0,
                  'Music Skill': 0,
                  },
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Reinforced'},
    realm={'Hibernia'}
)

Blademaster = ClassType(
    "(Hib) Blademaster",
    skills={'Shields Skill': 0,
            'Parry Skill': 0,},
    magic_skills={},
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0,
                  'Piercing Skill': 0,
                  },
    dual_wield_skills={'Celtic Dual Skill': 0},
    archery_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   Elf,
                   Lurikeen,
                   Shar,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Reinforced'},
    realm={'Hibernia'}
)

Champion = ClassType(
    "(Hib) Champion",
    skills={'Shields Skill': 0,
            'Parry Skill': 0,},
    magic_skills={'Valor Skill': 0,
                  },
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0,
                  'Piercing Skill': 0,
                  'Large Weapons Skill': 0,
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   Sylvan,
                   Shar,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Reinforced',
                 'Scale'},
    realm={'Hibernia'}
)

Druid = ClassType(
    "(Hib) Druid",
    skills={},
    magic_skills={'Regrowth Skill': 0,
                  'Nurture Skill': 0,
                  'Nature Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   Sylvan,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Reinforced',
                 'Scale'},
    realm={'Hibernia'}
)

Eldritch = ClassType(
    "(Hib) Eldritch",
    skills={},
    magic_skills={'Light Magic Skill': 0,
                  'Mana Magic Skill': 0,
                  'Void Magic Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Elf,
                   Lurikeen,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Hibernia'}
)

Enchanter = ClassType(
    "(Hib) Enchanter",
    skills={},
    magic_skills={'Light Magic Skill': 0,
                  'Mana Magic Skill': 0,
                  'Enchantments Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Elf,
                   Lurikeen,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Hibernia'}
)

Hero = ClassType(
    "(Hib) Hero",
    skills={'Shields Skill': 0,
            'Parry Skill': 0,},
    magic_skills={},
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0,
                  'Piercing Skill': 0,
                  'Celtic Spear Skill': 0,
                  'Large Weapons Skill': 0,
                  },
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   Lurikeen,
                   Sylvan,
                   Shar,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Reinforced',
                 'Scale'},
    realm={'Hibernia'}
)

Mauler_Hib = ClassType(
    "(Hib) Mauler",
    skills={},
    magic_skills={},
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={},
    armor_types={},
    realm={'Hibernia'}
)

Mentalist = ClassType(
    "(Hib) Mentalist",
    skills={},
    magic_skills={'Light Magic Skill': 0,
                  'Mana Magic Skill': 0,
                  'Mentalism Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   Shar,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Hibernia'}
)

Nightshade = ClassType(
    "(Hib) Nightshade",
    skills={'Stealth Skill': 0,
            'Envenom Skill': 0,
            'Critical Strike Skill': 0},
    magic_skills={},
    melee_skills={'Blades Skill': 0,
                  'Piercing Skill': 0,},
    dual_wield_skills={'Celtic Dual Skill': 0},
    archery_skills={},
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather'},
    realm={'Hibernia'}
)

Ranger = ClassType(
    "(Hib) Ranger",
    skills={'Stealth Skill': 0},
    magic_skills={},
    melee_skills={'Blades Skill': 0,
                  'Piercing Skill': 0},
    dual_wield_skills={'Celtic Dual Skill': 0},
    archery_skills={'Archery Skill': 0},
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   Sylvan,
                   Shar,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Reinforced'},
    realm={'Hibernia'}
)

Valewalker = ClassType(
    "(Hib) Valewalker",
    skills={'Parry Skill': 0},
    magic_skills={'Arboreal Path Skill': 0},
    melee_skills={'Scythe Skill': 0},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   Sylvan,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Hibernia'}
)

Vampiir = ClassType(
    "(Hib) Vampiir",
    skills={},
    magic_skills={},
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={},
    armor_types={},
    realm={'Hibernia'}
)

Warden = ClassType(
    "(Hib) Warden",
    skills={'Shields Skill': 0,
            'Parry Skill': 0,},
    magic_skills={'Nurture Skill': 0,
                  'Regrowth Skill': 0
                  },
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   Elf,
                   Lurikeen,
                   Sylvan,
                   Shar,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Reinforced',
                 'Scale'},
    realm={'Hibernia'}
)

##################################
#       Hibernian Classes
##################################

Berserker = ClassType(
    "(Mid) Berserker",
    skills={'Parry Skill': 0},
    magic_skills={},
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0},
    dual_wield_skills={'Left Axe Skill': 0},
    archery_skills={},
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Kobold,
                   Valkyn,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded'},
    realm={'Midgard'}
)

Bonedancer = ClassType(
    "(Mid) Bonedancer",
    skills={},
    magic_skills={'Darkness Skill': 0,
                  'Suppression Skill': 0,
                  'Bone Army Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Troll,
                   Kobold,
                   Valkyn,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Midgard'}
)

Healer = ClassType(
    "(Mid) Healer",
    skills={},
    magic_skills={'Mending Skill': 0,
                  'Augmentation Skill': 0,
                  'Pacification Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Norseman, 
                   Dwarf,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Midgard'}
)

Hunter = ClassType(
    "(Mid) Hunter",
    skills={'Stealth Skill': 0},
    magic_skills={'Beastcraft Skill': 0},
    melee_skills={'Sword Skill': 0,
                  'Spear Skill': 0
                  },
    dual_wield_skills={},
    archery_skills={'Archery Skill': 0},
    allowed_races={Norseman, 
                   Dwarf,
                   Kobold,
                   Valkyn,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded'},
    realm={'Midgard'}
)

Mauler_Mid = ClassType(
    "(Mid) Mauler",
    skills={},
    magic_skills={},
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={},
    armor_types={},
    realm={'Midgard'}
)

Runemaster = ClassType(
    "(Mid) Runemaster",
    skills={},
    magic_skills={'Darkness Skill': 0,
                  'Suppression Skill': 0,
                  'Runecarving Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Norseman, 
                   Dwarf,
                   Kobold,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Midgard'}
)

Savage = ClassType(
    "(Mid) Savage",
    skills={'Parry Skill': 0},
    magic_skills={'Savagery Skill': 0,
                  },
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0},
    dual_wield_skills={'Hand to Hand Skill': 0},
    archery_skills={},
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Kobold,
                   Valkyn,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded'},
    realm={'Midgard'}
)

Shadowblade = ClassType(
    "(Mid) Shadowblade",
    skills={'Stealth Skill': 0,
            'Envenom Skill': 0,
            'Critical Strike Skill': 0},
    magic_skills={},
    melee_skills={'Sword Skill': 0,
                  'Axe Skill': 0},
    dual_wield_skills={'Left Axe Skill': 0},
    archery_skills={},
    allowed_races={Norseman, 
                   Dwarf,
                   Kobold,
                   Valkyn,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather'},
    realm={'Midgard'}
)

Shaman = ClassType(
    "(Mid) Shaman",
    skills={},
    magic_skills={'Mending Skill': 0,
                  'Augmentation Skill': 0,
                  'Subterranean Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Troll,
                   Dwarf,
                   Kobold,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Midgard'}
)

Skald = ClassType(
    "(Mid) Skald",
    skills={'Parry Skill': 0},
    magic_skills={'Battlesongs Skill': 0,
                  },
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Kobold,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Midgard'}
)

Spiritmaster = ClassType(
    "(Mid) Spiritmaster",
    skills={},
    magic_skills={'Darkness Skill': 0,
                  'Suppression Skill': 0,
                  'Summoning Skill': 0,
                  },
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Norseman, 
                   Kobold,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth'},
    realm={'Midgard'}
)

Thane = ClassType(
    "(Mid) Thane",
    skills={'Shields Skill': 0,
            'Parry Skill': 0},
    magic_skills={'Stormcalling Skill': 0,
                  },
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Valkyn,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Midgard'}
)

Valkyrie = ClassType(
    "(Mid) Valkyrie",
    skills={'Shields Skill': 0,
            'Parry Skill': 0},
    magic_skills={'Mending Skill': 0,
                  'Odins Will Skill': 0
                  },
    melee_skills={'Sword Skill': 0,
                  'Spear Skill': 0},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Norseman, 
                   Dwarf,
                   Valkyn,
                   Frostalf,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Midgard'}
)

Warlock = ClassType(
    "(Mid) Warlock",
    skills={},
    magic_skills={},
    melee_skills={},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={},
    armor_types={},
    realm={'Midgard'}
)

Warrior = ClassType(
    "(Mid) Warrior",
    skills={'Shields Skill': 0,
            'Parry Skill': 0,
            'Thrown Weapons Skill': 0},
    magic_skills={},
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0},
    dual_wield_skills={},
    archery_skills={},
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Kobold,
                   Valkyn,
                   NoRace
                   },
    armor_types={'Cloth',
                 'Leather',
                 'Studded',
                 'Chain'},
    realm={'Midgard'}
)