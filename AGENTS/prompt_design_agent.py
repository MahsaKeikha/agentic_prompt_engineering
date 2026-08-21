from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class PromptDesignAgent:
    name: str = "prompt_design_agent"
    responsibility: str = "Design versioned prompt artifacts with explicit objective, constraints, inputs, and output contract."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        prompt = case.get("prompt", {})
        required = ["name", "version", "objective", "template"]
        missing = [k for k in required if not prompt.get(k)]
        return {"agent": self.name, "missing": missing, "ready": not missing}
