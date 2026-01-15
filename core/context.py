# Shared runtime context (read-heavy)


from perception.screen import capture_screen
from perception.ui_hashes import validate_ui
from perception.detectors import detect_loot_glow

class Context:
    def __init__(self):
        self.dead = False
        self.in_town = True
        self.inventory_open = False
        self.loot_glow_detected = False
        self.screen = None
        self.ui_valid = False

    def update(self):
        # Capture the current screen
        self.screen = capture_screen()
        # Validate UI state
        self.ui_valid = validate_ui()
        # Detect loot glow
        self.loot_glow_detected = detect_loot_glow()
        # TODO: Add more perception and state updates as needed
