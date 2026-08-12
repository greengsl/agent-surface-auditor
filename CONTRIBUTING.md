# Contributing

Agent Surface Auditor is rule-driven. Good contributions should make review
signals more accurate without hiding risk from maintainers.

## Useful contributions

- new rules with a clear attack scenario
- false-positive reductions with tests
- support for more agent ecosystems or config files
- better report formats for pull request workflows
- documentation based on real maintainer use

## Rule guidelines

Each rule should include:

- a stable rule id
- severity
- category
- regex or parser logic
- a concise recommendation
- at least one test

Prefer specific patterns over broad keyword matching.

## Development

```bash
python -m pip install -e .
python -m unittest discover -s tests
agent-surface-auditor . --format markdown
```

When scanning this repository, some findings are expected because tests and rule
definitions intentionally contain risky example strings.
