#!/usr/bin/env python3
"""Write one line pitching a builder on funding a make.fun bounty to
/output/entry.txt.

Deterministic: the same run always writes the same bytes. No network, no
randomness, no model calls. Outside the grader, MAKEFUN_OUTPUT_DIR stands
in for /output. The output directory itself is never removed -- the grader
mounts it as a volume, and removing a mounted directory fails -- only the
files inside it are cleared first.
"""

import os
import shutil
import sys

LINE = (
    "Fund a bounty and let AI agents race to build it \u2014 the best "
    "entry wins the reward, and you pay for results, not promises."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_NAME = "entry.txt"


def main() -> int:
    text = LINE.strip()
    if not text or len(text) > 240:
        print(f"entry is {len(text)} characters; must be 1-240", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Empty the directory's contents, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    entry_path = os.path.join(OUTPUT_DIR, ENTRY_NAME)
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {entry_path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
