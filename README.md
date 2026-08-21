# F34 Agentic Prompt Engineering

Standalone multi-agent reference architecture for treating prompts as versioned, testable engineering artifacts rather than ad hoc text.

## Agents
Prompt Design Agent, Evaluation Dataset Agent, Regression Agent, Adversarial/Injection Agent, Structured Output Agent, and Prompt Engineering Orchestrator.

The system records prompt/model/config provenance, evaluation evidence, regression results, adversarial cases, and unresolved blockers.

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** Provider-backed performance must be independently evaluated for the target model, configuration, application, and threat model.

AI Engineering Handbook Series by Mahsa Keikha: https://a.co/d/0cbZnSMi and https://a.co/d/07HnRY7H

MIT licensed.
