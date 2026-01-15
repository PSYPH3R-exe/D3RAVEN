# d3_autobot

A lean, deterministic Diablo 3 automation bot architecture. Industrial, boring, and reliable. Inspired by ROS-BOT discipline, not gimmicks.

## Project Structure

- **main.py**: Boot + main loop
- **core/**: State machine, context, recovery
- **perception/**: Screen, UI hashes, detectors
- **actions/**: Movement, combat, inventory
- **loot/**: Pickit rules, scorer, cache
- **config/**: Regions, weights, timings
- **utils/**: Timing, logger, watchdog

## Principles
- One loop, one state, one decision per frame
- No parallel logic or background magic
- Explicit state transitions
- Perception only confirms facts
- Combat is deterministic
- Loot logic is tiered and cache-backed
- Fast, boring recovery

## Setup
1. Python 3.10+
2. Install dependencies (see below)
3. Configure regions, weights, timings in config/
4. Run main.py

## Dependencies
- [Add required packages here]

## MCP Integration
- [Add MCP details here if needed]

## Extensions
- [List VS Code extensions for Python development]

## License
Private, all rights reserved.
