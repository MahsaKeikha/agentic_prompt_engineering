# F34 Agentic Prompt Engineering

Standalone multi-agent reference architecture for treating prompts as versioned, testable engineering artifacts rather than ad hoc text.

## Agent team

- Prompt Design Agent
- Evaluation Dataset Agent
- Regression Agent
- Adversarial and Injection Agent
- Structured Output Agent
- Prompt Engineering Orchestrator

The **actual specialist agent implementations live in [`src/agents.py`](src/agents.py)**. Shared run state, provenance, orchestration, and release gating live in [`src/system.py`](src/system.py). Agent-composition and workflow tests live under [`tests/`](tests/).

## Architecture

```text
Prompt artifact
   ↓
Prompt Design Agent
   ↓
Evaluation Dataset Agent
   ↓
Regression Agent
   ↓
Adversarial Agent
   ↓
Structured Output Agent
   ↓
Prompt Engineering Orchestrator / Release Gate
```

The system records prompt/model/config provenance, evaluation evidence, regression results, adversarial cases, and unresolved blockers.

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** Provider-backed performance must be independently evaluated for the target model, configuration, application, and threat model.

## AI Engineering Handbook Series

By Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

MIT licensed.
