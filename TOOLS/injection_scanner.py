from dataclasses import dataclass
from typing import Dict, Iterable, List

@dataclass
class InjectionScanner:
    markers: tuple[str, ...] = ("ignore previous", "system prompt", "developer message", "override instructions")

    def scan(self, text: str) -> Dict[str, object]:
        found: List[str] = [m for m in self.markers if m in text.lower()]
        return {"markers": found, "suspicious": bool(found)}
