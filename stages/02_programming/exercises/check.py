"""
Auto-checker for Stage 02 exercises.
====================================

    python3 stages/02_programming/exercises/check.py

Reports ✅ / ❌ / ⬜ per exercise. Keep editing exercises.py and re-running.
"""
import json
import os
import sys
import tempfile
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exercises as ex  # noqa: E402


def check(cond, msg):
    if not cond:
        raise AssertionError(msg)


def t_word_counts():
    check(ex.word_counts("a b a") == {"a": 2, "b": 1}, 'word_counts("a b a")')
    check(ex.word_counts("") == {}, 'word_counts("") should be {}')
    check(ex.word_counts("The the") == {"the": 2}, "should lowercase")


def t_group():
    got = ex.group_by_first_letter(["apple", "bob", "avocado"])
    check(got == {"a": ["apple", "avocado"], "b": ["bob"]}, f"got {got!r}")
    check(ex.group_by_first_letter([]) == {}, "empty list -> {}")


def t_parse_age():
    check(ex.parse_age(" 42 ") == 42, '" 42 " -> 42')
    for bad in ["abc", "-1", "151", "", "4.5"]:
        try:
            ex.parse_age(bad)
        except ValueError:
            continue
        raise AssertionError(f"parse_age({bad!r}) should raise ValueError")


def t_safe_load_json():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.json"
        p.write_text(json.dumps({"k": [1, 2]}))
        check(ex.safe_load_json(p) == {"k": [1, 2]}, "should parse the file")
        check(ex.safe_load_json(Path(d) / "missing.json", default={"items": []}) == {"items": []},
              "missing file -> default")


def t_stack():
    s = ex.Stack()
    check(len(s) == 0, "new stack has len 0")
    s.push(1); s.push(2)
    check(s.peek() == 2 and len(s) == 2, "peek should be 2")
    check(s.pop() == 2 and s.pop() == 1, "pop order")
    for op in (s.pop, s.peek):
        try:
            op()
        except IndexError:
            continue
        raise AssertionError(f"{op.__name__}() on empty stack should raise IndexError")


def t_chunks():
    import types
    g = ex.chunks([1, 2, 3, 4, 5], 2)
    check(isinstance(g, types.GeneratorType), "chunks must be a generator (use yield)")
    check(list(g) == [[1, 2], [3, 4], [5]], "chunks([1..5], 2)")
    check(list(ex.chunks([], 3)) == [], "empty -> []")
    try:
        list(ex.chunks([1], 0))
    except ValueError:
        pass
    else:
        raise AssertionError("size < 1 should raise ValueError")


def t_count_calls():
    @ex.count_calls
    def f(x):
        return x * 2
    check(f(1) == 2 and f(2) == 4, "must return the wrapped result")
    check(getattr(f, "calls", None) == 2, f"f.calls should be 2, got {getattr(f, 'calls', None)!r}")


def t_top_k():
    check(ex.top_k(["b", "a", "b", "a", "c"], 2) == [("a", 2), ("b", 2)], "ties alphabetical")
    check(ex.top_k(["x"], 5) == [("x", 1)], "k larger than vocab")
    check(ex.top_k([], 3) == [], "empty")


def t_extract_links():
    html = '<a href="/a">x</a> <img src="/i.png"> <a href="https://x.com/p?q=1">y</a>'
    check(ex.extract_links(html) == ["/a", "https://x.com/p?q=1"], "two hrefs, in order")
    check(ex.extract_links("<p>none</p>") == [], "no links -> []")


def t_parse_log_line():
    got = ex.parse_log_line("2026-01-15 09:30:12 ERROR db: connection timed out")
    check(got == {"date": "2026-01-15", "time": "09:30:12", "level": "ERROR",
                  "component": "db", "message": "connection timed out"}, f"got {got!r}")
    check(ex.parse_log_line("garbage") is None, "non-matching -> None")


def t_contact_book():
    book = ex.ContactBook()
    a = ex.Contact("ana", "ana@x.com", ["friend"])
    book.add(a)
    check(book.find("ana@x.com") is a, "find returns the contact")
    check(book.find("zed@x.com") is None, "missing -> None")
    try:
        book.add(ex.Contact("dup", "ana@x.com"))
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate email should raise ValueError")
    book.add(ex.Contact("ben", "ben@x.com"))
    check(book.with_tag("friend") == [a], "with_tag")
    check(ex.Contact("z", "z@x.com").tags == [], "default tags empty")


def t_lru():
    c = OrderedDict()
    ex.lru_put(c, "a", 1, 2); ex.lru_put(c, "b", 2, 2)
    check(ex.lru_get(c, "a") == 1, "get a")
    ex.lru_put(c, "c", 3, 2)                      # should evict "b" (least recent)
    check("b" not in c and "a" in c and "c" in c, f"after evict: {list(c)}")
    check(ex.lru_get(c, "b") is None, "missing -> None")
    ex.lru_put(c, "a", 10, 2)
    check(c["a"] == 10 and len(c) == 2, "update keeps size")


TESTS = [
    ("word_counts", t_word_counts), ("group_by_first_letter", t_group),
    ("parse_age", t_parse_age), ("safe_load_json", t_safe_load_json),
    ("Stack", t_stack), ("chunks", t_chunks), ("count_calls", t_count_calls),
    ("top_k", t_top_k), ("extract_links", t_extract_links),
    ("parse_log_line", t_parse_log_line), ("ContactBook", t_contact_book),
    ("lru_v1", t_lru),
]


def run():
    print("=" * 56)
    print("  Checking your Stage 02 exercises...")
    print("=" * 56)
    solved = 0
    for name, test in TESTS:
        try:
            test()
        except AssertionError as e:
            msg = str(e)
            if "None" in msg and ("got None" in msg or "should" in msg) and "returns None" not in msg:
                print(f"❌ {name:22} — {msg}")
            else:
                print(f"❌ {name:22} — {msg}")
        except (TypeError, AttributeError) as e:
            print(f"⬜ {name:22} — not done yet ({type(e).__name__}: {e})")
        except Exception as e:
            print(f"❌ {name:22} — your code raised {type(e).__name__}: {e}")
        else:
            print(f"✅ {name:22} — passed!")
            solved += 1
    print("-" * 56)
    print(f"  Score: {solved} / {len(TESTS)} exercises complete.")
    if solved == len(TESTS):
        print("  🎉🎉  PERFECT! Stage 02 done. Commit it:")
        print("        git add stages/ && git commit -m 'Finish Stage 02'")
    elif solved == 0:
        print("  Just getting started — open exercises.py and fill in the first one.")
    else:
        print("  Nice progress! Keep going — re-run this after each fix.")
    print("=" * 56)


if __name__ == "__main__":
    run()
