"""Public static checks; runtime evidence still requires Docker."""
from pathlib import Path

dockerfile = [line.strip().lower() for line in Path("Dockerfile").read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
ignore = [line.strip().lower() for line in Path(".dockerignore").read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
checks = {
    "named builder stage": any(line.startswith("from ") and " as builder" in line for line in dockerfile),
    "copies compiled artifact from builder": any(line.startswith("copy --from=builder ") for line in dockerfile),
    "explicit non-root user": any(line.startswith("user 65532") or line.startswith("user nonroot") for line in dockerfile),
    "explicit entry point": any(line.startswith("entrypoint ") for line in dockerfile),
    "ignores git history": ".git" in ignore,
    "ignores credential files": "*.env" in ignore or ".env" in ignore,
}
for label, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'} {label}")
if not all(checks.values()):
    raise SystemExit(1)
