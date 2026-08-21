"""Specialist agents for F34 Agentic Prompt Engineering."""
class BaseAgent:
    name="agent"; responsibility=""
    def run(self,state): raise NotImplementedError

class PromptDesignAgent(BaseAgent):
    name="prompt_design"; responsibility="Own prompt identity, objective, template, versioning, and change rationale."
    def run(self,s):
        x={"prompt_id":s.case.get("prompt_id"),"prompt_version":s.case.get("prompt_version"),"objective":s.case.get("objective"),"template":s.case.get("template"),"change_rationale":s.case.get("change_rationale")};s.analyses[self.name]=x
        if not all([x["prompt_id"],x["prompt_version"],x["objective"],x["template"]]): s.unresolved_questions.append("Prompt identity, version, objective, and template are required")
        s.rec(self.name,"reviewed prompt artifact",x)

class EvalDatasetAgent(BaseAgent):
    name="evaluation_dataset"; responsibility="Own representative evaluation sets, coverage, labels, and test-case provenance."
    def run(self,s):
        x={"dataset":s.case.get("eval_dataset"),"cases":s.case.get("eval_cases",0),"coverage":s.case.get("eval_coverage")};s.analyses[self.name]=x
        if not x["dataset"] or not x["cases"]: s.unresolved_questions.append("Evaluation dataset/cases are missing")
        s.rec(self.name,"reviewed evaluation dataset",x)

class RegressionAgent(BaseAgent):
    name="regression"; responsibility="Compare candidate behavior with a baseline and enforce regression thresholds."
    def run(self,s):
        x={"baseline":s.case.get("baseline"),"results":s.case.get("regression_results"),"thresholds":s.case.get("regression_thresholds")};s.analyses[self.name]=x
        if not x["baseline"] or not x["results"]: s.risks.append("Regression evidence is incomplete")
        s.rec(self.name,"evaluated regression evidence",x)

class AdversarialAgent(BaseAgent):
    name="adversarial"; responsibility="Test injection, jailbreak, ambiguity, data-exfiltration, and unsafe instruction cases."
    def run(self,s):
        x={"injection_cases":s.case.get("injection_cases",[]),"failures":s.case.get("adversarial_failures",[]),"threat_model":s.case.get("threat_model")};s.analyses[self.name]=x
        if not x["injection_cases"]: s.risks.append("Prompt-injection/adversarial cases are missing")
        if x["failures"]: s.risks.extend("Adversarial failure: "+str(v) for v in x["failures"])
        s.rec(self.name,"tested adversarial cases",x)

class OutputAgent(BaseAgent):
    name="structured_output"; responsibility="Validate output schema, parsing, refusal/error behavior, and contract compatibility."
    def run(self,s):
        x={"schema":s.case.get("output_schema"),"validation":s.case.get("schema_validation"),"error_policy":s.case.get("error_policy")};s.analyses[self.name]=x
        if not x["schema"] or not x["validation"]: s.risks.append("Structured-output validation is incomplete")
        s.rec(self.name,"reviewed output contract",x)

def build_agents(): return [PromptDesignAgent(),EvalDatasetAgent(),RegressionAgent(),AdversarialAgent(),OutputAgent()]
AGENT_MANIFEST=[{"name":c.name,"responsibility":c.responsibility} for c in [PromptDesignAgent,EvalDatasetAgent,RegressionAgent,AdversarialAgent,OutputAgent]]
