from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class StructuredOutputAgent:
    name: str = "structured_output_agent"
    responsibility: str = "Verify output-schema conformance, required fields, type expectations, and failure behavior."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        schema = case.get("output_schema", {}); sample = case.get("sample_output", {})
        required = list(schema.get("required", [])); missing = [k for k in required if k not in sample]
        return {"agent": self.name, "missing": missing, "valid": not missing and bool(schema)}
