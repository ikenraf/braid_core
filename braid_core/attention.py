from __future__ import annotations
from typing import Dict, Any
from .state import State

class Attention:
    """Select a candidate to broadcast. For M1, pick max score; later add thresholds/interrupts."""

    def select(self, state: State) -> Dict[str, Any]:
        preds = state.prediction or {}
        cands = preds.get("candidates", [])
        if not cands:
            return {"chosen": None, "reason": "no_candidates"}
        chosen = max(cands, key=lambda c: c.get("score", 0.0))
        return {"chosen": chosen, "reason": "argmax_score"}

