# F34 Agentic Prompt Engineering

Standalone multi-agent reference architecture for treating prompts as versioned, testable engineering artifacts rather than ad hoc text.

## Architecture

```text
src/
├── agents/          Prompt Design, Evaluation, Regression, Adversarial, Output agents
├── tools/           deterministic prompt-evaluation record builders
├── skills/          reusable prompt-engineering procedures
├── memory/          prompt-version memory
├── schemas/         prompt artifact contracts
├── prompts/         engineering principles
├── config/          regression and adversarial gates
├── safety/          prompt-release policy
├── observability/   trace summaries
├── state.py
├── gates.py
├── orchestrator.py
├── system.py
└── run.py
```

### Agents
Prompt Design Agent, Evaluation Dataset Agent, Regression Agent, Adversarial/Injection Agent, Structured Output Agent, coordinated by the Prompt Engineering Orchestrator.

### Skills
Prompt design, evaluation-set assessment, regression analysis, adversarial analysis, output-contract validation.

### Tools
Prompt artifact builder, evaluation record, regression record, adversarial record, schema record.

See `docs/AGENTS_TOOLS_SKILLS.md`.

```bash
python -m src.run --example
pytest -q
```

Prompt/model/configuration provenance, evaluation evidence, regression behavior, adversarial cases, and structured-output validation are explicit workflow artifacts.

**Maturity: Reference implementation.** Provider-backed performance must be independently evaluated for the target model, configuration, application, and threat model.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
