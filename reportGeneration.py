from Models.item import Item

def formatItemReportForInformationBox(item: Item):
    lines = []

    lines.append(f"{item.name}")
    lines.append("")
    lines.append(f"Item Slot : {item.slot}")
    lines.append(f"Item Type : {item.item_type}")
    lines.append(f"Item Level : {item.level}")
    lines.append(f"Tradeable : {item.tradeable}")
    lines.append(f"Quality : {item.quality}")
    if item.armor_factor:
        lines.append(f"Armor Factor : {item.armor_factor}")
    lines.append(f"Realm : {item.realm}")
    lines.append(f"Usable By : {item.usable}")

    if item.damage_type:
        lines.append(f"Damage Type : {item.damage_type}")
    if item.shield_size:
        lines.append(f"Shield Size : {item.shield_size}")
    if item.dps:
        lines.append(f"DPS : {item.dps}")
    if item.speed:
        lines.append(f"Speed : {item.speed}")
    lines.append("")
    for stat, value in item.stats.items():
        lines.append(f"{value} {stat.replace('_', ' ').title()}")
    
    lines.append("")
    lines.append(f"Single Utility : {item.single_utility}")
    lines.append(f"Total Utility : {item.total_utility}")
    lines.append("")
    lines.append(f"Bonus Level : {item.bonus_level}")

    return "\n".join(lines)