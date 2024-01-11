class Item:
    def __init__(self, slot, shield_size, name, stats, single_utility, total_utility, 
                 level, bonus_level, realm, armor_factor, usable,
                 tradeable, item_type, quality, dps, speed, damage_type, crafted
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
        self.crafted = crafted
    
    def setSlot(self, slot):
        self.slot = slot
    def setName(self, name):
        self.name = name
    def setStats(self, stats):
        self.stats = stats
    def setSingleUtility(self, single_utility):
        self.single_utility = single_utility
    def setTotalUtility(self, total_utility):
        self.total_utility = total_utility
    def setLevel(self, level):
        self.level = level
    def setBonusLevel(self, bonus_level):
        self.bonus_level = bonus_level
    def setRealm(self, realm):
        self.realm = realm
    def setArmorFactor(self, armor_factor):
        self.armor_factor = armor_factor
    def setUsable(self, usable):
        self.usable = usable
    def setTradeable(self, tradeable):
        self.tradeable = tradeable
    def setItemType(self, item_type):
        self.item_type = item_type
    def setQuality(self, quality):
        self.quality = quality
    def setDps(self, dps):
        self.dps = dps
    def setSpeed(self, speed):
        self.speed = speed
    def setDamageType(self, damage_type):
        self.damage_type = damage_type
    def setShieldSize(self, shield_size):
        self.shield_size = shield_size
    def setCrafted(self, crafted):
        self.crafted = crafted