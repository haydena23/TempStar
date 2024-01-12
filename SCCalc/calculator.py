from PyQt5.QtWidgets import QComboBox

from Models.item import Item
from changeFunctions import autoUpdateRealmRank
from SCCalc.sc_maps import imbue_cost_for_stats

def onNewItemCreated(self, name):
    slot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    level = int(self.findChild(QComboBox, 'scArmorLevelCombo').currentText())
    itemType = self.findChild(QComboBox, 'scArmorTypeCombo').currentText()
    newSCItem = Item(
        slot, # Slot
        "", # Shield Size
        name, # Name
        {}, # Stats
        0, # Single Utility
        0, # Total Utility
        level, # Level
        1, # Bonus level
        self.character.class_type.realm, # Realm
        0, # Armor Factor
        "All", # Usable
        "Yes", # Tradeable
        itemType, # Item Type
        "99%", # Quality
        0, # DPS
        0, # Speed
        "", # Damage Type
        "Yes" # Crafted
    )
    self.character.addToVault(slot, newSCItem)
    self.character.addToAllItems(slot, newSCItem)
    self.character.setCurrentItem(slot, newSCItem)
    self.character.setTempItem(slot, newSCItem)
    autoUpdateRealmRank(self)
    
def calculateTotalImbueCost(self):
    pairs = [
        (self.statCategory1, self.statCombo1, self.statValue1),
        (self.statCategory2, self.statCombo2, self.statValue2),
        (self.statCategory3, self.statCombo3, self.statValue3),
        (self.statCategory4, self.statCombo4, self.statValue4)
    ]

    stat_costs = {}
    combo_contributions = {}
    try:
        for i, (stat_category, stat_combo, cost_combo) in enumerate(pairs, start=1):
            category = stat_category.currentText()
            stat = stat_combo.currentText()
            cost = imbue_cost_for_stats[category][cost_combo.currentIndex()]

            if stat == '<Empty>':
                combo_contributions[f'comboBox{i}'] = 0
                continue

            if stat not in stat_costs or stat_costs[stat] < cost:
                stat_costs[stat] = cost
                combo_contributions[f'comboBox{i}'] = cost

        total_cost = 0
        max_cost = max(stat_costs.values()) if stat_costs else 0
        max_cost_contributed = False

        for combo, cost in combo_contributions.items():
            if cost == max_cost and not max_cost_contributed:
                total_cost += cost
                combo_contributions[combo] = cost
                max_cost_contributed = True
            else:
                half_cost = cost / 2
                total_cost += half_cost
                combo_contributions[combo] = half_cost

        result = {'totalCost': total_cost}
        result.update(combo_contributions)

    except Exception as e:
        print(f"Error in calculateTotalImbueCost: {e}")

    return result