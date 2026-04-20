import os
from pathlib import Path
from typing import Optional


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_PATH = PROJECT_ROOT / ".env"


def load_local_env(env_path: Path = DEFAULT_ENV_PATH) -> None:
    """Load simple KEY=VALUE pairs from a local .env file without extra deps."""
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("export "):
            line = line[len("export "):].strip()

        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key:
            os.environ.setdefault(key, value)


def get_env_var(name: str, default: Optional[str] = None) -> Optional[str]:
    load_local_env()
    return os.getenv(name, default)


def get_required_env_var(name: str) -> str:
    value = get_env_var(name)
    if value:
        return value

    raise RuntimeError(
        f"Missing required environment variable '{name}'. "
        f"Set it in the shell or in {DEFAULT_ENV_PATH}."
    )
