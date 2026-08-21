from src.system import run_system
def case():return {"prompt_id":"p","prompt_version":"1","objective":"o","template":"t","model":"fixture","configuration":"det","eval_dataset":"d","eval_cases":10,"baseline":"b","regression_results":"pass","injection_cases":["attack"],"adversarial_failures":[],"output_schema":"s","schema_validation":"pass"}
def test_clean_waits():assert run_system(case())["status"]=="awaiting_human_approval"
def test_clean_approval():assert run_system(case(),True)["status"]=="approved_for_human_follow_through"
def test_missing_eval_blocks():
 c=case();c["eval_cases"]=0;assert run_system(c,True)["status"]=="blocked"
def test_adversarial_failure_blocks():
 c=case();c["adversarial_failures"]=["injection succeeded"];assert run_system(c,True)["status"]=="blocked"
