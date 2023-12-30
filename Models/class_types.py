from Models.race_types import *

class ClassType:
    def __init__(self, name, magic_skills, melee_skills, allowed_races: RaceType):
        self.name = name
        self.magic_skills = magic_skills
        self.melee_skills = melee_skills 
        self.allowed_races = allowed_races

##################################
#       Hibernian Classes
##################################

Armsman = ClassType(
    "(Alb) Armsman",
    magic_skills={},
    melee_skills={'Crush Skill': 0, 
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Polearm Skill': 0,
                  'Two Handed Skill': 0,
                  'Shields Skill': 0,
                  },
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   Highlander,
                   Inconnu,
                   Saracen,
                   NoRace
                   }
)

Cabalist = ClassType(
    "(Alb) Cabalist",
    magic_skills={'Matter Magic Skill': 0,
                  'Body Magic Skill': 0,
                  'Spirit Magic Skill': 0
                  },
    melee_skills={},
    allowed_races={Briton, 
                   Avalonian,
                   Saracen,
                   Inconnu,
                   HalfOgre,
                   NoRace
                   }
)

Cleric = ClassType(
    "(Alb) Cleric",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0,
                  'Smite Skill': 0,
                  },
    melee_skills={},
    allowed_races={Briton, 
                   Avalonian,
                   Highlander,
                   NoRace
                   }
)

Friar = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  },
    allowed_races={Briton, 
                   Avalonian,
                   Highlander,
                   NoRace
                   }
)

Heretic = ClassType(
    "(Alb) Heretic",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Crush Skill': 0,
                  'Flexible Skill': 0,
                  'Shields Skill': 0,
                  },
    allowed_races={Briton, 
                   Avalonian,
                   Highlander,
                   Saracen,
                   Inconnu,
                   NoRace
                   }
)

Infiltrator = ClassType(
    "(Alb) Infiltrator",
    magic_skills={'Stealth Skill': 0,
                  'Envenom Skill': 0
                  },
    melee_skills={'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Critical Strike Skill': 0,
                  'Dual Wield Skill': 0,
                  },
    allowed_races={Briton, 
                   Highlander,
                   Saracen,
                   Inconnu,
                   NoRace
                   }
)

Mauler_Alb = ClassType(
    "(Alb) Mauler",
    magic_skills={},
    melee_skills={},
    allowed_races={}
)

Mercenary = ClassType(
    "(Alb) Mercenary",
    magic_skills={},
    melee_skills={'Crush Skill': 0,
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Dual Wield Skill': 0,
                  'Shields Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   Highlander,
                   Inconnu,
                   Saracen,
                   NoRace
                   }
)

Minstrel = ClassType(
    "(Alb) Minstrel",
    magic_skills={'Instruments Skill': 0,
                  'Stealth Skill': 0
                  },
    melee_skills={'Slash Skill': 0,
                  'Thrust Skill': 0
                  },
    allowed_races={Briton,
                   Highlander,
                   Inconnu,
                   Saracen,
                   NoRace
                   }
)

Necromancer = ClassType(
    "(Alb) Necromancer",
    magic_skills={'Deathsight Skill': 0,
                  'Painworking Skill': 0,
                  'Death Servant Skill': 0
                  },
    melee_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   Inconnu,
                   Saracen,
                   NoRace
                   }
)

Paladin = ClassType(
    "(Alb) Paladin",
    magic_skills={'Chants Skill': 0,
                  },
    melee_skills={'Crush Skill': 0,
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Two Handed Skill': 0,
                  'Shields Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Avalonian, 
                   Briton,
                   Highlander,
                   Saracen,
                   NoRace
                   }
)

Reaver = ClassType(
    "(Alb) Reaver",
    magic_skills={'Soulrending Skill': 0,
                  },
    melee_skills={'Crush Skill': 0,
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Flexible Skill': 0,
                  'Shield Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Briton,
                   Inconnu,
                   Saracen,
                   NoRace
                   }
)

Scout = ClassType(
    "(Alb) Scout",
    magic_skills={'Stealth Skill': 0,
                  'Archery Skill': 0,
                  },
    melee_skills={'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Shields Skill': 0,
                  },
    allowed_races={Briton,
                   Highlander,
                   Inconnu,
                   Saracen,
                   NoRace
                   }
)

Sorcerer = ClassType(
    "(Alb) Sorcerer",
    magic_skills={'Matter Magic Skill': 0,
                  'Body Magic Skill': 0,
                  'Mind Magic Skill': 0,
                  },
    melee_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   Inconnu,
                   Saracen,
                   NoRace
                   }
)

Theurgist = ClassType(
    "(Alb) Theurgist",
    magic_skills={'Earth Magic Skill': 0,
                  'Cold Magic Skill': 0,
                  'Wind Magic Skill': 0,
                  },
    melee_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   NoRace
                   }
)

Wizard = ClassType(
    "(Alb) Wizard",
    magic_skills={'Earth Magic Skill': 0,
                  'Cold Magic Skill': 0,
                  'Fire Magic Skill': 0,
                  },
    melee_skills={},
    allowed_races={Avalonian, 
                   Briton,
                   HalfOgre,
                   Inconnu,
                   NoRace
                   }
)

##################################
#       Hibernian Classes
##################################

Animist = ClassType(
    "(Hib) Animist",
    magic_skills={'Arboreal Path Skill': 0,
                  'Creeping Path Skill': 0,
                  'Verdant Path Skill': 0
                  },
    melee_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   Elf,
                   Sylvan,
                   NoRace
                   }
)

Bainshee = ClassType(
    "(Hib) Bainshee",
    magic_skills={'Spectral Guard Skill': 0,
                  'Phantasmal Wail Skill': 0,
                  'Ethereal Shriek Skill': 0,
                  },
    melee_skills={},
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   NoRace
                   }
)

Bard = ClassType(
    "(Hib) Bard",
    magic_skills={'Regrowth Skill': 0,
                  'Nurture Skill': 0,
                  'Music Skill': 0,
                  },
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0
                  },
    allowed_races={Celt, 
                   Firbolg,
                   NoRace
                   }
)

Blademaster = ClassType(
    "(Hib) Blademaster",
    magic_skills={},
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0,
                  'Piercing Skill': 0,
                  'Celtic Dual Skill': 0,
                  'Shields Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Celt, 
                   Firbolg,
                   Elf,
                   Lurikeen,
                   Shar,
                   NoRace
                   }
)

Champion = ClassType(
    "(Hib) Champion",
    magic_skills={'Valor Skill': 0,
                  },
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0,
                  'Piercing Skill': 0,
                  'Large Weapons Skill': 0,
                  'Shields Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   Sylvan,
                   Shar,
                   NoRace
                   }
)

Druid = ClassType(
    "(Hib) Druid",
    magic_skills={'Regrowth Skill': 0,
                  'Nurture Skill': 0,
                  'Nature Skill': 0,
                  },
    melee_skills={},
    allowed_races={Celt, 
                   Firbolg,
                   Sylvan,
                   NoRace
                   }
)

Eldritch = ClassType(
    "(Hib) Eldritch",
    magic_skills={'Light Magic Skill': 0,
                  'Mana Magic Skill': 0,
                  'Void Magic Skill': 0,
                  },
    melee_skills={},
    allowed_races={Elf,
                   Lurikeen,
                   NoRace
                   }
)

Enchanter = ClassType(
    "(Hib) Enchanter",
    magic_skills={'Light Magic Skill': 0,
                  'Mana Magic Skill': 0,
                  'Enchantments Skill': 0,
                  },
    melee_skills={},
    allowed_races={Elf,
                   Lurikeen,
                   NoRace
                   }
)

Hero = ClassType(
    "(Hib) Hero",
    magic_skills={},
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0,
                  'Piercing Skill': 0,
                  'Celtic Spear Skill': 0,
                  'Large Weapons Skill': 0,
                  'Shields Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Celt, 
                   Firbolg,
                   Lurikeen,
                   Sylvan,
                   Shar,
                   NoRace
                   }
)

Mauler_Hib = ClassType(
    "(Hib) Mauler",
    magic_skills={},
    melee_skills={},
    allowed_races={}
)

Mentalist = ClassType(
    "(Hib) Mentalist",
    magic_skills={'Light Magic Skill': 0,
                  'Mana Magic Skill': 0,
                  'Mentalism Skill': 0,
                  },
    melee_skills={},
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   Shar,
                   NoRace
                   }
)

Nightshade = ClassType(
    "(Hib) Nightshade",
    magic_skills={'Stealth Skill': 0,
                  'Envenom Skill': 0
                  },
    melee_skills={'Blades Skill': 0,
                  'Piercing Skill': 0,
                  'Celtic Dual Skill': 0,
                  'Critical Strike Skill': 0,
                  },
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   NoRace
                   }
)

Ranger = ClassType(
    "(Hib) Ranger",
    magic_skills={'Stealth Skill': 0,
                  'Archery Skill': 0
                  },
    melee_skills={'Blades Skill': 0,
                  'Piercing Skill': 0,
                  'Celtic Dual Skill': 0,
                  },
    allowed_races={Celt, 
                   Elf,
                   Lurikeen,
                   Sylvan,
                   Shar,
                   NoRace
                   }
)

Valewalker = ClassType(
    "(Hib) Valewalker",
    magic_skills={'Arboreal Path Skill': 0,
                  },
    melee_skills={'Scythe Skill': 0,
                  'Parry Skill': 0
                  },
    allowed_races={Celt, 
                   Firbolg,
                   Sylvan,
                   NoRace
                   }
)

Vampiir = ClassType(
    "(Hib) Vampiir",
    magic_skills={},
    melee_skills={},
    allowed_races={}
)

Warden = ClassType(
    "(Hib) Friar",
    magic_skills={'Nurture Skill': 0,
                  'Regrowth Skill': 0
                  },
    melee_skills={'Blades Skill': 0,
                  'Blunt Skill': 0,
                  'Shields Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Celt, 
                   Firbolg,
                   Elf,
                   Lurikeen,
                   Sylvan,
                   Shar,
                   NoRace
                   }
)

##################################
#       Hibernian Classes
##################################

Berserker = ClassType(
    "(Mid) Berserker",
    magic_skills={},
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0,
                  'Left Axe Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Kobold,
                   Valkyn,
                   NoRace
                   }
)

Bonedancer = ClassType(
    "(Mid) Bonedancer",
    magic_skills={'Darkness Skill': 0,
                  'Suppression Skill': 0,
                  'Bone Army Skill': 0,
                  },
    melee_skills={},
    allowed_races={Troll,
                   Kobold,
                   Valkyn,
                   Frostalf,
                   NoRace
                   }
)

Healer = ClassType(
    "(Mid) Healer",
    magic_skills={'Mending Skill': 0,
                  'Augmentation Skill': 0,
                  'Pacification Skill': 0,
                  },
    melee_skills={},
    allowed_races={Norseman, 
                   Dwarf,
                   Frostalf,
                   NoRace
                   }
)

Hunter = ClassType(
    "(Mid) Hunter",
    magic_skills={'Stealth Skill': 0,
                  'Archery Skill': 0,
                  'Beastcraft Skill': 0,
                  },
    melee_skills={'Sword Skill': 0,
                  'Spear Skill': 0
                  },
    allowed_races={Norseman, 
                   Dwarf,
                   Kobold,
                   Valkyn,
                   Frostalf,
                   NoRace
                   }
)

Mauler_Mid = ClassType(
    "(Mid) Mauler",
    magic_skills={},
    melee_skills={},
    allowed_races={}
)

Runemaster = ClassType(
    "(Mid) Runemaster",
    magic_skills={'Darkness Skill': 0,
                  'Suppression Skill': 0,
                  'Runecarving Skill': 0,
                  },
    melee_skills={},
    allowed_races={Norseman, 
                   Dwarf,
                   Kobold,
                   Frostalf,
                   NoRace
                   }
)

Savage = ClassType(
    "(Mid) Savage",
    magic_skills={'Savagery Skill': 0,
                  },
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0,
                  'Hand to Hand Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Kobold,
                   Valkyn,
                   NoRace
                   }
)

Shadowblade = ClassType(
    "(Mid) Shadowblade",
    magic_skills={'Stealth Skill': 0,
                  'Envenom Skill': 0
                  },
    melee_skills={'Sword Skill': 0,
                  'Axe Skill': 0,
                  'Critical Strike Skill': 0,
                  'Left Axe Skill': 0,
                  },
    allowed_races={Norseman, 
                   Dwarf,
                   Kobold,
                   Valkyn,
                   Frostalf,
                   NoRace
                   }
)

Shaman = ClassType(
    "(Mid) Shaman",
    magic_skills={'Mending Skill': 0,
                  'Augmentation Skill': 0,
                  'Subterranean Skill': 0,
                  },
    melee_skills={},
    allowed_races={Troll,
                   Dwarf,
                   Kobold,
                   Frostalf,
                   NoRace
                   }
)

Skald = ClassType(
    "(Mid) Skald",
    magic_skills={'Battlesongs Skill': 0,
                  },
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Kobold,
                   NoRace
                   }
)

Spiritmaster = ClassType(
    "(Mid) Spiritmaster",
    magic_skills={'Darkness Skill': 0,
                  'Suppression Skill': 0,
                  'Summoning Skill': 0,
                  },
    melee_skills={},
    allowed_races={Norseman, 
                   Kobold,
                   Frostalf,
                   NoRace
                   }
)

Thane = ClassType(
    "(Mid) Thane",
    magic_skills={'Stormcalling Skill': 0,
                  },
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0,
                  'Shields Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Valkyn,
                   Frostalf,
                   NoRace
                   }
)

Valkyrie = ClassType(
    "(Mid) Valkyrie",
    magic_skills={'Mending Skill': 0,
                  'Odins Will Skill': 0
                  },
    melee_skills={'Sword Skill': 0,
                  'Spear Skill': 0,
                  'Shields Skill': 0,
                  'Parry Skill': 0,
                  },
    allowed_races={Norseman, 
                   Dwarf,
                   Valkyn,
                   Frostalf,
                   NoRace
                   }
)

Warlock = ClassType(
    "(Mid) Warlock",
    magic_skills={},
    melee_skills={},
    allowed_races={}
)

Warrior = ClassType(
    "(Mid) Warrior",
    magic_skills={},
    melee_skills={'Axe Skill': 0,
                  'Hammer Skill': 0,
                  'Sword Skill': 0,
                  'Staff Skill': 0,
                  'Staff Skill': 0,
                  'Thrown Weapons Skill': 0,
                  },
    allowed_races={Norseman, 
                   Troll,
                   Dwarf,
                   Kobold,
                   Valkyn,
                   NoRace
                   }
)