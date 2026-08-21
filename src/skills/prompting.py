def design_prompt(a):return {**a,"questions":([] if all(a.get(k) for k in ("prompt_id","prompt_version","objective","template")) else ["Prompt identity, version, objective, and template are required"])}
def assess_eval_set(a):return {**a,"questions":([] if a["dataset"] and a["cases"] else ["Evaluation dataset/cases are missing"])}
def analyze_regression(a):return {**a,"risks":([] if all(a.values()) else ["Regression evidence is incomplete"])}
def analyze_adversarial(a):
 r=[]
 if not a["injection_cases"]:r.append("Prompt-injection/adversarial cases are missing")
 r.extend("Adversarial failure: "+str(x) for x in a["failures"])
 return {**a,"risks":r}
def validate_output_contract(a):return {**a,"risks":([] if all(a.values()) else ["Structured-output validation is incomplete"])}
SKILL_MANIFEST=["design_prompt","assess_eval_set","analyze_regression","analyze_adversarial","validate_output_contract"]
