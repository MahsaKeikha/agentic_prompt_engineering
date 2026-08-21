from typing import Dict

def regression_analysis(baseline: Dict[str, float], candidate: Dict[str, float], tolerance: float = 0.0) -> Dict[str, object]:
    regressions = [m for m, value in baseline.items() if float(candidate.get(m, float('-inf'))) + tolerance < float(value)]
    return {"regressions": regressions, "pass": not regressions}
