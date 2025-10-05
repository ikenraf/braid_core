from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from datetime import datetime

@dataclass
class State:
    """Minimal shared state for the M1 skeleton loop."""
    turn_id: int = 0
    timestamp: datetime = field(default_factory=datetime.utcnow)
    # working memory (bounded)
    wm: List[Dict[str, Any]] = field(default_factory=list)
    wm_capacity: int = 2

    # signals
    prediction: Optional[Dict[str, Any]] = None
    selection: Optional[Dict[str, Any]] = None

    # input/output (placeholder fields for future expansion)
    input_text: Optional[str] = None
    broadcast: Optional[str] = None

