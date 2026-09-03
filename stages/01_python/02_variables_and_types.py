"""
LESSON 2 — Variables and Types
==============================

A VARIABLE is a name that stores a value, like a labeled box.
You create one with:   name = value
The "=" means "store the value on the right into the name on the left."

Run me:
    python3 stages/01_python/02_variables_and_types.py
"""

# Create a variable called `age` and store the number 25 in it.
age = 25

# Now the name `age` stands for 25 everywhere we use it.
print("Age:", age)

# We can change ("reassign") a variable at any time.
age = 26
print("Next year's age:", age)

# -------------------------------------------------------------------------
# THE 4 BASIC TYPES you'll use constantly:
# -------------------------------------------------------------------------

# 1) int  — whole numbers (no decimal point)
count = 42

# 2) float — numbers WITH a decimal point
price = 9.99

# 3) str  — "string", i.e. text, always in quotes
name = "Ada"

# 4) bool — boolean, either True or False (note the capital letters!)
is_student = True

# The built-in type() function tells you what type a value is.
print("count is a", type(count))       # <class 'int'>
print("price is a", type(price))       # <class 'float'>
print("name is a", type(name))         # <class 'str'>
print("is_student is a", type(is_student))  # <class 'bool'>

# -------------------------------------------------------------------------
# GOOD VARIABLE NAMES make code readable. Rules & conventions:
#   - use lowercase_with_underscores (called "snake_case")
#   - make them descriptive:  total_price  is better than  tp
#   - they can't start with a number or contain spaces
# -------------------------------------------------------------------------
first_name = "Grace"
last_name = "Hopper"

# You can combine variables. For text, "+" glues strings together.
full_name = first_name + " " + last_name
print("Full name:", full_name)

# CONVERTING between types: sometimes you need to change a value's type.
# input from users always comes in as a string, so this is very common.
year_as_text = "2024"            # this is a STRING, not a number
year_as_number = int(year_as_text)   # convert it to an int
print("Next year:", year_as_number + 1)   # now math works: 2025

# str(...) goes the other way, turning a number into text.
print("I am " + str(age) + " years old.")


# -------------------------------------------------------------------------
# 🧪 YOUR TURN:
#   1. Make a variable `city` holding your city as a string, and print it.
#   2. Make two int variables and print their sum.
#   3. What happens if you write:  print("5" + 5)  ? Try it and read the error.
#      (You can't add a string and a number — that's a TypeError.)
#   4. Fix it using int("5") + 5 . Now it works!
# -------------------------------------------------------------------------
