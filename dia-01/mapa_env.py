import os 
from pathlib import Path

ambiente = os.getenv("AMBIENTE", "desenvolvimento")

env_file = Path(f".env.{ambiente}")

if env_file.exists():
    with open(env_file) as f:
        for linha in f:
            linha = linha.strip()
            if linha and not linha.startswith("#"):
                key, value = linha.split("=", 1)
                os.environ[key] = value

print(f"Ambiente: {ambiente} Carregado!")