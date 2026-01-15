# Authoritative state controller

class StateMachine:
    def __init__(self):
        self.states = ['IN_TOWN', 'ENTER_RIFT', 'COMBAT', 'LOOT_SCAN', 'INVENTORY', 'RECOVERY']
        self.current_state = 'IN_TOWN'

    def current(self):
        return self.current_state

    def transition(self, new_state):
        if new_state in self.states:
            self.current_state = new_state
