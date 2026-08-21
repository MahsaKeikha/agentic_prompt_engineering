from typing import Any
from .base import BaseAgent
from ..skills import design_prompt, assess_eval_set, analyze_regression, analyze_adversarial, validate_output_contract
from ..tools import prompt_artifact, eval_record, regression_record, adversarial_record, schema_record
class PromptDesignAgent(BaseAgent):
 name="prompt_design";responsibility="Define versioned prompt objective and template.";required_skills=("design_prompt",);allowed_tools=("prompt_artifact",)
 def run(self,s:Any):
  a=design_prompt(prompt_artifact(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.record(self.name,"reviewed prompt artifact",a)
class EvalDatasetAgent(BaseAgent):
 name="evaluation_dataset";responsibility="Assess evaluation dataset and case coverage.";required_skills=("assess_eval_set",);allowed_tools=("eval_record",)
 def run(self,s:Any):
  a=assess_eval_set(eval_record(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.record(self.name,"reviewed evaluation dataset",a)
class RegressionAgent(BaseAgent):
 name="regression";responsibility="Compare candidate prompt behavior to baseline.";required_skills=("analyze_regression",);allowed_tools=("regression_record",)
 def run(self,s:Any):
  a=analyze_regression(regression_record(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"analyzed regression",a)
class AdversarialAgent(BaseAgent):
 name="adversarial";responsibility="Review prompt injection and adversarial evaluation evidence.";required_skills=("analyze_adversarial",);allowed_tools=("adversarial_record",)
 def run(self,s:Any):
  a=analyze_adversarial(adversarial_record(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"analyzed adversarial cases",a)
class OutputAgent(BaseAgent):
 name="structured_output";responsibility="Validate structured-output contract and schema evidence.";required_skills=("validate_output_contract",);allowed_tools=("schema_record",)
 def run(self,s:Any):
  a=validate_output_contract(schema_record(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"validated output contract",a)
CLASSES=[PromptDesignAgent,EvalDatasetAgent,RegressionAgent,AdversarialAgent,OutputAgent]
def build_agents():return [c() for c in CLASSES]
AGENT_MANIFEST=[{"name":c.name,"responsibility":c.responsibility,"skills":list(c.required_skills),"tools":list(c.allowed_tools)} for c in CLASSES]
