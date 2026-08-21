from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List

@dataclass
class EvalRunner:
    def run(self, cases: Iterable[Dict[str, Any]], evaluator: Callable[[Dict[str, Any]], bool]) -> Dict[str, Any]:
        items: List[Dict[str, Any]] = list(cases)
        passed = sum(1 for item in items if evaluator(item))
        return {"cases": len(items), "passed": passed, "pass_rate": passed / max(1, len(items))}
