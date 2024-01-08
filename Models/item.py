class Item:
    def __init__(self, slot, shield_size, name, stats, single_utility, total_utility, 
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
        self.item_type = item_type
        self.quality = quality
        self.dps = dps
        self.speed = speed
        self.damage_type = damage_type
        self.shield_size = shield_size