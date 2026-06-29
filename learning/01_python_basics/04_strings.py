"""
LESSON 4 — Strings (text)
=========================

A STRING is text. Strings are everywhere in interviews, so get comfortable here.

Run me:
    python3 learning/01_python_basics/04_strings.py
"""

greeting = "Hello"
name = "World"

# JOINING strings with + is called "concatenation".
print(greeting + ", " + name + "!")   # Hello, World!

# The cleanest way to build strings is an F-STRING. Put f before the quotes,
# then drop variables inside {curly braces}. Use this everywhere!
age = 30
print(f"My name is {name} and I am {age} years old.")

# You can even put math or expressions inside the braces:
print(f"In 5 years I'll be {age + 5}.")

print()

# -------------------------------------------------------------------------
# LENGTH and INDEXING
# -------------------------------------------------------------------------
word = "Python"

# len() gives the number of characters.
print("Length of 'Python':", len(word))   # 6

# INDEXING: each character has a position (index) STARTING AT 0.
#   P  y  t  h  o  n
#   0  1  2  3  4  5
print("First character:", word[0])    # P  (not 1! indexing starts at 0)
print("Third character:", word[2])    # t

# NEGATIVE indices count from the end. -1 is the last character.
print("Last character: ", word[-1])   # n

print()

# -------------------------------------------------------------------------
# SLICING — grab a chunk:  word[start:stop]  (stop is NOT included)
# -------------------------------------------------------------------------
print("word[0:3] =", word[0:3])   # 'Pyt'  (indices 0,1,2 — stop=3 excluded)
print("word[2:]  =", word[2:])    # 'thon' (from index 2 to the end)
print("word[:4]  =", word[:4])    # 'Pyth' (from the start up to index 4)
print("word[::-1]=", word[::-1])  # 'nohtyP' (a neat trick to REVERSE a string)

print()

# -------------------------------------------------------------------------
# USEFUL STRING METHODS (a "method" is a function attached to a value with a dot)
# -------------------------------------------------------------------------
phrase = "  Learning Python is Fun  "

print(phrase.upper())          # "  LEARNING PYTHON IS FUN  "
print(phrase.lower())          # "  learning python is fun  "
print(phrase.strip())          # "Learning Python is Fun"  (removes outer spaces)
print(phrase.strip().replace("Fun", "Awesome"))  # swap a word
print("Python" in phrase)      # True  ('in' checks if text appears inside)
print(phrase.strip().split())  # ['Learning', 'Python', 'is', 'Fun'] (split into a list)

# Note: strings are IMMUTABLE — methods return a NEW string, they don't change
# the original. That's why we chain them or store the result in a variable.


# -------------------------------------------------------------------------
# 🧪 YOUR TURN:
#   1. Make a variable with your full name and print its length.
#   2. Print just the first letter of your name using indexing.
#   3. Use an f-string to print: "Hi <name>, you have <n> new messages."
#   4. Reverse the word "racecar" with [::-1]. Is it the same backwards? (Yes!)
# -------------------------------------------------------------------------
