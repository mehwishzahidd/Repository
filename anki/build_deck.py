"""Build anki/glossary.tsv from GLOSSARY.md. Import into Anki: File → Import,
choose the .tsv, fields separated by Tab, first field = Front, second = Back."""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
rows = []
for line in (root / "GLOSSARY.md").read_text().splitlines():
    if not line.startswith("| **"):
        continue
    cells = [c.strip() for c in line.strip("|").split("|")]
    term = re.sub(r"\*\*", "", cells[0]).strip()
    meaning = cells[1].strip()
    stage = cells[2].strip()
    rows.append(f"{term}\t{meaning} (Stage {stage})")
(root / "anki" / "glossary.tsv").write_text("\n".join(rows) + "\n")
print(f"wrote {len(rows)} cards to anki/glossary.tsv")
