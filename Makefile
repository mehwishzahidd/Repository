.PHONY: help check test lessons attack lint anki

help:
	@echo "make check    - run every stage's auto-grader"
	@echo "make lessons  - run every runnable lesson file (smoke test)"
	@echo "make test     - run pytest over stages/ and projects/"
	@echo "make attack   - run every project attack script (skips unimplemented projects)"
	@echo "make lint     - ruff, if installed"
	@echo "make anki     - regenerate anki/glossary.tsv from GLOSSARY.md"

check:
	@for c in stages/*/exercises/check.py; do echo "== $$c"; python3 $$c | tail -3; done

lessons:
	@for f in stages/0*/[0-9]*.py; do python3 $$f > /dev/null 2>&1 && echo "ok   $$f" || echo "FAIL $$f"; done; rm -rf stages/*/_scratch

test:
	@python3 -m pytest stages projects -q 2>/dev/null || echo "pytest not installed or no tests yet (pip install pytest)"

attack:
	@for a in projects/*/attack.py; do echo "== $$a"; python3 $$a; done

lint:
	@command -v ruff >/dev/null && ruff check stages projects || echo "ruff not installed (pip install ruff)"

anki:
	@python3 anki/build_deck.py
