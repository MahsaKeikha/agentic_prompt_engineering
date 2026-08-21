from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"AGENTS": ["prompt_design_agent.py", "evaluation_dataset_agent.py", "regression_agent.py", "adversarial_injection_agent.py", "structured_output_agent.py"], "TOOLS": ["prompt_registry.py", "eval_runner.py", "prompt_diff.py", "injection_scanner.py", "schema_validator.py"], "SKILLS": ["prompt_design_strategy.py", "evaluation_planning.py", "regression_analysis.py", "injection_analysis.py", "structured_output_assessment.py"]}
def test_visible_components_exist_and_compile():
    for folder, names in EXPECTED.items():
        for name in names:
            path = ROOT / folder / name
            assert path.exists(), path
            compile(path.read_text(), str(path), "exec")
