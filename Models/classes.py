from Models.races import *

class ClassType:
    def __init__(self, name, skills, magic_skills, melee_skills, dual_wield_skills,
                 archery_skills, allowed_races: RaceType, armor_types, realm,
                 weaponry, shield_types):
        self.name = name
        self.skills = skills
        self.magic_skills = magic_skills
        self.melee_skills = melee_skills
        self.dual_wield_skills = dual_wield_skills 
        self.archery_skills = archery_skills
        self.allowed_races = allowed_races
        self.armor_types = armor_types
        self.realm = realm
        self.weaponry = weaponry
        self.shield_types = shield_types

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
    realm='Albion',
    weaponry = {
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Two Handed',
        'Polearm',
        'Crossbow',
        'Shield'
    },
    shield_types = {
        'Small',
        'Medium',
        'Large'
    }
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shield'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shield'},
    shield_types={'Small',
                  'Medium'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shield'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Flexible',
        'Shield'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Crossbow',
        'Shield'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={},
    shield_types={}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shortbow',
        'Shield'},
    shield_types={'Small',
                  'Medium'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Instrument',
        'Shield'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shield'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Two Hand',
        'Shield'},
    shield_types={'Small',
                  'Medium',
                  'Large'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Flexible',
        'Shield'},
    shield_types={'Small',
                  'Medium',
                  'Large'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shield',
        'Longbow'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shield'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shield'},
    shield_types={'Small'}
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
    realm='Albion',
    weaponry={
        'Staff',
        'Slashing',
        'Thrust',
        'Crushing',
        'Shield'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield',
              'Instrument'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield',
              'Shortbow'},
    shield_types={'Small',
                  'Medium'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield',
              'Large Weapons'},
    shield_types={'Small',
                  'Medium',
                  'Large'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield',
              'Large Weapons',
              'Celtic Spear',
              'Shortbow'},
    shield_types={'Small',
                  'Medium',
                  'Large'}
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
    realm='Hibernia',
    weaponry={},
    shield_types={}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield',
              'Recursive Bow'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield',
              'Scythe'},
    shield_types={'Small'}
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
    realm='Hibernia',
    weaponry={},
    shield_types={}
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
    realm='Hibernia',
    weaponry={'Staff',
              'Blade',
              'Blunt',
              'Piercing',
              'Shield',
              'Shortbow'},
    shield_types={'Small',
                  'Medium',
                  'Large'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield',
              'Thrown',
              'Two Handed'},
    shield_types={'Small'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield'},
    shield_types={'Small'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield'},
    shield_types={'Small'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield',
              'Spear',
              'Composite Bow',
              'Two Handed'},
    shield_types={'Small'}
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
    realm='Midgard',
    weaponry={},
    shield_types={}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield'},
    shield_types={'Small'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield',
              'Hand to Hand',
              'Two Handed'},
    shield_types={'Small'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield',
              'Thrown',
              'Two Handed'},
    shield_types={}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield'},
    shield_types={'Small'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield',
              'Two Handed'},
    shield_types={'Small',
                  'Medium'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield'},
    shield_types={'Small'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield',
              'Two Handed'},
    shield_types={'Small',
                  'Medium',
                  'Large'}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield',
              'Spear',
              'Two Handed'},
    shield_types={'Small',
                  'Medium',
                  'Large'}
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
    realm='Midgard',
    weaponry={},
    shield_types={}
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
    realm='Midgard',
    weaponry={'Staff',
              'Sword',
              'Axe',
              'Hammer',
              'Shield',
              'Two Handed',
              'Thrown'},
    shield_types={'Small',
                  'Medium',
                  'Large'}
)