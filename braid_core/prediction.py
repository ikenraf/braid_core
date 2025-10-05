from __future__ import annotations
from typing import Dict, Any
from .state import State

class PredictionEngine:
    """Tiny stub that produces an expectation and candidates.
    In M1, this is deterministic/seeded; later we can plug a model.
    """

    def predict(self, state: State) -> Dict[str, Any]:
        candidates = [
            {"id": f"cand-{state.turn_id}-a", "score": 0.6, "text": "note:a"},
            {"id": f"cand-{state.turn_id}-b", "score": 0.4, "text": "note:b"},
        ]
        expectation = {"mean_score": sum(c["score"] for c in candidates)/len(candidates)}
        return {"candidates": candidates, "expectation": expectation}

