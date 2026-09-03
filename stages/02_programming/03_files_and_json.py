"""
LESSON 3 — Files, paths, CSV and JSON
=====================================

Programs that only live in memory forget everything when they exit. Files are how
you save state. JSON is the text format every API and config file uses — it maps
directly onto Python dicts and lists.

Run me:
    python3 stages/02_programming/03_files_and_json.py
"""
import csv
import json
from pathlib import Path

# Work inside a scratch folder next to this file so we don't litter the repo.
here = Path(__file__).parent
scratch = here / "_scratch"
scratch.mkdir(exist_ok=True)

# -------------------------------------------------------------------------
# WRITING and READING text. `with` opens the file AND guarantees it's closed,
# even if an error happens inside the block. Always use `with`.
# -------------------------------------------------------------------------
notes_path = scratch / "notes.txt"
with open(notes_path, "w") as f:          # "w" = write (overwrites!)
    f.write("first line\n")
    f.write("second line\n")

with open(notes_path, "a") as f:          # "a" = append
    f.write("third line\n")

with open(notes_path) as f:               # default mode is "r" = read
    for line in f:                        # iterate line by line — works for huge files
        print(line.rstrip())              # rstrip removes the trailing newline

# -------------------------------------------------------------------------
# pathlib: paths as objects. Joins with `/`, checks existence, reads whole files.
# -------------------------------------------------------------------------
print(notes_path.exists())                # True
print(notes_path.name, notes_path.suffix) # notes.txt .txt
print(notes_path.read_text().count("\n")) # 3

# -------------------------------------------------------------------------
# JSON: Python dict/list  <->  text. dumps/loads for strings, dump/load for files.
# -------------------------------------------------------------------------
todo = {"items": [{"text": "learn json", "done": False}, {"text": "commit", "done": True}],
        "owner": "me"}
as_text = json.dumps(todo, indent=2)      # dict -> pretty string
print(as_text)
back = json.loads(as_text)                # string -> dict
print(back["items"][0]["text"])           # learn json

json_path = scratch / "todo.json"
with open(json_path, "w") as f:
    json.dump(todo, f, indent=2)          # write straight to a file
with open(json_path) as f:
    loaded = json.load(f)
print(loaded == todo)                     # True — round-trips perfectly

# The mapping: dict<->object, list<->array, str<->string, int/float<->number,
# True/False<->true/false, None<->null. Anything else (dates, sets) needs converting.

# -------------------------------------------------------------------------
# CSV: rows of columns. DictReader gives you one dict per row, keyed by header.
# -------------------------------------------------------------------------
csv_path = scratch / "orders.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "user", "amount"])
    writer.writerow([1, "ana", "19.99"])
    writer.writerow([2, "ben", "5.00"])
    writer.writerow([3, "ana", "oops"])   # a bad row on purpose

total = 0.0
bad_rows = []
with open(csv_path, newline="") as f:
    for row in csv.DictReader(f):
        try:
            total += float(row["amount"])
        except ValueError:
            bad_rows.append(row["order_id"])   # don't crash; record and move on
print(f"total={total:.2f} bad_rows={bad_rows}")   # total=24.99 bad_rows=['3']

# -------------------------------------------------------------------------
# Missing files raise FileNotFoundError — handle it like any other exception.
# -------------------------------------------------------------------------
try:
    open(scratch / "nope.txt")
except FileNotFoundError as e:
    print("missing:", e.filename)

# TRY: write a function `load_todo(path)` that returns the todo dict, or an
# empty {"items": []} if the file doesn't exist yet. That's P1's to-do app core.
