from typing import Any, Dict

def evaluation_planning(case: Dict[str, Any]) -> Dict[str, Any]:
    data = case.get("evaluation_dataset", {})
    return {"cases": int(data.get("cases", 0)), "edge_cases": int(data.get("edge_cases", 0)), "held_out": bool(data.get("held_out")), "metrics": list(case.get("evaluation_metrics", []))}
