"""
LESSON 3 — Numbers and Math
===========================

Python is a great calculator. Here are the operators you'll use constantly,
including two "special" division operators that matter a LOT in interviews.

Run me:
    python3 stages/01_python/03_numbers_and_math.py
"""

a = 17
b = 5

# The everyday operators:
print("Addition:        a + b =", a + b)    # 22
print("Subtraction:     a - b =", a - b)    # 12
print("Multiplication:  a * b =", a * b)    # 85
print("Division:        a / b =", a / b)    # 3.4   <- always gives a float!

print()

# -------------------------------------------------------------------------
# TWO SPECIAL OPERATORS — memorize these, they appear in interview problems:
# -------------------------------------------------------------------------

# Floor division //  — divides and throws away the remainder (rounds DOWN).
print("Floor division:  a // b =", a // b)   # 3   (17 / 5 = 3.4, drop the .4)

# Modulo %  — gives the REMAINDER of a division.
print("Modulo:          a % b  =", a % b)    # 2   (17 = 3*5 + 2, remainder 2)

# Why care about %?  A classic trick: a number is EVEN if  n % 2 == 0.
print("Is 10 even?", 10 % 2 == 0)   # True
print("Is 7 even? ", 7 % 2 == 0)    # False

print()

# Exponent ** — "to the power of"
print("3 to the power 4:", 3 ** 4)   # 81
print("Square root of 9:", 9 ** 0.5) # 3.0  (a power of 0.5 = square root)

# -------------------------------------------------------------------------
# ORDER OF OPERATIONS is the same as in math (PEMDAS).
# Use parentheses to make your intent clear and control the order.
# -------------------------------------------------------------------------
print("2 + 3 * 4   =", 2 + 3 * 4)     # 14  (multiplication happens first)
print("(2 + 3) * 4 =", (2 + 3) * 4)   # 20  (parentheses force addition first)

# -------------------------------------------------------------------------
# HANDY SHORTCUTS for updating a variable based on its current value:
# -------------------------------------------------------------------------
score = 10
score = score + 5     # the long way
print("Score:", score)  # 15

score += 5            # shortcut for  score = score + 5
print("Score:", score)  # 20
# The same shortcut works for  -=  *=  /=  //=  %=

# Useful built-in math functions (no import needed):
print("abs(-8)      =", abs(-8))        # 8   (absolute value)
print("round(3.7)   =", round(3.7))     # 4
print("max(4, 9, 2) =", max(4, 9, 2))   # 9
print("min(4, 9, 2) =", min(4, 9, 2))   # 2


# -------------------------------------------------------------------------
# 🧪 YOUR TURN:
#   1. Print the remainder when 100 is divided by 7.  (Answer should be 2.)
#   2. Use % to check whether 51 is divisible by 3 (i.e. 51 % 3 == 0).
#   3. A clock: if it's 22:00 now, what hour is it 5 hours later on a 24-hour
#      clock? Compute  (22 + 5) % 24 .  (This is why % is everywhere!)
# -------------------------------------------------------------------------
