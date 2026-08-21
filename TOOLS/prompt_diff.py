from dataclasses import dataclass
from difflib import unified_diff

@dataclass
class PromptDiff:
    def compare(self, old: str, new: str) -> str:
        return "".join(unified_diff(old.splitlines(True), new.splitlines(True), fromfile="old", tofile="new"))
