class ClassType:
    def __init__(self, name, magic_skills, melee_skills):
        self.name = name
        self.magic_skills = magic_skills
        self.melee_skills = melee_skills        

"""
Albion Classes
"""
Armsman = ClassType(
    "(Alb) Armsman",
    magic_skills={},
    melee_skills={'Crush Skill': 0, 
                  'Slash Skill': 0,
                  'Thrust Skill': 0,
                  'Polearm Skill': 0,
                  'Two Handed Skill': 0,
                  'Shields Skill': 0,
                  }
)

Cabalist = ClassType(
    "(Alb) Cabalist",
    magic_skills={'Matter Magic Skill': 0,
                  'Body Magic Skill': 0,
                  'Spirit Magic Skill': 0
                  },
    melee_skills={}
)

Cleric = ClassType(
    "(Alb) Cleric",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0,
                  'Smite Skill': 0,
                  },
    melee_skills={}
)

Friar = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
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
                  }
)

Mauler_Alb = ClassType(
    "(Alb) Mauler",
    magic_skills={},
    melee_skills={}
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
                  }
)

Minstrel = ClassType(
    "(Alb) Minstrel",
    magic_skills={'Instruments Skill': 0,
                  'Stealth Skill': 0
                  },
    melee_skills={'Slash Skill': 0,
                  'Thrust Skill': 0
                  }
)

Necromancer = ClassType(
    "(Alb) Necromancer",
    magic_skills={'Deathsight Skill': 0,
                  'Painworking Skill': 0,
                  'Death Servant Skill': 0
                  },
    melee_skills={}
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
                  }
)

Sorcerer = ClassType(
    "(Alb) Sorcerer",
    magic_skills={'Matter Magic Skill': 0,
                  'Body Magic Skill': 0,
                  'Mind Magic Skill': 0,
                  },
    melee_skills={}
)

Theurgist = ClassType(
    "(Alb) Theurgist",
    magic_skills={'Earth Magic Skill': 0,
                  'Cold Magic Skill': 0,
                  'Wind Magic Skill': 0,
                  },
    melee_skills={}
)

Wizard = ClassType(
    "(Alb) Wizard",
    magic_skills={'Earth Magic Skill': 0,
                  'Cold Magic Skill': 0,
                  'Fire Magic Skill': 0,
                  },
    melee_skills={}
)

"""
Hibernian Classes
"""

Animist = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Bainshee = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Bard = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Blademaster = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Champion = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Druid = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Eldritch = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Enchanter = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Hero = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Mauler_Hib = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Mentalist = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Nightshade = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Ranger = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Valewalker = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Vampiir = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Warden = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

"""
Midgard Classes
"""

Berserker = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Bonedancer = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Healer = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Hunter = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Mauler_Mid = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Runemaster = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Savage = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Shadowblade = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Shaman = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Skald = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Spiritmaster = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Thane = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Valkyrie = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Warlock = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)

Warrior = ClassType(
    "(Alb) Friar",
    magic_skills={'Rejuvenation Skill': 0,
                  'Enhancement Skill': 0
                  },
    melee_skills={'Staff Skill': 0,
                  'Parry Skill': 0
                  }
)