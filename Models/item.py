class Item:
    def __init__(self, slot, stats):
        self.slot = slot
        self.stats = stats
        
belt = Item(
    "Belt",
    stats={'strength': 5,
        'constitution': 5,
        'intelligence': 5,
        'piety': 75,
        'acuity': 5,
        'dexterity_cap': 30,
        'heat_resist': 27,
        'power_cap': 99,
        'hit_points_cap': 250,
        'crush_skill': 15,
        'parry_skill': 10,
        'crush_resist': 26,
        'matter_magic_skill': 10}
)

cloak = Item(
    "Cloak",
    stats={'strength': 5,
        'essence_resist': 26,
        'shields_skill': 15,
        'piety': 10}
)