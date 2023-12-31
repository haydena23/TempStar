class RaceType:
    def __init__(self, name, resists):
        self.name = name
        self.resists = resists

"""
Albion Races
"""
Avalonian = RaceType(
    "Avalonian",
    resists={'crush_resist': 2,
             'slash_resist': 3,
             'spirit_resist': 5}
)
Briton = RaceType(
    "Briton",
    resists={'crush_resist': 2,
             'slash_resist': 3,
             'spirit_resist': 5}
)
HalfOgre = RaceType(
    "Half-Ogre",
    resists={'slash_resist': 3,
             'thrust_resist': 2,
             'matter_resist': 5}
)
Highlander = RaceType(
    "Highlander",
    resists={'crush_resist': 2,
             'slash_resist': 3,
             'cold_resist': 5}
)
Inconnu = RaceType(
    "Inconnu",
    resists={'crush_resist': 2,
             'thrust_resist': 3,
             'heat_resist': 5,
             'spirit_resist': 3}
)
Saracen = RaceType(
    "Saracen",
    resists={'slash_resist': 2,
             'thrust_resist': 3,
             'heat_resist': 5}
)

"""
Hibernian Races
"""
Celt = RaceType(
    "Celt",
    resists={'crush_resist': 2,
             'slash_resist': 3,
             'spirit_resist': 5}
)
Elf = RaceType(
    "Elf",
    resists={'slash_resist': 2,
             'thrust_resist': 3,
             'spirit_resist': 5}
)
Firbolg = RaceType(
    "Firbolg",
    resists={'crush_resist': 3,
             'slash_resist': 2,
             'heat_resist': 5}
)
Lurikeen = RaceType(
    "Lurikeen",
    resists={'crush_resist': 5,
             'energy_resist': 5}
)
Shar = RaceType(
    "Shar",
    resists={'crush_resist': 5,
             'energy_resist': 5}
)
Sylvan = RaceType(
    "Sylvan",
    resists={'crush_resist': 3,
             'thrust_resist': 2,
             'matter_resist': 5,
             'energy_resist': 5}
)

"""
Midgard Races
"""
Dwarf = RaceType(
    "Dwarf",
    resists={'slash_resist': 2,
             'thrust_resist': 3,
             'body_resist': 5}
)
Frostalf = RaceType(
    "Frostalf",
    resists={'slash_resist': 2,
             'thrust_resist': 3,
             'spirit_resist': 5}
)
Kobold = RaceType(
    "Kobold",
    resists={'crush_resist': 5,
             'energy_resist': 5}
)
Norseman = RaceType(
    "Norseman",
    resists={'crush_resist': 2,
             'slash_resist': 3,
             'cold_resist': 5}
)
Troll = RaceType(
    "Troll",
    resists={'slash_resist': 3,
             'thrust_resist': 2,
             'matter_resist': 5}
)
Valkyn = RaceType(
    "Valkyn",
    resists={'slash_resist': 3,
             'thrust_resist': 2,
             'body_resist': 5}
)

"""
Universal Races
"""
Minotaur = RaceType(
    "Minotaur",
    resists={'crush_resist': 2,
             'heat_resist': 3,
             'cold_resist': 3}
)

NoRace = RaceType(
    "<None>",
    resists={}
)