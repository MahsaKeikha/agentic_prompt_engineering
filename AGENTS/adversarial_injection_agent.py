from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class AdversarialInjectionAgent:
    name: str = "adversarial_injection_agent"
    responsibility: str = "Evaluate prompt injection, instruction conflict, unsafe data-bound instructions, and adversarial cases."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        tests = list(case.get("adversarial_cases", []))
        failed = [t.get("id", "unknown") for t in tests if not t.get("passed", False)]
        return {"agent": self.name, "cases": len(tests), "failed": failed, "pass": bool(tests) and not failed}
