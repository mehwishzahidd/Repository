"""
LESSON 2 — Errors and exceptions
================================

When something goes wrong, Python "raises" an exception. Unhandled, it crashes the
program with a traceback. Handled, your program can recover, retry, or fail with a
clear message. Production code is mostly about deciding what to do when things fail.

Run me:
    python3 stages/02_programming/02_exceptions.py
"""

# -------------------------------------------------------------------------
# try / except: attempt something; if it raises, run the except block instead.
# -------------------------------------------------------------------------
text = "42x"
try:
    number = int(text)
except ValueError:
    print(f"'{text}' is not a number")     # this runs; the program keeps going

# -------------------------------------------------------------------------
# Catch SPECIFIC exceptions. A bare `except:` hides bugs you wanted to see.
# -------------------------------------------------------------------------
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        print("both arguments must be numbers")
        return None

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # None
print(safe_divide(10, "x"))   # prints the message, returns None

# -------------------------------------------------------------------------
# else runs if NO exception happened; finally ALWAYS runs (cleanup goes here).
# -------------------------------------------------------------------------
try:
    value = int("7")
except ValueError:
    print("bad input")
else:
    print("parsed:", value)
finally:
    print("this line runs no matter what")

# -------------------------------------------------------------------------
# RAISING your own. Validate inputs and fail loudly and early.
# -------------------------------------------------------------------------
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError(f"insufficient funds: balance {balance}, requested {amount}")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:        # `as e` gives you the exception object
    print("Error:", e)

# -------------------------------------------------------------------------
# CUSTOM exception classes. Name the failure so callers can catch exactly it.
# -------------------------------------------------------------------------
class InsufficientFunds(Exception):
    """Raised when a withdrawal exceeds the balance."""

def withdraw2(balance, amount):
    if amount > balance:
        raise InsufficientFunds(f"need {amount - balance} more")
    return balance - amount

try:
    withdraw2(10, 25)
except InsufficientFunds as e:
    print("Custom error caught:", e)

# -------------------------------------------------------------------------
# Exceptions travel UP the call stack until something catches them.
# -------------------------------------------------------------------------
def inner():
    raise RuntimeError("deep failure")

def outer():
    inner()          # doesn't catch it, so it keeps travelling up

try:
    outer()
except RuntimeError as e:
    print("caught at the top:", e)

# -------------------------------------------------------------------------
# READ THE TRACEBACK. Uncomment the next line, run, and read bottom-up:
# the last line says WHAT went wrong; the lines above say WHERE.
# -------------------------------------------------------------------------
# int("not a number")

# TRY: write `parse_age(text)` that returns an int, raising ValueError with a
# helpful message if the text isn't a number or the age is outside 0–150.
