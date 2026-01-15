# loot/build_guard.py

def is_build_required(item, build):
    for names in build["required_items"].values():
        if item.name in names:
            return True
    return False

def slot_missing_priority(item, build):
    required_stats = build["slot_priorities"].get(item.slot, [])
    return not all(stat in item.stats for stat in required_stats)
