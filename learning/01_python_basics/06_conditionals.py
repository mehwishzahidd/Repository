"""
LESSON 6 — Conditionals (making decisions)
==========================================

Programs become powerful when they can make decisions: "IF this is true, do that."
That's what `if` / `elif` / `else` are for.

Run me:
    python3 learning/01_python_basics/06_conditionals.py
"""

# -------------------------------------------------------------------------
# COMPARISON OPERATORS produce a boolean (True or False):
#     ==  equal to            (note: TWO equals signs! one = is assignment)
#     !=  not equal to
#     <   less than           >   greater than
#     <=  less than or equal  >=  greater than or equal
# -------------------------------------------------------------------------
print("5 == 5 :", 5 == 5)    # True
print("5 != 3 :", 5 != 3)    # True
print("4 > 10 :", 4 > 10)    # False

print()

# -------------------------------------------------------------------------
# THE if STATEMENT
# Note the colon ":" and the INDENTATION (4 spaces). In Python, indentation
# is not decoration — it defines which lines belong to the `if`. This matters!
# -------------------------------------------------------------------------
temperature = 30

if temperature > 25:
    print("It's hot out. Wear shorts.")   # runs only if the condition is True

# if / else : do one thing OR another.
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("Too young to vote.")

print()

# -------------------------------------------------------------------------
# if / elif / else : choose among MANY options. Python checks them top to
# bottom and runs the FIRST one that's True, then skips the rest.
# -------------------------------------------------------------------------
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"A score of {score} earns a {grade}.")   # B

print()

# -------------------------------------------------------------------------
# COMBINING CONDITIONS with  and / or / not
#   and  -> True only if BOTH sides are True
#   or   -> True if AT LEAST ONE side is True
#   not  -> flips True<->False
# -------------------------------------------------------------------------
has_ticket = True
has_id = False

if has_ticket and has_id:
    print("Welcome in!")
else:
    print("Sorry, you need both a ticket AND an id.")

age = 20
if age < 13 or age >= 65:
    print("You get a discount.")
else:
    print("Full price.")

# A common interview pattern: check if a number is in a range.
n = 7
if 1 <= n <= 10:    # Python lets you chain comparisons like math!
    print(f"{n} is between 1 and 10.")


# -------------------------------------------------------------------------
# 🧪 YOUR TURN:
#   1. Write an if/else that prints "even" or "odd" for a number n.
#      Hint: use the modulo trick from lesson 3 ->  n % 2 == 0
#   2. Write if/elif/else that, given an hour (0-23), prints "morning"
#      (before 12), "afternoon" (12-17), or "evening" (18+).
#   3. Make a variable `is_weekend = True` and print "relax" if it's the
#      weekend, otherwise "work".
# -------------------------------------------------------------------------
