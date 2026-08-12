## Summary

Describe the change and the review scenario it supports.

## Risk Review

- [ ] This change does not introduce command execution.
- [ ] This change does not upload repository contents or credentials.
- [ ] New risky example strings are synthetic and documented.
- [ ] New rules include tests or a clear manual validation path.

## Testing

```bash
python -m unittest discover -s tests
agent-surface-auditor . --format markdown
```
