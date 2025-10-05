from __future__ import annotations
from typing import Any, Dict
from .state import State

class WorkingMemory:
    """Bounded store with simple FIFO eviction for M1."""

    def store(self, state: State, item: Dict[str, Any]) -> None:
        if item is None:
            return
        state.wm.append(item)
        while len(state.wm) > state.wm_capacity:
            state.wm.pop(0)  # FIFO eviction

