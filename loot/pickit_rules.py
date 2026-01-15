# Tier 1 + Tier 2 logic ONLY


from loot.filters import should_auto_salvage
from loot.build_guard import is_build_required
from loot.scorer import score_item

def should_equip(new_item, equipped_item, ctx):
    if not equipped_item:
        return True
    new_score = score_item(new_item, ctx.weights, ctx.build["slot_priorities"])
    old_score = score_item(equipped_item, ctx.weights, ctx.build["slot_priorities"])
    return new_score > old_score * 1.05

def handle_legendary(item, ctx):
    if getattr(item, 'primal', False):
        ctx.stash(item)
        return
    equipped = ctx.get_equipped(item.slot)
    if should_equip(item, equipped, ctx):
        ctx.equip(item)
    else:
        ctx.salvage(item)

def apply_pickit_rules(ctx):
    for item in ctx.visible_items:
        if should_auto_salvage(item):
            ctx.salvage(item)
            continue
        if getattr(item, 'primal', False):
            ctx.stash(item)
            continue
        if getattr(item, 'is_equipped', False) or is_build_required(item, ctx.build):
            ctx.keep(item)
            continue
        handle_legendary(item, ctx)
