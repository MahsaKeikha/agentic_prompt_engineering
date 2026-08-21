from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class EvaluationDatasetAgent:
    name: str = "evaluation_dataset_agent"
    responsibility: str = "Check evaluation-set coverage, labels, edge cases, and separation from prompt-development examples."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        data = case.get("evaluation_dataset", {})
        return {"agent": self.name, "cases": int(data.get("cases", 0)), "edge_cases": int(data.get("edge_cases", 0)), "held_out": bool(data.get("held_out")), "ready": int(data.get("cases", 0)) > 0 and bool(data.get("held_out"))}
