# P-mini — Sampling profiler → trace events (Stage 03, revisited in Stage 13)

## Interface contract
```python
from profiler import samples_to_events     # projects/pmini_profiler/profiler.py
events = samples_to_events(samples, interval_ms=10)
```
`samples` is a list of stacks, outermost first, one per tick:
```python
samples = [
    ["main"],
    ["main", "foo"],
    ["main", "foo", "bar"],
    ["main", "foo"],
    ["main", "foo", "foo"],      # recursion: foo called foo
    ["main", "foo"],
    ["main"],
]
```
Output: a list of `(name, "B"|"E", time_ms, depth)` events, in order — `B` when a frame
first appears at a stack position, `E` when it disappears. Track frames by **position**,
not name: in tick 4 the inner `foo` at depth 2 is a *new* frame; the outer `foo` at depth 1
is still running.

Tests to write: the sample above · a missing tick · an empty stack for a while ·
1,000-deep recursion · two functions swapping at the same depth between ticks.
In Stage 13, emit Chrome trace-event JSON and open it in Perfetto.
