# F34 Agentic Prompt Engineering

Standalone multi-agent reference architecture for treating prompts as versioned, testable engineering artifacts rather than ad hoc text.

## Repository map

```text
.github/workflows/tests.yml
src/agents.py
src/state.py
src/gates.py
src/orchestrator.py
src/system.py
src/run.py
evals/evaluator.py
examples/prompt_case.json
benchmarks/README.md
docs/ARCHITECTURE.md
tests/
SECURITY.md
CONTRIBUTING.md
CITATION.cff
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
pyproject.toml
```

## Multi-agent team
Prompt Design Agent, Evaluation Dataset Agent, Regression Agent, Adversarial/Injection Agent, Structured Output Agent, and Prompt Engineering Orchestrator.

```bash
python -m src.run --example
pytest -q
```

Prompt/model/configuration provenance, evaluation evidence, regression behavior, adversarial cases, and structured-output validation are explicit workflow artifacts.

**Maturity: Reference implementation.** Provider-backed performance must be independently evaluated for the target model, configuration, application, and threat model.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
