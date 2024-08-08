default:
    just --list

rye-sync:
    rye sync

pre-commit:
    pre-commit install

ollama-start:
    ollama serve

llama3:
    ollama pull llama3
