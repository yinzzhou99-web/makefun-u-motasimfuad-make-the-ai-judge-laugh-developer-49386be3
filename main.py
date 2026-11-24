#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Stdlib only. Writes one funny developer excuse for code breaking in
production to /output/entry.txt. Clears nothing; the grader owns /output.
"""

from pathlib import Path

LINE = "The code passed every test, because the tests were written by the same optimistic developer who wrote the bug."

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
print(f"wrote {len(LINE)} characters to /output/entry.txt")
