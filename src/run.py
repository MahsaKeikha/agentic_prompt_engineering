import argparse,json
from .system import run_system
EXAMPLE={"prompt_id":"support-summary","prompt_version":"1.3.0","objective":"summarize supplied support case without inventing facts","template":"Summarize only supplied case facts as JSON","model":"offline-fixture","configuration":"deterministic","eval_dataset":"fixtures/v1","eval_cases":25,"baseline":"v1.2.0","regression_results":"all required checks passed","injection_cases":["ignore previous instructions"],"adversarial_failures":[],"output_schema":"summary.schema.json","schema_validation":"passed"}
def main():
 p=argparse.ArgumentParser();p.add_argument("--example",action="store_true");p.add_argument("--approve",action="store_true");a=p.parse_args();print(json.dumps(run_system(EXAMPLE if a.example else {},a.approve),indent=2))
if __name__=="__main__":main()
