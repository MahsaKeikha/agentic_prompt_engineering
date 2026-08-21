from typing import Any, Dict

def structured_output_assessment(payload: Dict[str, Any], schema: Dict[str, Any]) -> Dict[str, Any]:
    required = list(schema.get("required", [])); missing = [k for k in required if k not in payload]
    return {"required": required, "missing": missing, "valid": not missing and bool(schema)}
