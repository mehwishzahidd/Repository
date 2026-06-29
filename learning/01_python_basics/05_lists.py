"""
LESSON 5 — Lists
================

A LIST is an ordered collection of items. It is THE most-used data structure in
coding interviews, so this lesson matters a lot. A list can hold anything, and
you can change it (add, remove, reorder items).

Run me:
    python3 learning/01_python_basics/05_lists.py
"""

# Create a list with square brackets, items separated by commas.
fruits = ["apple", "banana", "cherry"]
print("The list:", fruits)
print("How many items:", len(fruits))   # 3

# INDEXING works just like strings — starts at 0.
print("First fruit:", fruits[0])    # apple
print("Last fruit: ", fruits[-1])   # cherry

# Lists are MUTABLE — you can change an item in place.
fruits[1] = "blueberry"
print("After changing index 1:", fruits)   # ['apple', 'blueberry', 'cherry']

print()

# -------------------------------------------------------------------------
# ADDING and REMOVING items
# -------------------------------------------------------------------------
numbers = [10, 20, 30]

numbers.append(40)        # add to the END
print("After append:", numbers)   # [10, 20, 30, 40]

numbers.insert(0, 5)      # insert 5 at index 0 (the front)
print("After insert:", numbers)   # [5, 10, 20, 30, 40]

numbers.pop()             # remove and return the LAST item
print("After pop:   ", numbers)   # [5, 10, 20, 30]

numbers.remove(20)        # remove the first matching VALUE (not index)
print("After remove:", numbers)   # [5, 10, 30]

print()

# -------------------------------------------------------------------------
# SLICING works on lists too (same rules as strings)
# -------------------------------------------------------------------------
letters = ["a", "b", "c", "d", "e"]
print("letters[1:4] =", letters[1:4])   # ['b', 'c', 'd']
print("letters[:2]  =", letters[:2])    # ['a', 'b']
print("letters[::-1]=", letters[::-1])  # ['e', 'd', 'c', 'b', 'a'] (reversed)

print()

# -------------------------------------------------------------------------
# HANDY LIST OPERATIONS you'll use in interviews
# -------------------------------------------------------------------------
scores = [88, 72, 95, 60, 95]

print("Sum:    ", sum(scores))           # 410
print("Max:    ", max(scores))           # 95
print("Min:    ", min(scores))           # 60
print("Sorted: ", sorted(scores))        # [60, 72, 88, 95, 95] (returns a NEW list)
print("95 in scores?", 95 in scores)     # True ('in' checks membership)
print("Count of 95:", scores.count(95))  # 2

# .sort() sorts the list IN PLACE (changes the original), no new list returned.
scores.sort()
print("After .sort():", scores)          # [60, 72, 88, 95, 95]
scores.sort(reverse=True)
print("Sorted descending:", scores)      # [95, 95, 88, 72, 60]


# -------------------------------------------------------------------------
# 🧪 YOUR TURN:
#   1. Make a list of 3 of your favorite movies and print the second one.
#   2. append() a fourth movie, then print the whole list.
#   3. Make a list of numbers [4, 1, 7, 3] and print its sum and its max.
#   4. Sort that number list and print it. Then reverse it with [::-1].
# -------------------------------------------------------------------------
