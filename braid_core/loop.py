from __future__ import annotations
import os
from datetime import datetime
from .state import State
from .prediction import PredictionEngine
from .attention import Attention
from .working_memory import WorkingMemory
from .logger import Logger

# Turn count can be overridden by env var, default 5
TURNS = int(os.getenv("M1_TURNS", "5"))
WM_CAPACITY = int(os.getenv("WM_CAPACITY", "2"))

prediction = PredictionEngine()
attention = Attention()
wm = WorkingMemory()
logger = Logger()

def run_loop(turns: int = TURNS) -> None:
    state = State(wm_capacity=WM_CAPACITY)
    for t in range(1, turns + 1):
        state.turn_id = t
        state.timestamp = datetime.utcnow()

        state.prediction = prediction.predict(state)
        state.selection = attention.select(state)

        chosen = (state.selection or {}).get("chosen")
        state.broadcast = (chosen or {}).get("text") if chosen else None
        wm.store(state, {"turn": t, "broadcast": state.broadcast})

        logger.record_turn(state)

if __name__ == "__main__":
    run_loop()
