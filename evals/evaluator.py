def evaluate_result(r):
 a=r.get("analyses",{});return {"prompt_versioned":"prompt_design" in a,"eval_dataset_present":"evaluation_dataset" in a,"regression_present":"regression" in a,"adversarial_present":"adversarial" in a,"output_contract_present":"structured_output" in a,"blocked":r.get("status")=="blocked"}
