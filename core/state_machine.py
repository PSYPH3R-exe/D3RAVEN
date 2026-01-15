# Authoritative state controller


# State base class
class State:
    def tick(self, context):
        pass

# State implementations
class InTown(State):
    def tick(self, context):
        # TODO: Implement in-town logic
        print("Tick: IN_TOWN")

class EnterRift(State):
    def tick(self, context):
        # TODO: Implement rift entry logic
        print("Tick: ENTER_RIFT")

class Combat(State):
    def tick(self, context):
        # TODO: Implement combat logic
        print("Tick: COMBAT")

class LootScan(State):
    def tick(self, context):
        # TODO: Implement loot scan logic
        print("Tick: LOOT_SCAN")

class Inventory(State):
    def tick(self, context):
        # TODO: Implement inventory logic
        print("Tick: INVENTORY")

class Recovery(State):
    def tick(self, context):
        # TODO: Implement recovery logic
        print("Tick: RECOVERY")

class StateMachine:
    def __init__(self):
        self.state_map = {
            'IN_TOWN': InTown(),
            'ENTER_RIFT': EnterRift(),
            'COMBAT': Combat(),
            'LOOT_SCAN': LootScan(),
            'INVENTORY': Inventory(),
            'RECOVERY': Recovery(),
        }
        self.current_state_name = 'IN_TOWN'

    def current(self):
        return self.state_map[self.current_state_name]

    def transition(self, new_state):
        if new_state in self.state_map:
            self.current_state_name = new_state
