# Soft reset hooks


import time

_last_check = time.time()
_max_loop_time = 2.0  # seconds

def check():
    global _last_check
    now = time.time()
    if now - _last_check > _max_loop_time:
        print("[WATCHDOG] Loop took too long! Triggering recovery...")
        from core.recovery import handle_recovery
        handle_recovery(None)  # Pass context if needed
    _last_check = now
