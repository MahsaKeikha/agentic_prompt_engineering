from .agents import build_agents
from .gates import evaluate_prompt_gate
from .state import RunState
SYSTEM_ID,SYSTEM_NAME,VERSION="F34","Agentic Prompt Engineering","0.2.0"
def run_system(case,approve=False):
 s=RunState(case);s.record("prompt_engineering_orchestrator","run started",{"system_id":SYSTEM_ID,"version":VERSION,"model":case.get("model"),"configuration":case.get("configuration")})
 for a in build_agents():a.run(s)
 for e in case.get("evidence",[]):s.evidence.append({"claim":str(e.get("claim","")),"source":str(e.get("source","")),"status":str(e.get("status","supplied"))})
 s.conflicts.extend(case.get("conflicts",[]));status=evaluate_prompt_gate(s,approve);s.record("prompt_engineering_orchestrator","prompt release gate evaluated",{"approve":approve,"status":status})
 return {"system_id":SYSTEM_ID,"system_name":SYSTEM_NAME,"version":VERSION,"run_id":s.run_id,"domain":"prompt_engineering","analyses":s.analyses,"evidence":s.evidence,"unresolved_questions":s.unresolved_questions,"conflicts":s.conflicts,"risks":s.risks,"recommendation":"Resolve prompt engineering blockers." if status=="blocked" else "Prompt artifact is ready for accountable human review.","status":status,"trace":s.trace}
