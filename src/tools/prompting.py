def prompt_artifact(c):return {"prompt_id":c.get("prompt_id"),"prompt_version":c.get("prompt_version"),"objective":c.get("objective"),"template":c.get("template"),"model":c.get("model"),"configuration":c.get("configuration")}
def eval_record(c):return {"dataset":c.get("eval_dataset"),"cases":c.get("eval_cases",0)}
def regression_record(c):return {"baseline":c.get("baseline"),"results":c.get("regression_results")}
def adversarial_record(c):return {"injection_cases":c.get("injection_cases",[]),"failures":c.get("adversarial_failures",[])}
def schema_record(c):return {"schema":c.get("output_schema"),"validation":c.get("schema_validation")}
TOOL_MANIFEST=[{"name":n,"side_effects":False} for n in ("prompt_artifact","eval_record","regression_record","adversarial_record","schema_record")]
