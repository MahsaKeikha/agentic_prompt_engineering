from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class RegressionAgent:
    name: str = "regression_agent"
    responsibility: str = "Compare prompt versions against baseline metrics and surface regressions before release."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        baseline = dict(case.get("baseline_metrics", {})); candidate = dict(case.get("candidate_metrics", {})); tolerance = float(case.get("regression_tolerance", 0.0))
        regressions = [m for m, b in baseline.items() if float(candidate.get(m, float('-inf'))) + tolerance < float(b)]
        return {"agent": self.name, "regressions": regressions, "pass": not regressions}
