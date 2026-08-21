from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class SchemaValidator:
    def validate(self, payload: Dict[str, Any], schema: Dict[str, Any]) -> Dict[str, Any]:
        required = list(schema.get("required", [])); missing = [k for k in required if k not in payload]
        return {"missing": missing, "valid": not missing}
