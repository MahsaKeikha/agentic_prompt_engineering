from typing import Any, Dict

def prompt_design_strategy(case: Dict[str, Any]) -> Dict[str, Any]:
    return {"objective": case.get("prompt", {}).get("objective"), "constraints": list(case.get("constraints", [])), "output_contract": case.get("output_schema"), "versioned": bool(case.get("prompt", {}).get("version"))}
