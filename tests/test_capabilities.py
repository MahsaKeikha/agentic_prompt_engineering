from src.agents import AGENT_MANIFEST
from src.skills.prompting import SKILL_MANIFEST
from src.tools.prompting import TOOL_MANIFEST

def test_capabilities():
 assert len(AGENT_MANIFEST)==5
 assert len(SKILL_MANIFEST)==5
 assert len(TOOL_MANIFEST)==5
 assert all(a["skills"] and a["tools"] for a in AGENT_MANIFEST)
