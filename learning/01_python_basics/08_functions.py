"""
LESSON 8 — Functions
====================

A FUNCTION is a reusable, named block of code. You write it once, then "call" it
whenever you need it. Functions are how we organize code and avoid repetition —
and every interview answer you write will be a function.

Run me:
    python3 learning/01_python_basics/08_functions.py
"""

# -------------------------------------------------------------------------
# DEFINING a function with `def`. The (parentheses) hold "parameters" —
# placeholders for the inputs the function will receive.
# -------------------------------------------------------------------------
def greet(name):
    print(f"Hello, {name}! Welcome.")

# CALLING the function — this is when the code inside actually runs.
greet("Alice")     # the value "Alice" becomes `name` inside the function
greet("Bob")       # reuse it as many times as you want

print()

# -------------------------------------------------------------------------
# RETURN values — a function can compute something and hand it back with
# `return`, so the caller can use the result. This is the most important part.
# -------------------------------------------------------------------------
def add(a, b):
    return a + b           # send the result back to whoever called add()

result = add(3, 5)         # result now holds 8
print("3 + 5 =", result)
print("10 + 20 =", add(10, 20))   # you can use the return value directly

# Note the difference:
#   print() DISPLAYS something on screen but gives nothing back.
#   return  HANDS A VALUE BACK so your program can keep using it.
# In interviews you almost always `return` the answer, not print it.

print()

# -------------------------------------------------------------------------
# A function can have several parameters, and you can give DEFAULT values.
# -------------------------------------------------------------------------
def power(base, exponent=2):     # exponent defaults to 2 if not provided
    return base ** exponent

print("power(5)    =", power(5))      # 25  (uses default exponent 2)
print("power(2, 10)=", power(2, 10))  # 1024

print()

# -------------------------------------------------------------------------
# A realistic example: a function that does real work and returns a result.
# -------------------------------------------------------------------------
def average(numbers):
    """Return the average (mean) of a list of numbers."""
    if len(numbers) == 0:        # guard against dividing by zero
        return 0
    return sum(numbers) / len(numbers)

print("Average of [10, 20, 30]:", average([10, 20, 30]))   # 20.0
print("Average of []:", average([]))                       # 0

print()

# -------------------------------------------------------------------------
# SCOPE — variables created INSIDE a function only exist inside it.
# -------------------------------------------------------------------------
def make_message():
    secret = "I only exist inside this function"
    return secret

print(make_message())
# print(secret)   # <- This would ERROR: `secret` doesn't exist out here.
#                 #    Try uncommenting it to see the NameError.


# -------------------------------------------------------------------------
# 🧪 YOUR TURN:
#   1. Write a function `square(n)` that RETURNS n * n. Test it with square(6).
#   2. Write `is_even(n)` that returns True/False using  n % 2 == 0.
#   3. Write `greatest(a, b)` that returns the larger of two numbers
#      (use an if/else, or the built-in max — try both!).
#   4. Write `count_vowels(word)` that returns how many vowels (a,e,i,o,u)
#      are in a word. Hint: loop over the word and use `if letter in "aeiou"`.
# -------------------------------------------------------------------------
