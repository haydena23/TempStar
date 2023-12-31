class Item:
    def __init__(self, slot, stats):
        self.slot = slot
        self.stats = stats
        
belt = Item(
    "Belt",
    stats={'strength': 5,
        'constitution': 5,
        'intelligence': 5,
        'acuity': 5}
)