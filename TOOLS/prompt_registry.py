from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class PromptRegistry:
    versions: List[Dict[str, Any]] = field(default_factory=list)

    def register(self, name: str, version: str, template: str, metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
        record = {"name": name, "version": version, "template": template, "metadata": metadata or {}}
        self.versions.append(record)
        return record
