# Decision cache (item hash → action)

class LootCache:
    def __init__(self):
        self.cache = {}

    def get(self, item_hash):
        return self.cache.get(item_hash)

    def set(self, item_hash, action):
        self.cache[item_hash] = action
