"""Verify local setup without calling the Claude API."""
import os
import sys

from dotenv import load_dotenv

# TODO 1: load variables from .env into the environment

def mask(secret: str) -> str:
    # TODO 2: return only the first 7 chars + "..." + last 4 chars
    ...

def main() -> None:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Interpreter: {sys.executable}")   # should point inside .venv

    key = os.getenv("ANTHROPIC_API_KEY")
    model = os.getenv("CLAUDE_MODEL")

    # TODO 3: if key or model is missing, print a clear error and exit with code 1
    # TODO 4: print the masked key and the model name

if __name__ == "__main__":
    main()