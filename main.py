# Boot + main loop


from core.state_machine import StateMachine
from core.context import Context
from utils.watchdog import check as watchdog_check

def init():
    ctx = Context()
    sm = StateMachine()
    return ctx, sm



def update_context(context):
    context.update()

def main():
    context, state_machine = init()
    running = True
    while running:
        update_context(context)
        state = state_machine.current()
        state.tick(context)
        watchdog_check()

if __name__ == "__main__":
    main()
