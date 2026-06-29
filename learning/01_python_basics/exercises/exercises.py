"""
Module 01 — EXERCISES
=====================

Fill in each function below. Replace the `pass` (or `return None`) with your own
code so the function does what its instructions say.

Check your answers any time by running:
    python3 learning/01_python_basics/exercises/check.py

Do them in order. Re-read the lesson file if you get stuck — each exercise maps
to something you've already seen.
"""


# -------------------------------------------------------------------------
# EXERCISE 1 — say_hello  (lesson 4: strings / f-strings)
# Return a greeting string. For the input "Sam", return the string "Hello, Sam!"
# (Return it — do NOT print it.)
# -------------------------------------------------------------------------
def say_hello(name):
    # TODO: replace this with: return an f-string like f"Hello, {name}!"
    pass


# -------------------------------------------------------------------------
# EXERCISE 2 — rectangle_area  (lesson 3 & 8: math + functions)
# Return the area of a rectangle: width times height.
# rectangle_area(4, 5)  ->  20
# -------------------------------------------------------------------------
def rectangle_area(width, height):
    # TODO
    pass


# -------------------------------------------------------------------------
# EXERCISE 3 — is_even  (lesson 3 & 6: modulo + booleans)
# Return True if n is even, False if it is odd.
# is_even(4) -> True     is_even(7) -> False
# Hint: a number is even when  n % 2 == 0
# -------------------------------------------------------------------------
def is_even(n):
    # TODO
    pass


# -------------------------------------------------------------------------
# EXERCISE 4 — sum_list  (lesson 7: loops)
# Return the sum of all numbers in the list.
# sum_list([1, 2, 3, 4]) -> 10      sum_list([]) -> 0
# (Try it with a for loop and an accumulator. The built-in sum() also works!)
# -------------------------------------------------------------------------
def sum_list(numbers):
    # TODO
    pass


# -------------------------------------------------------------------------
# EXERCISE 5 — count_vowels  (lesson 4, 6, 7: strings + loops + if)
# Return how many vowels (a, e, i, o, u) are in the word. Assume lowercase.
# count_vowels("hello") -> 2        count_vowels("xyz") -> 0
# Hint: loop over each letter; if letter in "aeiou": add 1 to a counter.
# -------------------------------------------------------------------------
def count_vowels(word):
    # TODO
    pass


# -------------------------------------------------------------------------
# EXERCISE 6 — reverse_string  (lesson 4: slicing)
# Return the word spelled backwards.
# reverse_string("hello") -> "olleh"
# Hint: there's a one-line slicing trick from lesson 4 ...  [::-1]
# -------------------------------------------------------------------------
def reverse_string(s):
    # TODO
    pass


# -------------------------------------------------------------------------
# EXERCISE 7 — largest  (lesson 5 & 7: lists + loops)
# Return the largest number in the list. Assume the list is not empty.
# largest([3, 9, 2, 7]) -> 9
# (The built-in max() works, but try writing it with a loop too, for practice!)
# -------------------------------------------------------------------------
def largest(numbers):
    # TODO
    pass


# -------------------------------------------------------------------------
# EXERCISE 8 — fizzbuzz  (THE classic interview warm-up! lessons 3, 6, 8)
# For a number n, return:
#   "FizzBuzz" if n is divisible by BOTH 3 and 5
#   "Fizz"     if n is divisible by 3 (only)
#   "Buzz"     if n is divisible by 5 (only)
#   otherwise  the number itself as a STRING, e.g. str(n)
# fizzbuzz(3)->"Fizz"  fizzbuzz(5)->"Buzz"  fizzbuzz(15)->"FizzBuzz"  fizzbuzz(7)->"7"
# Hint: check the BOTH case FIRST, or it'll never run. Order matters!
# -------------------------------------------------------------------------
def fizzbuzz(n):
    # TODO
    pass
