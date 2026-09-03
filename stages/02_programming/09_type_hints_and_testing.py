"""
LESSON 9 — Type hints, docstrings, and writing tests with pytest
================================================================

Type hints say what a function expects and returns. They don't change how code
runs, but editors and `mypy` use them to catch bugs, and interviewers read them
as a sign of care. Tests are small programs that check your program — and the
habit that separates "it ran once" from "it works".

Run me:
    python3 stages/02_programming/09_type_hints_and_testing.py
Then run the tests at the bottom with:
    python3 -m pytest stages/02_programming/09_type_hints_and_testing.py -v
"""
from dataclasses import dataclass
from typing import Optional

# -------------------------------------------------------------------------
# TYPE HINTS: name: type for parameters, -> type for the return value.
# -------------------------------------------------------------------------
def average(values: list[float]) -> float:
    """Return the mean of `values`. Raises ValueError on an empty list."""
    if not values:
        raise ValueError("average of empty list")
    return sum(values) / len(values)

def find_user(users: dict[str, int], name: str) -> Optional[int]:   # int or None
    """Return the user's id, or None if unknown."""
    return users.get(name)

@dataclass
class Order:
    order_id: int
    amount: float
    note: str = ""

def total(orders: list[Order]) -> float:
    return round(sum(o.amount for o in orders), 2)

print(average([1, 2, 3]))                       # 2.0
print(find_user({"ana": 1}, "zed"))             # None
print(total([Order(1, 9.99), Order(2, 5.01)]))  # 15.0

# Hints are documentation the machine can check. Try:  python3 -m mypy <this file>
# (install with: pip install mypy). It will flag e.g. average("abc").

# -------------------------------------------------------------------------
# DOCSTRINGS: the first string in a function/class. Say what it does, its
# inputs, what it returns, and what it raises. Keep it short and true.
# -------------------------------------------------------------------------
print(average.__doc__)

# -------------------------------------------------------------------------
# TESTS. pytest finds functions named test_* and runs them. `assert` is the
# whole API. Arrange (set up) → Act (call) → Assert (check).
# -------------------------------------------------------------------------
try:
    import pytest   # pip install pytest
except ImportError:  # the lesson still runs without it; the tests need it
    print("\n(pytest is not installed — run `pip install pytest` to run the tests below)")
    pytest = None

if pytest is None:
    raise SystemExit(0)

def test_average_basic():
    assert average([2, 4]) == 3.0

def test_average_single():
    assert average([7]) == 7.0

def test_average_empty_raises():
    with pytest.raises(ValueError):      # the test PASSES if the error is raised
        average([])

def test_find_user_missing_is_none():
    assert find_user({}, "x") is None

# Parametrize: one test, many cases. Edge cases belong here.
@pytest.mark.parametrize("orders, expected", [
    ([], 0.0),                                        # empty
    ([Order(1, 0.0)], 0.0),                           # zero
    ([Order(1, 0.1), Order(2, 0.2)], 0.3),            # float rounding
    ([Order(1, 5.0), Order(1, 5.0)], 10.0),           # duplicate ids still count
])
def test_total(orders, expected):
    assert total(orders) == expected

# A FIXTURE: shared setup, requested by name as a parameter.
@pytest.fixture
def sample_users():
    return {"ana": 1, "ben": 2}

def test_find_user_present(sample_users):
    assert find_user(sample_users, "ben") == 2

# -------------------------------------------------------------------------
# THE HABIT: for every function, at least one happy-path test and one edge or
# failure test. Ask: empty? zero? duplicate? huge? wrong type? That question
# is the Anthropic drill from LEETCODE.md, and it starts here.
# -------------------------------------------------------------------------
# TRY: write `parse_price("$12.50") -> 12.5` with tests for "$0", "abc", "" and
# "$1,000.00". Decide what each should do BEFORE writing the code.
