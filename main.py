# Boot + main loop


from core.state_machine import StateMachine
from core.context import Context
from utils.watchdog import check as watchdog_check

def init():
    ctx = Context()
    sm = StateMachine()
    return ctx, sm


def update_context(context):
    # TODO: Fill in with perception and game state updates
    pass

def main():
    context, state_machine = init()
    running = True
    while running:
        update_context(context)
        state = state_machine.current()
        # Each state should have a tick(context) method or similar
        # For now, just print state for demonstration
        print(f"Current state: {state}")
        # TODO: Call state.tick(context) when implemented
        watchdog_check()

if __name__ == "__main__":
    main()
