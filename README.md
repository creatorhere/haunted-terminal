# Haunted Terminal

A small Python shell wrapper where a ghost whispers about every command you run. The ghost is a local open-weight model (Gemma 3 via Ollama), so it runs fully offline and your commands never leave your machine.

Built for the Hacktoberfest 2026 Open-Source AI Challenge (theme: Ghost in the Machine).

## How it works

1. You type a normal command (`dir`, `echo hello`, `cd ..`).
2. The command runs, and its output is shown as usual.
3. The command and a trimmed copy of its output are sent to a local model through Ollama.
4. The ghost whispers one short line about what you just did. It sounds amused when a command works and mournful when it fails.
5. Every whisper is saved to `haunting_log.txt`.

## Requirements

- Python 3.9 or newer
- [Ollama](https://ollama.com)
- The `ollama` Python package

## Setup

```
ollama pull gemma3:1b
pip install ollama
```

## Run

```
python haunted.py
```

Type `exit` to leave. Use normal commands only. Interactive programs (like `python` on its own) won't work inside the ghost terminal.

## Customize

- **Personality:** edit the `GHOST` line in `haunted.py`, for example "a grumpy old sysadmin who retired in 1999".
- **Model:** change the `MODEL` line to any model you have in Ollama.
- **Whisper colour:** change the `\033[96m` colour code in the print line.

## Why open source?

- It works offline.
- Your commands (which can contain private paths and data) stay on your machine.
- You can swap the model or the ghost's personality with one line.

## Warning

This tool runs whatever you type, just like a normal terminal. Use it only for your own commands.
