class RaceType:
    def __init__(self, name, resists):
        self.name = name
        self.resists = resists

Briton = RaceType(
    "Briton",
    resists={'crush_resist': 2,
             'slash_resist': 3,
             'spirit_resist': 5}
)