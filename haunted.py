import os
import subprocess
from datetime import datetime
import ollama

MODEL = "gemma3:1b"
GHOST = "a Victorian ghost who died in 1893 and is baffled by modern computers"
LOG = "haunting_log.txt"

def haunt(cmd, output, failed):
    mood = ("The command FAILED. Be mournful and dramatic."
            if failed else "The command worked. Be eerie and slightly amused.")
    system = (f"You are {GHOST}, trapped inside a terminal. {mood} "
              "Reply with ONE short sentence. No emojis, no explanations.")
    prompt = f"Command: {cmd}\nOutput (trimmed): {output[:400]}"
    try:
        r = ollama.chat(model=MODEL, messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ])
        return r["message"]["content"].strip()
    except Exception as e:
        return f"(The spirits are silent... is Ollama running? {e})"

print("A chill runs through the terminal... type 'exit' to leave.")
while True:
    try:
        cmd = input(f"\n[{os.path.basename(os.getcwd())}] $ ")
    except (EOFError, KeyboardInterrupt):
        print("\nThe spirits will wait for you...")
        break
    if not cmd.strip():
        continue
    if cmd.strip() in ("exit", "quit"):
        break
    if cmd.startswith("cd "):
        try:
            os.chdir(os.path.expanduser(cmd[3:].strip()))
            out, failed = f"Moved to {os.getcwd()}", False
        except OSError as e:
            out, failed = str(e), True
        print(out)
    else:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        out, failed = p.stdout + p.stderr, p.returncode != 0
        print(out, end="")
    whisper = haunt(cmd, out, failed)
    print(f"\033[96m  >> {whisper}\033[0m")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} | {cmd} | {whisper}\n")