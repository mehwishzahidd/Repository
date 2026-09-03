"""
LESSON 8 — Regular expressions
==============================

A regex is a tiny pattern language for matching text. You'll use it for log
parsing, validating input, pulling URLs out of HTML (the crawler), and splitting
messy strings. Learn the ten pieces below and you can read 90% of real regexes.

Run me:
    python3 stages/02_programming/08_regular_expressions.py
"""
import re

# -------------------------------------------------------------------------
# THE BUILDING BLOCKS
#   .      any one character           \d  a digit        \w  a "word" char (letter/digit/_)
#   \s     whitespace                  [abc] one of a,b,c  [^abc] anything except a,b,c
#   *      0 or more of the previous   +   1 or more      ?   0 or 1
#   {3}    exactly 3                   {2,5} between 2 and 5
#   ^      start of string             $   end of string
#   (...)  a GROUP you can pull out    a|b  a or b
# Always write patterns as raw strings: r"..." so backslashes survive.
# -------------------------------------------------------------------------

# re.search: find the first match anywhere. Returns a Match object or None.
m = re.search(r"\d+", "order 4521 shipped")
print(m.group())                 # 4521   (.group() is the matched text)

# re.match anchors at the START; re.fullmatch requires the WHOLE string to match.
print(re.fullmatch(r"\d{4}-\d{2}-\d{2}", "2026-01-15") is not None)   # True
print(re.fullmatch(r"\d{4}-\d{2}-\d{2}", "2026-1-15") is not None)    # False

# -------------------------------------------------------------------------
# GROUPS: parentheses capture parts. This is how you PARSE.
# -------------------------------------------------------------------------
line = "2026-01-15 09:30:12 ERROR db: connection timed out after 30s"
pattern = r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (\w+): (.*)$"
m = re.match(pattern, line)
date, time_, level, component, message = m.groups()
print(level, component, "->", message)

# Named groups read better: (?P<name>...)
pat = re.compile(r"(?P<level>ERROR|WARN|INFO) (?P<component>\w+):")   # compile = reuse
m = pat.search(line)
print(m.group("level"), m.group("component"))     # ERROR db

# -------------------------------------------------------------------------
# re.findall: every match. Pull all links out of some HTML — the crawler's core.
# -------------------------------------------------------------------------
html = '<a href="/about">About</a> <a href="https://x.com/p?q=1">X</a> <img src="/i.png">'
links = re.findall(r'href="([^"]+)"', html)     # [^"]+ = everything up to the next quote
print(links)                                    # ['/about', 'https://x.com/p?q=1']

# -------------------------------------------------------------------------
# re.sub: search-and-replace. Mask card numbers, normalise whitespace.
# -------------------------------------------------------------------------
print(re.sub(r"\d{12}(\d{4})", r"************\1", "card 1234567890123456"))
print(re.sub(r"\s+", " ", "too    many\n\nspaces").strip())    # too many spaces

# re.split: split on a pattern instead of a fixed string.
print(re.split(r"[,;]\s*", "a, b;c ,d"))       # ['a', 'b', 'c ', 'd']

# -------------------------------------------------------------------------
# GREEDY vs LAZY: * and + grab as much as possible. Add ? to grab as little.
# -------------------------------------------------------------------------
tags = "<b>bold</b> and <i>italic</i>"
print(re.findall(r"<.+>", tags))     # ['<b>bold</b> and <i>italic</i>']  — greedy, one match
print(re.findall(r"<.+?>", tags))    # ['<b>', '</b>', '<i>', '</i>']       — lazy

# -------------------------------------------------------------------------
# A REAL log-parsing pattern: count errors per component.
# -------------------------------------------------------------------------
log = """2026-01-15 09:30:12 ERROR db: timeout
2026-01-15 09:30:13 INFO api: ok
2026-01-15 09:30:15 ERROR api: 500
2026-01-15 09:30:16 ERROR db: timeout"""
counts = {}
for lvl, comp in re.findall(r" (ERROR|WARN) (\w+):", log):
    counts[comp] = counts.get(comp, 0) + 1
print(counts)                         # {'db': 2, 'api': 1}

# -------------------------------------------------------------------------
# When NOT to use regex: parsing full HTML/JSON/URLs. Use a real parser
# (html.parser / BeautifulSoup, json, urllib.parse). Regex is for lines and tokens.
# -------------------------------------------------------------------------
# TRY: write `is_valid_email(s)` with fullmatch: letters/digits/._- then @ then a
# domain with at least one dot. Test it on 5 good and 5 bad addresses.
# Practice interactively at regex101.com (pick the Python flavour).
