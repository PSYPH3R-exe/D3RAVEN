# loot/filters.py

def should_auto_salvage(item):
    return item.rarity in ("COMMON", "MAGIC", "RARE")
