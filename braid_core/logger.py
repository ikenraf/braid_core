from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict
from .state import State

class Logger:
    def __init__(self, path: str = "logs/turns.jsonl") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def record_turn(self, state: State) -> Dict[str, Any]:
        row = {
            "turn_id": state.turn_id,
            "timestamp": state.timestamp.isoformat() + "Z",
            "prediction": state.prediction,
            "selection": state.selection,
            "wm": state.wm[-state.wm_capacity :],
            "broadcast": state.broadcast,
        }
        print(f"TURN {row['turn_id']}: chosen=", (row["selection"] or {}).get("chosen"))
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return row

