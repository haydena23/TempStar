from Models.classes import *

class Item:
    def __init__(self, slot, name, stats, single_utility, total_utility, 
                 level, bonus_level, realm, armor_factor, usable,
                 tradeable, item_type, quality, dps, speed, damage_type,
                 ):
        self.slot = slot
        self.name = name
        self.stats = stats
        self.single_utility = single_utility
        self.total_utility = total_utility
        self.level = level
        self.bonus_level = bonus_level
        self.realm = realm
        self.armor_factor = armor_factor
        self.usable = usable
        self.tradeable = tradeable
        self.itemType = item_type
        self.quality = quality
        self.dps = dps
        self.speed = speed
        self.damage_type = damage_type

belt = Item(
    "Belt",
    "Shimmering Satin Sash",
    stats={'strength_cap': 15,
        'strength': 92,
        'constitution_cap': 13,
        'constitution': 90,
        'dexterity': 75,
        'quickness_cap': 13,
        'quickness': 88,
        'heat_resist': 26,
        'color_resist': 24,
        'crush_resist': 29,
        'crush_skill': 12,
        'parry_skill': 11,
        'shields_skill': 11,
        'polearm_skill': 11,
        'crush_resist': 26,},
    single_utility=None,
    total_utility=None,
    level=None,
    bonus_level=None,
    realm=None,
    armor_factor=None,
    usable=None,
    tradeable=None,
    item_type=None,
    quality=None,
    dps=None,
    speed=None,
    damage_type=None
)

belt2 = Item(
    "Belt",
    "Apostle of Arawn Belt",
    stats={'quickness': 75,
        'strength': 75,
        'constitution': 75,
        'dexterity': 75,},
    single_utility=None,
    total_utility=None,
    level=None,
    bonus_level=None,
    realm=None,
    armor_factor=None,
    usable=None,
    tradeable=None,
    item_type=None,
    quality=None,
    dps=None,
    speed=None,
    damage_type=None
)

cloak = Item(
    "Cloak",
    "Dragonsworn Cloak",
    stats={'crush_resist': 26,
        'slash_resist': 26,
        'thrust_resist': 26},
    single_utility=None,
    total_utility=None,
    level=None,
    bonus_level=None,
    realm=None,
    armor_factor=None,
    usable=None,
    tradeable=None,
    item_type=None,
    quality=None,
    dps=None,
    speed=None,
    damage_type=None
)

sword1 = Item(
    "Right Hand",
    "Right Hand Sword",
    stats={'crush_resist': 26},
    single_utility=None,
    total_utility=None,
    level=None,
    bonus_level=None,
    realm=None,
    armor_factor=None,
    usable=None,
    tradeable=None,
    item_type=None,
    quality=None,
    dps=None,
    speed=None,
    damage_type=None
)

sword2 = Item(
    "Left Hand",
    "Left Hand Sword",
    stats={'slash_resist': 26},
    single_utility=None,
    total_utility=None,
    level=None,
    bonus_level=None,
    realm=None,
    armor_factor=None,
    usable=None,
    tradeable=None,
    item_type=None,
    quality=None,
    dps=None,
    speed=None,
    damage_type=None
)

claymore = Item(
    "Two Hand",
    "Two Hand Sword",
    stats={'strength': 75},
    single_utility=None,
    total_utility=None,
    level=None,
    bonus_level=None,
    realm=None,
    armor_factor=None,
    usable=None,
    tradeable=None,
    item_type=None,
    quality=None,
    dps=None,
    speed=None,
    damage_type=None
)

bow = Item(
    "Ranged",
    "Bow",
    stats={'dexterity': 75},
    single_utility=None,
    total_utility=None,
    level=None,
    bonus_level=None,
    realm=None,
    armor_factor=None,
    usable=None,
    tradeable=None,
    item_type=None,
    quality=None,
    dps=None,
    speed=None,
    damage_type=None
)

gear = [belt, belt2]