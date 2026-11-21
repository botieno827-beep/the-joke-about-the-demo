import os
from pathlib import Path

JOKE = "My coding agent nailed the rehearsal, then saw the audience and threw an 'untrusted input' error."
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")
