# Shared runtime context (read-heavy)

class Context:
    def __init__(self):
        self.dead = False
        self.in_town = True
        self.inventory_open = False
        self.loot_glow_detected = False
