# P7 — Mini database (Stage 12) — the OpenAI design round, built
`CREATE TABLE`, `INSERT`, `SELECT ... WHERE`, `JOIN` (nested-loop → hash → sort-merge),
a B+tree or hash index, row- vs column-oriented storage for one table, a write-ahead
log, then MVCC snapshot isolation.

## Interface contract (suggested)
```python
db = Database(path)          # projects/p07_mini_db/minidb/
db.execute("CREATE TABLE users (id INT, name TEXT)")
db.execute("INSERT INTO users VALUES (1, 'ana')")
db.execute("SELECT u.name, o.item FROM users u JOIN orders o ON u.id = o.user_id WHERE o.amount > 5")
with db.transaction() as tx: ...
```
## Crash tests live in your `tests/`
Use `os.fork()` or a subprocess and `kill -9` between the WAL write and the data write;
on restart the committed row must exist and the uncommitted one must not. Benchmark the
three joins at 1k×1k, 100k×100, and 100k×100k rows; record which wins and why.
