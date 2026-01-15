# Weighted stat scoring

def score_item(item):
    def score_item(item, weights, slot_priorities):
        score = 0.0
        for stat, value in item.stats.items():
            score += value * weights.get(stat, 0)
        if getattr(item, 'ancient', False):
            score *= 1.25
        if getattr(item, 'primal', False):
            score *= 1.5
        required = slot_priorities.get(item.slot, [])
        if not all(stat in item.stats for stat in required):
            score *= 0.6
        return score
