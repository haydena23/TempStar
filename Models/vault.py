import json
from Models.item import Item

def loadVault(self):
    with open('database.json') as f:
        data = json.load(f)
        for item_data in data["items"]:
            item = Item(**item_data)
            if item.slot == "Left Hand":
                self.character.addToVault('Left Hand', item)
                if item.item_type != "Shield":
                    self.character.addToVault('Right Hand', item)
            elif item.slot == "Ring":
                self.character.addToVault('Ring 1', item)
                self.character.addToVault('Ring 2', item)
            elif item.slot == "Wrist":
                self.character.addToVault('Wrist 1', item)
                self.character.addToVault('Wrist 2', item)
            else:
                self.character.addToVault(item.slot, item)